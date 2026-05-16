---
ai_writable: false
area: null
backlinks:
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- OpenClaw-VPS-Reference
- VPS-Access-Tailscale
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- Tailscale
- SSH
- VPS
- culsec repo
id: 20260512040715-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-15-sync-to-vps-tuer-orphelin-port
- OpenClaw-VPS-Reference
- PMS-Desktop-Reference
- VPS-Hostinger
- session
schema_version: 1
source_notes:
- 10-Projects/pms-jardin-tropical/2026-05-12-0207-session-0d81ecb1.md
source_session: 0d81ecb1-2006-4cb3-ad96-6d7224a30db7
status: active
summary: 'Connecter au VPS hébergeant culsec : `ssh monvps` ou `ssh vps-pms`, puis
  `cd /var/www/culsec` pour accéder au repo live.'
tags:
- permanent
- synthesized
- remote-access
- vpn
- workflow
tier: warm
title: Accès VPS culsec via Tailscale + SSH (alias monvps/vps-pms)
topic_cluster: vps-devops
type: permanent-note
updated: '2026-05-12'
---

**Workflow établi** :

```bash
# Option 1 (alias Mac/Linux)
ssh monvps
cd /var/www/culsec

# Option 2 (alias alias vps-pms via Tailscale)
ssh vps-pms "cd /var/www/culsec && git status"
```

**Détails** :
- SSH configuré dans `~/.ssh/config` avec alias
- Connexion via Tailscale (réseau P2P privé, pas port 22 public)
- Repo live = `/var/www/culsec/` sur VPS Hostinger (2 vCPU EPYC, 8 GB RAM)
- Git repo standard, logs via `git log --oneline`, status via `git status --short`
- CLAUDE.md et AGENTS.md présents dans le repo

**Anti-pattern** : Ne pas laisser `next dev` orphelin sur VPS longtemps (throttle CPU). Préférer `next build && next start` pour sessions dev longues.

## Related

- [[2026-05-08-syncthing-p2p-vault-sync-tailscale-only]] — Syncthing P2P vault sync Tailscale-only
- [[PMS-Desktop-Reference]] — PMS Desktop — Paths, endpoints, commandes
- [[2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p]] — Stack CUL SEC: Next.js 14 App Router + Framer Motion PWA offline
- [[OpenClaw-VPS-Reference]] — OpenClaw sur le VPS — Paths, ports, config
- [[VPS-Hostinger]] — VPS Hostinger
- [[session]] — session
- [[2026-05-15-sync-to-vps-tuer-orphelin-port]] — 2026-05-15-sync-to-vps-tuer-orphelin-port