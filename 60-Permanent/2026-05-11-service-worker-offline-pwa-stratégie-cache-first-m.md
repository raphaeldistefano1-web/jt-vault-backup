---
ai_writable: false
area: null
backlinks:
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
- Desktop-App-Electron
- Plugin-OpenClaw
- _VAULT-INDEX
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- service worker
- PWA
- manifest.webmanifest
- offline
id: 20260511211942-service-worker-offline-pwa-stratégie-cache-first-m
intent: pattern
last-accessed: '2026-05-11'
moc: null
project: null
related:
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
- Desktop-App-Electron
- OpenClaw-Etat
- Workflow-Deploy-PMS
- interface-design
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0820-session-19e3ce30.md
- 10-Projects/claude-system/2026-05-10-0827-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: Service Worker statique + manifest permettent jeu offline et installation
  PWA sur mobile/desktop.
tags:
- permanent
- synthesized
- pwa
- offline
- caching
tier: warm
title: 'Service Worker offline PWA: stratégie cache-first + manifest'
topic_cluster: project-culsec
type: permanent-note
updated: '2026-05-11'
---

**Registration**: `ServiceWorkerRegister.tsx` (composant client) enregistre `/public/sw.js` au montage. Silent fail si pas support.

**Caching**: SW intercepte requêtes GET statiques (JS, CSS, images) via stratégie cache-first (cache → réseau fallback). Précache assets au install event.

**Manifest**: `/public/manifest.webmanifest` déclare PWA (noms, icones, couleurs d'accent). Installable sur homescreen iOS/Android, desktop via Chrome/Edge.

**UX offline**: Après 1ère visite, joueurs peuvent lancer l'app sans réseau, importer joueurs, jouer. Aucune dépendance API réseau pour gameplay.

**Limitation**: Pas de persistance statistiques sans backend (localStorage ok pour session courante, pas sync cross-devices).

## Related

- [[Desktop-App-Electron]] — Desktop App Electron
- [[interface-design]] — interface design
- [[Workflow-Deploy-PMS]] — Workflow Deploy PMS
- [[OpenClaw-Etat]] — Plugin OpenClaw du PMS — État (avr 2026)
- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p]] — Stack CUL SEC: Next.js 14 App Router + Framer Motion PWA offline
- [[2026-05-11-architecture-jeux-extensible-registry-gameshell-is]] — Architecture jeux extensible: registry + GameShell + isolement composant
- [[2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq]] — État global Zustand + hook useGameSession pour logique jeu