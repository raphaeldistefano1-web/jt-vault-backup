---
ai_writable: false
backlinks:
- Brainstorm-PMS-Ameliorations-2026-04-25
- Desktop-App-Electron
- PMS-AI-Assistant
- PMS-Calendar-v2
- PMS-Dashboard-v2
- PMS-Settings-Hub
- PMS-Stack
- Sub-agents-internes-PMS
- Tests-PMS-Batterie-2026-04-25
- User-Raphael-Distefano
- VPS-Hostinger
- Workflow-API-Integrations
- Workflow-Cross-Feature-Coherence
- Workflow-Deploy-PMS
- Workflow-File-Share-Uploads
- Workflow-Preview-Then-Apply
created: 2026-04-25
description: Area de responsabilité — développement et exploitation du PMS custom
  Le Jardin Tropical
embed_hash: null
embed_model_version: null
entities:
- brevo
- nextjs
- pm2
- pms
- postgres
- prisma
- traefik
id: 202604252024-dev-pms-area
intent: reference
last-accessed: 2026-04-25
related:
- 2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router
- Workflow-File-Share-Uploads
- '[[Desktop-App-Electron]]'
- '[[PMS-Stack]]'
- '[[Plugin-OpenClaw]]'
- '[[Sub-agents-internes-PMS]]'
- '[[Workflow-Deploy-PMS]]'
- '[[Workflow-Preview-Then-Apply]]'
relevance: high
status: active
summary: PMS-Area|PMS = Property Management System custom Next.js mono-tenant pour
  piloter Le Jardin Tropical au quotidien. Pas d…
tags:
- pms
- dev
- nextjs
tier: hot
topic_cluster: area-hub
type: area
updated: 2026-04-25
---

# 💻 Dev PMS Area

## Vue d'ensemble

[[PMS-Area|PMS]] = Property Management System custom Next.js mono-tenant pour piloter Le Jardin Tropical au quotidien. Pas de produit SaaS, pas multi-tenant — outil interne de [[User-Raphael-Distefano|Raphaël]].

## Stack technique

Cf. [[PMS-Stack]] pour détails.

- Next.js 15 + React 19
- PostgreSQL local
- Prisma 6 (PAS Prisma 7)
- Tailwind CSS
- Nginx port 8080 + Traefik HTTPS
- PM2 process manager
- Brevo pour emails transactionnels

## État global (post-session 2026-04-25)

- ✅ [[PMS-Dashboard-v2]] appliqué prod
- ✅ [[PMS-Calendar-v2]] appliqué prod
- ✅ [[PMS-Settings-Hub]] consolidé
- ✅ [[PMS-AI-Assistant]] : fusion Mémoire IA + Assistant IA
- ✅ [[Plugin-OpenClaw]] Feature 1 OAuth Codex livrée sur `/dashboard/ai`
- ⏳ [[Plugin-OpenClaw]] Feature 2 (routines) reportée
- ✅ [[Desktop-App-Electron]] v1.3.0 déployée prod

## Workflows projet (à respecter)

- [[Workflow-Preview-Then-Apply]] — toute refonte UI passe par route `_v2` prévisualisable
- [[Workflow-Deploy-PMS]] — migrate (si schema) → build → pm2 restart
- [[Workflow-API-Integrations]] — toute clé API externe via `/dashboard/settings/integrations`
- [[Workflow-Cross-Feature-Coherence]] — toute feature exposée à TOUS les points d'entrée pertinents (calendar SlidePanel, frontdesk, détail résa…)

## Sub-agents internes

[[Sub-agents-internes-PMS]] — 6 agents dans `.claude/agents/` (priorité sur les plugins officiels Claude Code quand on travaille dans `/var/www/pms-jardin-tropical`).

## Priorités à venir

- [ ] Connecter PMS ↔ [[Plugin-jt-booking|jt-booking]] (email J+1 post-checkout via Brevo)
- [ ] Synchro tarifs jt-booking ↔ PMS (éviter divergence)
- [ ] [[Plugin-OpenClaw]] Feature 2 routines

## Path serveur

- **Code source** : `/var/www/pms-jardin-tropical/`
- **URL provisoire** : https://pms-46-202-171-204.nip.io

## Related

- [[Workflow-File-Share-Uploads]] — Workflow-File-Share-Uploads
- [[2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router]] — Stack CUL SEC — PWA Next.js 14 App Router