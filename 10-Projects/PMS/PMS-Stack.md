---
type: resource
status: active
tags: [pms, stack, infra]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Stack technique complète du PMS Le Jardin Tropical — Next.js 15 / Postgres / Prisma 6 / PM2 / Brevo"
ai_writable: false
related:
  - "[[Dev-PMS-Area]]"
  - "[[Stack-Tech]]"
  - "[[Workflow-Deploy-PMS]]"
  - "[[VPS-Hostinger]]"
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
