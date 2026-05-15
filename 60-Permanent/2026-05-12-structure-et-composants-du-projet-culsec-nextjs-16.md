---
ai_writable: false
area: null
backlinks:
- 2026-05-10-registry-pattern-centralisateur-jeux-modulaires
- 2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- culsec
- Next.js 16
- Zustand
- registry pattern
id: 20260512040712-structure-et-composants-du-projet-culsec-nextjs-16
intent: config
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-10-questionsprompts-externalisées-par-jeu
- 2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
- business-plan
schema_version: 1
source_notes:
- 10-Projects/pms-jardin-tropical/2026-05-12-0207-session-0d81ecb1.md
source_session: 0d81ecb1-2006-4cb3-ad96-6d7224a30db7
status: active
summary: Culsec = 15 jeux d'apéro Next.js 16, organisés via registry.ts, data/games/index.ts,
  et structure components/games/.
tags:
- permanent
- synthesized
- project-structure
- component-registry
- game-catalog
tier: warm
title: Structure et composants du projet culsec (Next.js 16 + Zustand)
topic_cluster: culsec-project
type: permanent-note
updated: '2026-05-12'
---

**Arborescence clé** :
- `app/page.tsx` : accueil avec liste jeux
- `app/catalog/page.tsx` : catalogue détaillé
- `app/layout.tsx` : layout global
- `components/games/` : composants individuels (Picolo, HigherLower, JeNaiJamais, MostLikely, ShesATen, TuPreferes, TwoTruths, etc.)
- `components/games/registry.ts` : index centralisé de tous les jeux (importés pour le catalog)
- `data/games/index.ts` : métadonnées jeux (titre, desc, regles, images)
- `components/ui/` : composants réutilisables (Button, LinkButton, RevealPrompt)
- `lib/store.ts` : Zustand store (global game state)
- `components/StoreHydrator.tsx` : wrapper hydration (créé pour fix #418)

**Patterns** :
- Chaque jeu = composant React isolé + données centralisées
- Registry pattern pour éviter imports répétés
- Store Zustand pour state cross-game (score, joueurs, etc.)

## Related

- [[2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router]] — Stack CUL SEC — PWA Next.js 14 App Router
- [[2026-05-10-questionsprompts-externalisées-par-jeu]] — Questions/prompts externalisées par jeu
- [[2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq]] — État global Zustand + hook useGameSession pour logique jeu
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[business-plan]] — Cul Sec — Business Plan 2026