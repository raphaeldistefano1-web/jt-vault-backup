---
ai_writable: false
area: null
backlinks:
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-12-auto-arrêt-à-80-cpu-notification-email
- 2026-05-12-chemins-daccumulation-disque-connus-docker-node-mo
- 2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar
- 2026-05-12-migration-architecture-claude-vps-mac-mini
- 2026-05-12-procédure-daudit-disque-vps-diagnostic-standard
- 2026-05-12-structure-et-composants-du-projet-culsec-nextjs-16
- PMS-Desktop-Reference
- VPS-Access-Tailscale
- VPS-Hostinger
- Vault-Setup
- _VAULT-INDEX
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- /var/www/culsec
- VPS
- Nginx
- next build
id: 20260511211947-path-varwwwculsec-homogénéité-infra-vps-avec-pms
intent: config
last-accessed: '2026-05-11'
moc: null
project: null
related:
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps
- 2026-05-12-auto-arrêt-à-80-cpu-notification-email
- 2026-05-12-chemins-daccumulation-disque-connus-docker-node-mo
- 2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar
- 2026-05-12-migration-architecture-claude-vps-mac-mini
- 2026-05-12-procédure-daudit-disque-vps-diagnostic-standard
- 2026-05-12-structure-et-composants-du-projet-culsec-nextjs-16
- 2026-05-15-sync-to-vps-tuer-orphelin-port
- PMS-Desktop-Reference
- Stack-Tech
- VPS-Access-Tailscale
- VPS-Hostinger
- Vault-Setup
- business-plan
- check-1-critique-2026-05-14-1244
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0820-session-19e3ce30.md
- 10-Projects/claude-system/2026-05-10-0827-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: CUL SEC hébergé au même emplacement que PMS sur VPS, même pipeline build/start.
tags:
- permanent
- synthesized
- infrastructure
- deployment
tier: warm
title: Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
topic_cluster: project-culsec
type: permanent-note
updated: '2026-05-11'
---

**Path**: `/var/www/culsec/` (cohérent avec `/var/www/pms-jardin-tropical/`, à côté)

**Build/Deploy**: `npm run build` suivi `npm start` (identique PMS). Réutilise systemd service ou PM2 déjà configurés.

**Nginx**: Reverse proxy sur port 3001 (ou dédié) → domaine `culsec-46-202.nip.io` ou sous-domaine.

**Git**: Repo git initialisé, prêt pour versionning + webhooks de deploy.

**Avantage**: Zero infra neuve. Monitoring/alertes existent déjà (Tailscale access, swap guardrails, CPU throttle awareness). Scaling horizontal possible (copier `/var/www/culsec/` si besoin). Backup via snapshots VPS existants.

## Related

- [[Vault-Setup]] — Vault Setup
- [[PMS-Desktop-Reference]] — PMS Desktop — Paths, endpoints, commandes
- [[VPS-Hostinger]] — VPS Hostinger
- [[Stack-Tech]] — Stack Tech
- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p]] — Stack CUL SEC: Next.js 14 App Router + Framer Motion PWA offline
- [[2026-05-12-auto-arrêt-à-80-cpu-notification-email]] — Auto-arrêt à 80% CPU + notification email
- [[2026-05-12-migration-architecture-claude-vps-mac-mini]] — Migration architecture Claude : VPS → Mac mini
- [[2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar]] — CPU throttling VPS Hostinger — monitoring via sar
- [[2026-05-12-chemins-daccumulation-disque-connus-docker-node-mo]] — Chemins d'accumulation disque connus: Docker, node_modules, logs
- [[2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps]] — Accès VPS culsec via Tailscale + SSH (alias monvps/vps-pms)
- [[2026-05-12-structure-et-composants-du-projet-culsec-nextjs-16]] — Structure et composants du projet culsec (Next.js 16 + Zustand)
- [[2026-05-12-procédure-daudit-disque-vps-diagnostic-standard]] — Procédure d'audit disque VPS — diagnostic standard
- [[business-plan]] — Cul Sec — Business Plan 2026
- [[check-1-critique-2026-05-14-1244]] — check-1-critique-2026-05-14-1244
- [[2026-05-15-sync-to-vps-tuer-orphelin-port]] — 2026-05-15-sync-to-vps-tuer-orphelin-port