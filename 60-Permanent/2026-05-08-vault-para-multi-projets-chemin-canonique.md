---
ai_writable: false
area: null
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- PARA
- /srv/vault
- symlink
- 50-MOCs
- 10-Projects
id: 20260508040100-vault-para-multi-projets-chemin-canonique
intent: decision
last-accessed: '2026-05-08'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/openclaw-plugin/2026-05-07-1325-session-158ff0de.md
- 10-Projects/openclaw-plugin/2026-05-07-1340-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1433-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1532-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1446-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1520-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1437-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1307-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1513-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1551-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1655-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1549-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1517-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1420-session-158ff0de.md
- 10-Projects/pms-jardin-tropical/2026-05-07-1459-session-158ff0de.md
source_session: 158ff0de-03dd-41ec-927d-9cb29780c3d1
status: active
summary: Vault centralisé `/srv/vault` avec PARA et symlink legacy rétro-compatible.
tags:
- permanent
- synthesized
- obsidian
- structure
- canonical-path
- rétro-compatibility
tier: warm
title: Vault PARA multi-projets chemin canonique
topic_cluster: vault-architecture
type: permanent-note
updated: '2026-05-08'
---

Structure PARA canonique établie sur VPS pour unifier multi-projets :

- **Chemin canonical** : `/srv/vault/` (symlink rétro-compat `/srv/vault-jardin-tropical/` pour anciennes routes)
- **Hiérarchie PARA** : `00-Inbox`, `05-Daily`, `10-Projects/<slug>/`, `20-Areas`, `30-Resources`, `40-Archives`, `50-MOCs`, `60-Permanent`, `90-Meta`

Chaque projet a dossier `/10-Projects/pms-jardin-tropical/`, `/10-Projects/openclaw-plugin/`, etc. Les MOCs centralisés en `/50-MOCs/`. Cela prévient collisions de noms, clarifie sémantique, et facilite migrations futures. Cette structure restera stable 12+ mois.