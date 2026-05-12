---
ai_writable: false
area: null
backlinks:
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-09-tmux-dashboard-3-windows-monitoring-quotas-live-cl
- Bug-Cross-Compile-Linux-MacOS
- PMS-Desktop-Pieges-Dev
- VPS-Access-Tailscale
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- Tailscale
- macOS
- CLI
id: 20260512040308-tailscale-cli-installation-sur-macos
intent: config
last-accessed: '2026-05-12'
moc: null
project: null
related:
- VPS-Access-Tailscale
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-09-tmux-dashboard-3-windows-monitoring-quotas-live-cl
- PMS-Desktop-Pieges-Dev
- Bug-Cross-Compile-Linux-MacOS
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-12-0048-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0102-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0040-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0043-session-13c136f3.md
source_session: 13c136f3-b295-415e-a3a5-7c632218fad1
status: active
summary: Installer Tailscale CLI sur Mac pour accès shell (optionnel).
tags:
- permanent
- synthesized
- config
- tailscale
- optional
tier: warm
title: Tailscale CLI installation sur macOS
topic_cluster: mac-setup
type: permanent-note
updated: '2026-05-12'
---

Pour accéder à `tailscale` en ligne de commande sur macOS (optionnel) :

1. Ouvrir l'application **Tailscale.app**
2. Aller à **Preferences**
3. Cliquer sur **« Install CLI…« »
4. Autoriser l'installation

**Résultat** : `tailscale` devient disponible au shell pour des commandes comme `tailscale up`, `tailscale status`, etc.

**Optionnel** : Cette étape n'est requise que si vous avez besoin de contrôler Tailscale en CLI (vs. via l'UI graphique).

## Related

- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[2026-05-08-syncthing-p2p-vault-sync-tailscale-only]] — Syncthing P2P vault sync Tailscale-only
- [[2026-05-09-tmux-dashboard-3-windows-monitoring-quotas-live-cl]] — Tmux dashboard 3-windows monitoring quotas live Claude/Codex
- [[PMS-Desktop-Pieges-Dev]] — Pièges du dev — Electron PMS Desktop
- [[Bug-Cross-Compile-Linux-MacOS]] — Bug Cross Compile Linux MacOS