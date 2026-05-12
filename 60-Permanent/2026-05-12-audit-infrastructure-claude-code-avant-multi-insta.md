---
ai_writable: false
area: null
backlinks:
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- CANONICITY
- _VAULT-INDEX
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- Claude CLI
- MCPs
- plugins
- hooks
- settings
id: 20260512040406-audit-infrastructure-claude-code-avant-multi-insta
intent: lesson
last-accessed: '2026-05-12'
moc: null
project: null
related:
- CANONICITY
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-11-2202-session-d41c35b1.md
- 10-Projects/claude-system/2026-05-11-2154-session-d41c35b1.md
- 10-Projects/claude-system/2026-05-11-2146-session-d41c35b1.md
- 10-Projects/claude-system/2026-05-11-2125-session-d41c35b1.md
source_session: d41c35b1-20aa-48d5-b5d8-36100ffefa41
status: active
summary: Procédure d'audit système avant déployer Claude Code sur nouvelle instance
tags:
- permanent
- synthesized
- audit
- diagnostic
- multi-instance
- checklist
tier: warm
title: Audit infrastructure Claude Code avant multi-instance
topic_cluster: claude-code-ops
type: permanent-note
updated: '2026-05-12'
---

Avant étendre Claude Code vers Mac mini, auditer infrastructure VPS existante pour comprendre dépendances et chemins hardcodés.

**Versions & runtime** : `claude --version`, `node --version`, `codex --version`, `tailscale version`

**MCPs** : `claude mcp list` → vérifier quels MCPs actifs, leurs scopes (user/project/local), accessibilité (local vs SSH-tunnelable)

**Plugins & skills** : `ls /root/.claude/plugins/`, `ls /root/.claude/skills/` → empreinte disque

**Hooks & automation** : `ls /root/.claude/hooks/`, `head -N *.py` → vérifier dispatch_advisor, extract_memory, event listeners

**Settings** : `cat /root/.claude/settings.json` + `/root/.claude/settings.local.json` → scopes configuration (user global vs project-local), env vars, permission allowlists

**Auth & credentials** : `/root/.codex/auth.json` (Codex OAuth), Syncthing token, API keys locales

**Disk-heavy components** : vault-rag modèle (~2 GB), cached embeddings, offline datasets

Rationale : avant réplique archi Mac, identifier ce qui est répliquable (config, repos), ce qui requiert wrapper (MCP lourd), ce qui doit rester unique (secrets, tokens).

## Related

- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code