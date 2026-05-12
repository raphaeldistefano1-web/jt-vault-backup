---
ai_writable: false
area: null
backlinks:
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- game registry
- GameShell
- 15 jeux
- PromptCard
id: 20260511211941-architecture-jeux-extensible-registry-gameshell-is
intent: pattern
last-accessed: '2026-05-11'
moc: null
project: null
related:
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-11-layout-nouvelle-saison-3-cartes-alignées-horizonta
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
- 2026-05-12-structure-et-composants-du-projet-culsec-nextjs-16
- Workflow-Cross-Feature-Coherence
- _MOC-claude-system
- interface-design
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0820-session-19e3ce30.md
- 10-Projects/claude-system/2026-05-10-0827-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: 15 jeux implémentés comme composants React isolés, orchestrés par GameShell
  et registry centralisée.
tags:
- permanent
- synthesized
- architecture
- extensibility
- component-design
tier: warm
title: 'Architecture jeux extensible: registry + GameShell + isolement composant'
topic_cluster: project-culsec
type: permanent-note
updated: '2026-05-11'
---

**Structure**:
- `/components/games/registry.ts` : registre des 15 jeux (ActionVérité, BizzBuzz, Categories, HeadsUp, HigherLower, JeNaiJamais, Medusa, MostLikely, Paranoia, Picolo, Roulette, SeptSecondes, ShesATen, TuPreferes, TwoTruths)
- Chaque jeu = composant React avec props état (joueurs, tour courant, prompt)
- `GameShell` gère transitions, timers, changement joueur, validation tour
- `PlayerChips` + `PromptCard` composants réutilisables pour UI commune
- `/data/questions/` : données jeu par fichier (picolo.ts, categories.ts, etc.)

**Extensibilité**: Ajouter jeu = créer `/components/games/NouveauJeu.tsx` + enregistrer dans registry. Pas de mutation cœur.

**Typing**: Interfaces jeu + question définies en `/types/index.ts`, typage fort end-to-end.

## Related

- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[interface-design]] — interface design
- [[2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend]] — Pipeline veille-ia-youtube : ingest→analyze→render→send
- [[Workflow-Cross-Feature-Coherence]] — Workflow Cross Feature Coherence
- [[_MOC-claude-system]] — MOC Claude System — système IA personnel
- [[2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m]] — Service Worker offline PWA: stratégie cache-first + manifest
- [[2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p]] — Stack CUL SEC: Next.js 14 App Router + Framer Motion PWA offline
- [[2026-05-11-layout-nouvelle-saison-3-cartes-alignées-horizonta]] — Layout 'nouvelle saison' — 3 cartes alignées horizontalement
- [[2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq]] — État global Zustand + hook useGameSession pour logique jeu
- [[2026-05-12-structure-et-composants-du-projet-culsec-nextjs-16]] — Structure et composants du projet culsec (Next.js 16 + Zustand)