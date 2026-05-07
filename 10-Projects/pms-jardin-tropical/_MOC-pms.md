---
id: 20260507-1100-moc-pms
type: moc
title: "MOC PMS Le Jardin Tropical"
project: pms-jardin-tropical
area: null
status: active
confidence: high
summary: "Hub d'entrée pour le PMS Next.js custom de l'hôtel Le Jardin Tropical (Bouillante)."
intent: reference
entities: [pms, nextjs, nextauth, jardin-tropical, hotel]
topic_cluster: pms-stack
related: ["[[PMS-Stack]]", "[[PMS-Dashboard-v2]]", "[[PMS-Calendar-v2]]", "[[PMS-Settings-Hub]]", "[[PMS-AI-Assistant]]"]
moc: "[[INDEX]]"
source: null
tier: hot
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07
embed_model_version: null
embed_hash: null
tags: [pms, moc, hotel]
ai_writable: false
---

# 💻 MOC — PMS Jardin Tropical

> Hub d'entrée pour le **PMS** (Property Management System) Next.js custom de l'hôtel.

## Vue d'ensemble

PMS développé sur-mesure pour Le Jardin Tropical (14 chambres, Bouillante, Guadeloupe). Stack Next.js 15 + Postgres + NextAuth v5 + Prisma. Déployé sur VPS via PM2.

## Notes du projet

### Architecture & stack
- [[PMS-Stack]] — Stack technique complète
- [[PMS-Dashboard-v2]] — Dashboard refondu (preview-then-apply)
- [[PMS-Calendar-v2]] — Calendrier réservations refondu
- [[PMS-Settings-Hub]] — Hub de paramètres consolidé
- [[PMS-AI-Assistant]] — Assistant IA + Mémoire IA fusionnés

### Brainstorming & roadmap
- [[Brainstorm-PMS-Ameliorations-2026-04-25]] — Quick wins UX/perf + investissements + anti-patterns

### Tests & validation
- [[Tests-PMS-Batterie-2026-04-25]] — 22 endpoints + 26 pages, perfs OK

### Intégrations connexes
- Plugin desktop Electron → cf. [[_MOC-desktop-app]]
- Plugin OpenClaw (IA) → cf. [[_MOC-openclaw]]
- Connexion jt-booking → cf. [[_MOC-site-wordpress]]

## Décisions transversales
- [[Decisions-Log]] (filtrer par `project: pms-jardin-tropical`)

## Bugs ouverts
- Voir `90-Meta/bases/bugs-pms.base` (à créer Phase 4)

## Lien externe
- Code : `/var/www/pms-jardin-tropical/`
- Sub-agents projet : `.claude/agents/` (pms-planner, pms-explorer, etc.)
