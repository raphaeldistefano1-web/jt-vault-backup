---
ai_writable: false
area: null
backlinks:
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- 2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
- _VAULT-INDEX
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- Next.js 14
- Tailwind CSS
- Framer Motion
- PWA
- service worker
id: 20260511211938-stack-cul-sec-nextjs-14-app-router-framer-motion-p
intent: decision
last-accessed: '2026-05-11'
moc: null
project: null
related:
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- 2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
- 2026-05-12-structure-et-composants-du-projet-culsec-nextjs-16
- AGENTS
- _MOC-claude-system
- _MOC-pms
- business-plan
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0820-session-19e3ce30.md
- 10-Projects/claude-system/2026-05-10-0827-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: 'CUL SEC architecture: Next.js 14 + Tailwind + Framer Motion pour jeu d''apéro
  offline-first.'
tags:
- permanent
- synthesized
- frontend
- game
- pwa
- next14
- offline
tier: hot
title: 'Stack CUL SEC: Next.js 14 App Router + Framer Motion PWA offline'
topic_cluster: project-culsec
type: permanent-note
updated: '2026-05-11'
---

**Stack choisi**: Next.js 14 (Turbopack, App Router) + Tailwind CSS + Framer Motion + Zustand + Lucide-react.

**Rationale**: PWA offline-capable via service worker (`/public/sw.js`). Framer Motion pour animations fluides (micro-interactions jeu d'apéro). Déployable sur VPS existant (`/var/www/culsec/`), cohérent avec infra PMS. Next 14 App Router + Turbopack pour perfs.

**Offline**: Service worker intercepte assets statiques (cache-first), permet gameplay sans réseau. Questions de jeux stockées localement.

**Deploy**: `next build && npm start` sur VPS, intègre pipeline existant (Nginx reverse proxy, monitoring via Tailscale).

## Related

- [[_MOC-pms]] — MOC PMS Le Jardin Tropical
- [[AGENTS]] — AGENTS
- [[_MOC-claude-system]] — MOC Claude System — système IA personnel
- [[2026-05-07-critères-filtrage-youtube-veille-ia]] — Critères filtrage YouTube veille-ia
- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m]] — Service Worker offline PWA: stratégie cache-first + manifest
- [[2026-05-11-architecture-jeux-extensible-registry-gameshell-is]] — Architecture jeux extensible: registry + GameShell + isolement composant
- [[2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16]] — Hydration mismatch (#418) avec Zustand + Next.js 16
- [[2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps]] — Accès VPS culsec via Tailscale + SSH (alias monvps/vps-pms)
- [[2026-05-12-structure-et-composants-du-projet-culsec-nextjs-16]] — Structure et composants du projet culsec (Next.js 16 + Zustand)
- [[business-plan]] — Cul Sec — Business Plan 2026