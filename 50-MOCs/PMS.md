---
type: moc
status: active
tags: [pms, dev, nextjs, moc]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Map of Content — PMS (Property Management System) custom Next.js du Jardin Tropical"
ai_writable: false
id: 202604252021-pms
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "PMS Property Management System custom dev en Next.js, géré par Raphaël owner-operator. Pas de produit SaaS — outil inter…"
entities: [nextjs, pms, postgres, prisma]
topic_cluster: vault-navigation
intent: reference
tier: warm
---

# 🛏️ MOC PMS Le Jardin Tropical

## Identité

PMS (Property Management System) custom dev en Next.js, géré par Raphaël (owner-operator). Pas de produit SaaS — outil interne mono-tenant pour piloter l'hôtel au quotidien.

## URL et accès

- **Public** : https://pms-46-202-171-204.nip.io/
- **Path serveur** : `/var/www/pms-jardin-tropical/`

## Stack

- **Next.js 15** + React 19
- **PostgreSQL** local (pas Postgres cloud)
- **Prisma 6** (pas Prisma 7)
- **Tailwind CSS**
- **Nginx** sur port 8080 (Traefik Docker Hostinger gère 80/443)
- **PM2** pour la gestion process en prod
- **Brevo** pour l'envoi d'emails transactionnels

## Composants clés

- [[Dashboard-v2]] — dashboard principal v2 appliqué prod
- [[Calendar-v2]] — calendar v2 appliqué prod
- [[Settings-Hub]] — paramètres consolidés en hub central
- [[AI-Assistant]] — fusion Mémoire IA + Assistant IA via plugin OpenClaw
- [[Desktop-App]] — wrapper Electron v1.3.0 (notifs natives, badge dock, tray menu bar, deep links pms://, mode offline lecture, auto-update prompt)
- [[Plugin-OpenClaw]] — plugin IA, Feature 1 OAuth Codex livrée sur /dashboard/ai

## Sub-agents internes du projet

Le projet a 6 sub-agents spécialisés dans `.claude/agents/` (priorité sur les plugins officiels quand on travaille dans `/var/www/pms-jardin-tropical`).

## Workflows

- [[Workflow-Preview-Then-Apply]] — toute refonte UI passe par route `_v2` prévisualisable
- [[Workflow-Deploy]] — migrate (si schema) → build → pm2 restart
- [[Workflow-API-Integrations]] — toute clé API externe via /dashboard/settings/integrations (Stripe, Brevo, OVH, Claude…)
- [[Workflow-Cross-Feature-Coherence]] — toute feature exposée à TOUS les points d'entrée pertinents

## Reste à faire

- Plugin OpenClaw Feature 2 (routines) — reportée
- Connecter PMS ↔ jt-booking (email J+1 post-checkout via Brevo)
- Synchro tarifs jt-booking ↔ PMS (éviter divergence)
