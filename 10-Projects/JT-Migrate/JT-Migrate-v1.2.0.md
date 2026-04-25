---
type: project
status: superseded
tags: [jt-migrate, version, feature]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "v1.2.0 — mode import-from-server-path (bypass upload HTTP, dépose archive via SCP dans incoming/)"
ai_writable: false
related:
  - "[[Plugin-jt-migrate]]"
  - "[[JT-Migrate-v1.1.0]]"
  - "[[JT-Migrate-v1.2.1]]"
  - "[[Bug-Apache-Timeout-300-vs-Uploads]]"
supersedes: "[[JT-Migrate-v1.1.0]]"
superseded_by: "[[JT-Migrate-v1.2.1]]"
---

# 📦 JT Migrate v1.2.0

## Status

❌ **Superseded** par [[JT-Migrate-v1.2.1]].

## Apport

### Mode import-from-server-path

Bypass l'upload HTTP qui était fragile sur les gros fichiers (cf. [[Bug-Apache-Timeout-300-vs-Uploads]]).

#### Workflow

1. User dépose le `.tar.gz` directement dans `wp-content/uploads/jt-migrate/incoming/` via **SCP** (ou côté server-to-server par `curl`)
2. UI WP → Plugins → JT Migrate → Import → onglet "Import depuis incoming/"
3. Liste des archives présentes, clic sur "Importer"
4. Pipeline d'import normal (extract → db → replace → files → cleanup) sans passer par upload HTTP

#### Implémentation

- `JT_Migrate_Import::ajax_from_path()` — équivalent de `ajax_upload()` mais lit depuis incoming/ au lieu de `$_FILES`
- Path direct vers le fichier (pas de copie dans le job_dir)
- Sécurité : `realpath()` + check que le path résolu est sous `incoming_dir/`, regex sur extension `.gz` / `.tgz`
- UI : panneau dépliable "📂 Ou : importer une archive déjà déposée sur le serveur"

### Bug subsistant (corrigé en v1.2.1)

L'extract utilisait toujours `PharData::extract()` qui crash sur archive > 100 MB en RAM.

## Liens

- [[Plugin-jt-migrate]]
- [[JT-Migrate-v1.2.1]]
