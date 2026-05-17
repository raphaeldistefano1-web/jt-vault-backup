---
ai_writable: false
area: null
backlinks:
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- 2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- React
- Next.js 16
- Zustand
- StoreHydrator
- SSR
id: 20260512040708-hydration-mismatch-418-avec-zustand-nextjs-16
intent: gotcha
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- 2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
- 2026-05-15-qa-hygiene-serveur-next-local
- 2026-05-16-culsec-premium-validation-serveur
schema_version: 1
source_notes:
- 10-Projects/pms-jardin-tropical/2026-05-12-0207-session-0d81ecb1.md
source_session: 0d81ecb1-2006-4cb3-ad96-6d7224a30db7
status: active
summary: Synchronisation rendu serveur/client échoue quand le store côté client n'est
  pas hydraté avant le rendu des composants dépendants.
tags:
- permanent
- synthesized
- hydration-mismatch
- server-client-sync
- store-initialization
tier: warm
title: Hydration mismatch (#418) avec Zustand + Next.js 16
topic_cluster: react-hydration
type: permanent-note
updated: '2026-05-12'
---

Erreur React #418 survient typiquement sur pages utilisant Zustand (ou store client-side) si le state est lu côté serveur pendant le rendu, puis remplacé côté client après hydration.

**Symptômes** : 3 pages du projet culsec affectées, tokens/state mal synchronisés entre serveur et client.

**Solution** : Wrapper l'app avec `StoreHydrator.tsx` qui initialise le store avant le rendu des composants clients. Pattern : créer un composant "hydrator" qui expose le state **après** hydration complète, jamais durant le rendu initial.

**Prévention** : Toujours séparer les composants server (layout, pages) des composants client (consommatrices du store). Utiliser `'use client'` strictement sur les composants qui lisent Zustand. Valider que le state initial côté serveur == state initial côté client (sinon mismatch garanti).

## Related

- [[2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router]] — Stack CUL SEC — PWA Next.js 14 App Router
- [[2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq]] — État global Zustand + hook useGameSession pour logique jeu
- [[2026-05-09-anti-pattern-redonder-info-du-contexte-injecté]] — Anti-pattern : redonder info du contexte injecté
- [[2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p]] — Stack CUL SEC: Next.js 14 App Router + Framer Motion PWA offline
- [[2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo]] — Trier items capturés : hot (immédiat) vs warm/cold (mémoire)
- [[2026-05-15-qa-hygiene-serveur-next-local]] — 2026-05-15-qa-hygiene-serveur-next-local
- [[2026-05-16-culsec-premium-validation-serveur]] — 2026-05-16-culsec-premium-validation-serveur