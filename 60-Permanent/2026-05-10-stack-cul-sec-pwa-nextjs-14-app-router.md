---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- Dev-PMS-Area
- PMS
- PMS-Stack
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- Next.js 14
- Zustand
- Framer Motion
- PWA
- Service Worker
id: 20260510040509-stack-cul-sec-pwa-nextjs-14-app-router
intent: decision
last-accessed: '2026-05-10'
moc: null
project: null
related:
- PMS-Stack
- PMS
- Brainstorm-PMS-Ameliorations-2026-04-25
- AGENTS
- 2026-05-08-vault-para-multi-projets-chemin-canonique
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0114-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: PWA Next.js 14 App Router + Zustand + Framer Motion pour jeu party multiplayer
  offline-capable.
tags:
- permanent
- synthesized
- pwa
- next.js
- state-management
- offline
- animation
tier: warm
title: Stack CUL SEC — PWA Next.js 14 App Router
topic_cluster: culsec-infra
type: permanent-note
updated: '2026-05-10'
---

**Stack choisi** : Next.js 14 App Router (Turbopack), Zustand pour état global (léger vs Redux), Framer Motion pour animations, Service Worker pour offline, manifest.webmanifest pour PWA.

**Rationale** : déployable sur VPS existant (/var/www/culsec/) à côté du PMS. Offline capability essentiel pour jeu party (stable réseau wifi irrégulier). Zustand élimine boilerplate Redux. Framer Motion pour micro-interactions polies (entrées jeux, transitions).

**Bénéfices** : installable comme app mobile, fonctionnel sans réseau, déploiement trivial sur infra existante.

## Related

- [[PMS-Stack]] — PMS Stack
- [[PMS]] — PMS
- [[Brainstorm-PMS-Ameliorations-2026-04-25]] — Brainstorm PMS Ameliorations 2026 04 25
- [[AGENTS]] — AGENTS
- [[2026-05-08-vault-para-multi-projets-chemin-canonique]] — Vault PARA multi-projets chemin canonique