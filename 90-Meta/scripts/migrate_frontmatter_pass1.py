#!/usr/bin/env python3
"""
Phase 2 Pass 1 — Frontmatter structurel (déterministe, 0 token LLM).

Ajoute aux notes existantes les champs nécessaires pour future-proof :
- id (YYYYMMDDHHMM-slug, dérivé de created + filename)
- embed_model_version: null
- embed_hash: null
- last-accessed (= updated)

Préserve tous les autres champs existants. Idempotent.

Usage:
    python3 migrate_frontmatter_pass1.py [--dry-run] [vault_root]
"""

import sys
import re
import os
import hashlib
from pathlib import Path
from datetime import datetime

VAULT = Path(sys.argv[-1] if sys.argv[-1].startswith("/") else "/srv/vault")
DRY_RUN = "--dry-run" in sys.argv

# Notes à exclure : déjà créées en Phase 1 avec frontmatter complet
EXCLUDE_PATTERNS = [
    "_MOC-*.md",
    "INDEX.md",
    "AGENTS.md",
    "README.md",
    "note-schema.md",
    "note-template.md",
]

def is_excluded(path: Path) -> bool:
    for pat in EXCLUDE_PATTERNS:
        if path.match(pat):
            return True
    if "/.git/" in str(path):
        return True
    if str(path).endswith(".gitignore"):
        return True
    return False

def slugify(name: str) -> str:
    s = re.sub(r"\.md$", "", name)
    s = re.sub(r"[^a-zA-Z0-9-]+", "-", s).lower().strip("-")
    return s[:60]

def parse_frontmatter(content: str):
    """Returns (frontmatter_dict, body, has_frontmatter)"""
    if not content.startswith("---\n"):
        return {}, content, False
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content, False
    fm_text = content[4:end]
    body = content[end + 5:]
    fm = {}
    current_key = None
    for line in fm_text.split("\n"):
        if not line.strip():
            continue
        m = re.match(r"^([a-zA-Z_-]+)\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            fm[key] = val
            current_key = key
        elif current_key and (line.startswith("  ") or line.startswith("- ")):
            # multiline value (simplified — preserve as text)
            fm[current_key] = (fm.get(current_key, "") + "\n" + line).strip()
    return fm, body, True

def derive_id(path: Path, fm: dict) -> str:
    """Derive YYYYMMDDHHMM-slug from existing frontmatter or file mtime."""
    created = fm.get("created", "").strip().strip('"').strip("'")
    if re.match(r"^\d{4}-\d{2}-\d{2}$", created):
        date_part = created.replace("-", "")
        # Use filename mtime hour:minute for uniqueness
        mtime = datetime.fromtimestamp(path.stat().st_mtime)
        time_part = f"{mtime.hour:02d}{mtime.minute:02d}"
    else:
        mtime = datetime.fromtimestamp(path.stat().st_mtime)
        date_part = mtime.strftime("%Y%m%d")
        time_part = mtime.strftime("%H%M")
    slug = slugify(path.stem)
    return f"{date_part}{time_part}-{slug}"

def update_frontmatter_block(content: str, path: Path) -> tuple[str, list[str]]:
    """Returns (new_content, changes_log)."""
    fm, body, has_fm = parse_frontmatter(content)
    changes = []

    if not has_fm:
        # Skip files without any frontmatter (shouldn't happen in this vault)
        return content, ["SKIP: no frontmatter"]

    # 1. Add id if missing
    if "id" not in fm:
        new_id = derive_id(path, fm)
        fm["id"] = new_id
        changes.append(f"+ id: {new_id}")

    # 2. Add embed_model_version, embed_hash if missing
    for key in ["embed_model_version", "embed_hash"]:
        if key not in fm:
            fm[key] = "null"
            changes.append(f"+ {key}: null")

    # 3. Add last-accessed if missing (= updated)
    if "last-accessed" not in fm:
        fm["last-accessed"] = fm.get("updated", "2026-05-07")
        changes.append(f"+ last-accessed: {fm['last-accessed']}")

    if not changes:
        return content, []

    # Rebuild frontmatter (preserve order: existing keys first, then new)
    # Read original block to preserve formatting
    end = content.find("\n---\n", 4)
    original_fm = content[4:end]
    original_keys = []
    for line in original_fm.split("\n"):
        m = re.match(r"^([a-zA-Z_-]+)\s*:", line)
        if m and m.group(1) not in original_keys:
            original_keys.append(m.group(1))

    new_fm_lines = []
    # Preserve original lines
    for line in original_fm.split("\n"):
        new_fm_lines.append(line)

    # Append new keys at the end
    new_keys = [k for k in fm if k not in original_keys]
    for k in new_keys:
        v = fm[k]
        new_fm_lines.append(f"{k}: {v}")

    new_content = "---\n" + "\n".join(new_fm_lines) + "\n---\n" + body
    return new_content, changes

def main():
    md_files = []
    for root, dirs, files in os.walk(VAULT):
        if "/.git" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                md_files.append(Path(root) / f)

    md_files = [p for p in md_files if not is_excluded(p)]

    print(f"Found {len(md_files)} notes to scan (mode: {'DRY-RUN' if DRY_RUN else 'WRITE'})")
    print(f"Vault: {VAULT}\n")

    total_modified = 0
    for path in sorted(md_files):
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  ⚠️  {path.relative_to(VAULT)}: read error ({e})")
            continue

        new_content, changes = update_frontmatter_block(content, path)

        if changes and changes != ["SKIP: no frontmatter"]:
            total_modified += 1
            print(f"  ✓ {path.relative_to(VAULT)}")
            for c in changes:
                print(f"      {c}")
            if not DRY_RUN:
                path.write_text(new_content, encoding="utf-8")
        elif changes == ["SKIP: no frontmatter"]:
            print(f"  ⏭  {path.relative_to(VAULT)} (no frontmatter)")

    print(f"\nDone: {total_modified} notes modified ({'dry run, not written' if DRY_RUN else 'written'})")

if __name__ == "__main__":
    main()
