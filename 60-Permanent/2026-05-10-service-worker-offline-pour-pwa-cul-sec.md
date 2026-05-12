---
ai_writable: false
area: null
backlinks:
- 2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a
- PMS-Stack
- Sub-agents-internes-PMS
- Workflow-Collaboration-IA
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- public/sw.js
- ServiceWorkerRegister.tsx
id: 20260510040512-service-worker-offline-pour-pwa-cul-sec
intent: config
last-accessed: '2026-05-10'
moc: null
project: null
related:
- Sub-agents-internes-PMS
- 2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a
- PMS-Stack
- _MOC-claude-system
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0114-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: Service Worker cache-first permet jouer offline ; registration dans ServiceWorkerRegister.tsx,
  manifest via next.config.js.
tags:
- permanent
- synthesized
- pwa
- offline
- service-worker
- cache
tier: warm
title: Service Worker offline pour PWA CUL SEC
topic_cluster: culsec-offline
type: permanent-note
updated: '2026-05-10'
---

**Fichier** : `/var/www/culsec/public/sw.js` (enregistré via component ServiceWorkerRegister.tsx).

**Statégie cache** : cache-first pour assets statiques (CSS, JS, images), network-first pour API. Permet jeu jouable sans connexion réseau.

**Manifest** : `/var/www/culsec/public/manifest.webmanifest` (PWA metadata : nom, icône, theme color, start_url=/play).

**Test** : DevTools → Application → Service Workers vérifier activation.

## Related

- [[Sub-agents-internes-PMS]] — Sub agents internes PMS
- [[2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a]] — Nouveaux skills doivent être auto-découverts par agents
- [[PMS-Stack]] — PMS Stack
- [[_MOC-claude-system]] — MOC Claude System — système IA personnel