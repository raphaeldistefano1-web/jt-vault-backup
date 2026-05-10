---
ai_writable: false
backlinks:
- 2026-05-10-service-worker-offline-pour-pwa-cul-sec
- 2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router
- Brainstorm-PMS-Ameliorations-2026-04-25
- Desktop-App-Electron
- Dev-PMS-Area
- Test-jt-booking-PMS-2026-04-25
- Tests-PMS-Batterie-2026-04-25
- VPS-Hostinger
- Workflow-Deploy-PMS
- Workflow-File-Share-Uploads
- _Index
- _MOC-pms
- _VAULT-INDEX
created: 2026-04-25
description: Stack technique complète du PMS Le Jardin Tropical — Next.js 15 / Postgres
  / Prisma 6 / PM2 / Brevo
embed_hash: null
embed_model_version: null
entities:
- electron
- nextjs
- pm2
- pms
- postgres
- prisma
- traefik
id: 202604252030-pms-stack
intent: reference
last-accessed: 2026-04-25
project: pms-jardin-tropical
related:
- 2026-05-10-service-worker-offline-pour-pwa-cul-sec
- 2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router
- OpenClaw-VPS-Reference
- Workflow-File-Share-Uploads
- '[[Dev-PMS-Area]]'
- '[[Stack-Tech]]'
- '[[VPS-Hostinger]]'
- '[[Workflow-Deploy-PMS]]'
relevance: high
status: active
summary: Stack technique PMS — Next.js 15 + Postgres + Prisma 6 + PM2 + NextAuth v5
  + OpenClaw Gateway loopback.
tags:
- pms
- stack
- infra
tier: hot
topic_cluster: pms-stack
type: resource
updated: 2026-04-25
---

# 🏗️ PMS Stack

## Composants

- **Framework** : Next.js 15 (App Router)
- **Frontend** : React 19, Tailwind CSS, Server Components
- **DB** : PostgreSQL local (pas managé cloud)
- **ORM** : **Prisma 6** (PAS Prisma 7 — décision explicite, ne pas mettre à jour)
- **Process manager** : PM2 (`pms-jardin-tropical` instance)
- **Web server** : Nginx port 8080 (Traefik gère 80/443 niveau Hostinger)
- **Email transactionnel** : Brevo
- **Wrapper desktop** : [[Desktop-App-Electron]] v1.3.0
- **Plugin IA** : [[Plugin-OpenClaw]] (Gateway loopback :18789)

## Path serveur

- Code source : `/var/www/pms-jardin-tropical/`
- Build : `.next/`
- Public assets : `public/`
- DB Postgres : local au VPS

## URL

- **Provisoire** : https://pms-46-202-171-204.nip.io
- **Cible** : domaine sur `lejardintropical.fr` (à définir)

## Environnement variables

⚠️ Pas d'édition `.env` côté user. Toutes les clés API passent par [[Workflow-API-Integrations|/dashboard/settings/integrations]].

## Sub-agents projet

Le projet PMS a **6 sub-agents internes** dans `.claude/agents/` (cf. [[Sub-agents-internes-PMS]]). Quand on travaille dans `/var/www/pms-jardin-tropical/`, ces agents ont **priorité** sur les plugins officiels Claude Code.

## Liens

- [[Dev-PMS-Area]]
- [[Workflow-Deploy-PMS]]
- [[Workflow-Cross-Feature-Coherence]]

## Related

- [[OpenClaw-VPS-Reference]] — OpenClaw-VPS-Reference
- [[Workflow-File-Share-Uploads]] — Workflow-File-Share-Uploads
- [[2026-05-10-service-worker-offline-pour-pwa-cul-sec]] — Service Worker offline pour PWA CUL SEC
- [[2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router]] — Stack CUL SEC — PWA Next.js 14 App Router