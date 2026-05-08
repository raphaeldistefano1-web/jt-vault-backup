---
ai_writable: false
created: 2026-04-25
description: Batterie complète tests fonctionnels PMS — 22 endpoints API + 26 pages
  testés, perfs excellentes, quelques incohérences mineures
embed_hash: null
embed_model_version: null
entities:
- api
- authentication
- debugging
- jwt
- nextauth
- pms
id: 202604252224-tests-pms-batterie-2026-04-25
intent: reference
last-accessed: 2026-04-25
project: pms-jardin-tropical
related:
- '[[PMS-Stack]]'
- '[[Dev-PMS-Area]]'
- '[[Brainstorm-PMS-Améliorations-2026-04-25]]'
relevance: high
status: completed
summary: Batterie tests PMS complets — 22 endpoints OK, 26 pages OK, TTFB < 120ms,
  7 findings mineurs documentés.
tags:
- pms
- tests
- audit
tier: hot
topic_cluster: pms-stack
type: project
updated: 2026-04-25
---

# 🧪 Tests batterie PMS — 2026-04-25

## Résumé

- **22/22 endpoints API** : tous OK fonctionnellement (les 2 "400" initiaux étaient des params manquants côté curl, pas des bugs)
- **26/26 pages user-facing** : toutes en HTTP 200/307
- **Perfs** : TTFB cached 33-115 ms partout, < 120 ms même non cached
- **CRUD réservation** : création + facture OK
- **Auth NextAuth v5 JWT** : login Credentials marche

## Auth

User test créé : `claude-test@lejardin-tropical.fr` (rôle ADMIN). Script `scripts/create-test-user.ts`. Cookie session valide pour 30j.

## Endpoints API testés

### Lecture (GET)
- `/api/dashboard/stats` ✅ 821b 49ms
- `/api/hotel-config` ✅ 558b 44ms
- `/api/nav/counts` ✅ 85b 54ms
- `/api/desktop/tray-summary` ✅ 374b 43ms
- `/api/calendar?start=&end=` ✅ (params requis : `start`, `end`)
- `/api/rooms/availability?start=&end=` ✅
- `/api/reservations` ✅ 3071b
- `/api/guests` + `/api/guests/search` ✅
- `/api/invoices` ✅ 867b
- `/api/notifications` ✅ 890b
- `/api/communications` ✅ vide (0 records)
- `/api/ai/memory`, `/api/ai/draft-rules`, `/api/ai/settings` ✅
- `/api/integrations` ✅ 7989b
- `/api/seasons`, `/api/partners`, `/api/supplements`, `/api/ota-channels` ✅
- `/api/reports/monthly` ✅ 1785b
- `/api/search?q=test` ✅ 747b

### Mutation
- `POST /api/reservations` ✅ — payload requis : `roomId`, `checkIn`, `checkOut`, `newGuest{firstName, lastName, email, phone}`. Auto-calcule prix avec saisons, status CONFIRMED, génère reference JT-YYYY-NNNNNN.
- `POST /api/reservations/[id]/invoice` ✅ HTTP 201
- `PATCH /api/reservations/[id]` ✅ (utilise PATCH, **pas PUT** !)

## Bugs / incohérences trouvés

### 1. Inconsistance noms paramètres API
- **Public API** (`/api/public/*`) : `from` / `to`
- **Internal API** (`/api/calendar`, `/api/rooms/availability`) : `start` / `end`

→ À uniformiser : choisir `from` / `to` partout (plus naturel) ou ajouter alias l'un vers l'autre.

### 2. PUT pas supporté sur reservations
`/api/reservations/[id]` n'expose que `GET` et `PATCH`. Pas de `PUT`. Pas de `DELETE`.

→ Est-ce intentionnel ? L'annulation passe via `PATCH { status: "CANCELLED" }` (soft delete), c'est cohérent REST. Mais à documenter dans le code (commentaire) sinon les nouveaux devs essaieront PUT/DELETE.

### 3. Cartographie agent imprécise
L'agent code-explorer disait `PUT, DELETE` sur `/api/reservations/[id]` — en réalité c'est `PATCH` only. Petit gap de cartographie, vault à corriger.

### 4. Données vides (config pas faite)
- `seasons` : 0 records → pas de tarification haute/basse saison configurée
- `partners` : 0 records → pas de tarifs B2B
- `ota-channels` : 0 records → pas de sync Booking/Airbnb
- `ai-memory` : 0 records → pas de docs IA (policies, FAQs)
- `ai-draft-rules` : 0 records → pas de templates IA
- `communications` : 0 records → pas d'historique encore (logique pour un PMS récent)

Pas des bugs, juste de la config user pas finie.

### 5. AI provider OPENAI configuré mais pas de clé en env
`HotelConfig.aiActiveProvider = OPENAI` mais pas de `OPENAI_API_KEY` en `.env`. AI Assistant tombera en erreur si invoqué. À configurer (cf. to-do).

### 6. Rooms : Bungalow 7 et 8 manquants
14 rooms en DB mais nommés Bungalow 1-6, 9-12 (pas 7, pas 8). Choix volontaire (skip 7/8 = superstition asiatique ?) ou bug du seed à valider.

### 7. /api/calendar et /api/rooms/availability params
- Erreur 400 si pas `start` & `end` → erreur message claire ✅
- Format `YYYY-MM-DD` attendu, `parseClientDate` côté serveur ✅

## Faux positifs (pas des bugs)

- Mots "error" sur dashboard (15) et calendar (14) → ce sont des chunks Next.js `app/(dashboard)/error.js` (error boundary), pas des messages d'erreur affichés.
- HTTP 308 sur certains endpoints quand l'ID est vide → redirect Next.js automatique (path normalization), comportement standard.

## Performance

| Métrique | Valeur | Cible |
|---|---|---|
| TTFB API moyen | 49 ms | < 100 ms ✅ |
| TTFB pages moyen | 78 ms | < 200 ms ✅ |
| Plus lente page | `/dashboard` 115 ms | < 200 ms ✅ |
| Plus lent endpoint | `/api/reports/monthly` 64 ms | < 100 ms ✅ |

Très bon état général.

## Liens

- [[PMS-Stack]]
- [[Dev-PMS-Area]]
- [[Brainstorm-PMS-Améliorations-2026-04-25]]