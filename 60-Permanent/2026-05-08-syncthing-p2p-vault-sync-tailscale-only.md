---
ai_writable: false
area: null
backlinks:
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
- CANONICITY
- Vault-Setup
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- Syncthing
- Tailscale
- /srv/vault
- ~/Documents/vault
id: 20260508040101-syncthing-p2p-vault-sync-tailscale-only
intent: config
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
- CANONICITY
- Vault-Setup
- _HEALTH
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
summary: Syncthing sync bidirectionnel `/srv/vault` ↔ Mac via Tailscale, discovery/relay
  off.
tags:
- permanent
- synthesized
- sync
- vps-mac
- security
- p2p
- .stignore
tier: warm
title: Syncthing P2P vault sync Tailscale-only
topic_cluster: vault-sync
type: permanent-note
updated: '2026-05-08'
---

Setup P2P vault VPS ↔ Mac (développement local) :

- **VPS** : `/srv/vault` partage, Syncthing en user-mode
- **Mac** : `~/Documents/vault` miroir
- **Transport** : Tailscale uniquement (VPS 100.98.218.10, port 22000 Syncthing bloqué publiquement)
- **GUI** : http://100.98.218.10:8384 (raphael/pwd via gui-password.txt)
- **Hardening** : global discovery off, relay off, rate-limiting ON
- **.stignore** : exclude logs, `.DS_Store`, fichiers temporaires

**Avantage** : chiffrage P2P, pas serveur tiers, latence basse Tailscale. **À noter** : Syncthing gourmand en file descriptors sur vaults >50k notes — monitorer via `lsof | grep syncthing`.

## Related

- [[Vault-Setup]] — Vault Setup
- [[2026-05-08-vault-para-multi-projets-chemin-canonique]] — Vault PARA multi-projets chemin canonique
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[_HEALTH]] — Vault Health Check
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-10-config-cron-jobs-pour-curator-et-synthesizer]] — Config : Cron jobs pour curator et synthesizer