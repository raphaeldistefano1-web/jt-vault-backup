---
ai_writable: false
area: null
backlinks:
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
- 2026-05-12-structure-et-composants-du-projet-culsec-nextjs-16
- PMS-Settings-Hub
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- Zustand
- store.ts
- useGameSession
- PlayerChips
id: 20260511211945-état-global-zustand-hook-usegamesession-pour-logiq
intent: decision
last-accessed: '2026-05-11'
moc: null
project: null
related:
- 2026-05-08-frontmatter-enrichi-extrait-insights-durables
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
- PMS-Settings-Hub
- _MOC-claude-system
- interface-design
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0820-session-19e3ce30.md
- 10-Projects/claude-system/2026-05-10-0827-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: Zustand store + useGameSession hook encapsulent logique joueur et transitions
  tour-par-tour.
tags:
- permanent
- synthesized
- state-management
- game-logic
- hooks
tier: warm
title: État global Zustand + hook useGameSession pour logique jeu
topic_cluster: project-culsec
type: permanent-note
updated: '2026-05-11'
---

**Zustand store** (`lib/store.ts`): État centralisé du jeu
- `players[]` : liste joueurs (ID, nom, état actif, score)
- `currentPlayerIdx` : index joueur courant
- `gameState` : jeu en cours (questions restantes, réponses validées)
- Actions: `addPlayer()`, `removePlayer()`, `nextTurn()`, `updateScore()`

**useGameSession hook** (`lib/useGameSession.ts`): Encapsule logique applicative
- Récupère Zustand state
- Gère transitions tour (validation input, timer, détection fin jeu)
- Expose interface simple : `playTurn()`, `endGame()`, `getRules(gameId)`

**Avantage**: Séparation concern (store = data, hook = logique métier). Testable isolément (mock Zustand). Réutilisable sur routes/games différentes.

**Accès état**: Composants consumers utilisent hook directement, pas prop drilling.

## Related

- [[_MOC-claude-system]] — MOC Claude System — système IA personnel
- [[PMS-Settings-Hub]] — PMS Settings Hub
- [[interface-design]] — interface design
- [[2026-05-08-frontmatter-enrichi-extrait-insights-durables]] — Frontmatter enrichi extrait insights durables
- [[2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m]] — Service Worker offline PWA: stratégie cache-first + manifest
- [[2026-05-11-architecture-jeux-extensible-registry-gameshell-is]] — Architecture jeux extensible: registry + GameShell + isolement composant
- [[2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16]] — Hydration mismatch (#418) avec Zustand + Next.js 16