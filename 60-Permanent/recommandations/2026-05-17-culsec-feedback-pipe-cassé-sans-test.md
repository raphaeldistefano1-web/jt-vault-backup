---
applies_to: /Users/raphia/Documents/dev/culsec — app/api/feedback/route.ts + SwipeFeedback
backlinks:
- 2026-05-17-cyclone-rename-identifiants-risques
date: 2026-05-17
session_id: b4dd63b4-0812-409a-958e-414720444c19
status: pending
target: pms
type: improvement
urgency: medium
---

# Constat

Le système de feedback béta de culsec (SwipeFeedback → POST /api/feedback) rejetait **100 % des notes en HTTP 400 depuis sa création**, tous jeux confondus : la route validait `rating ∈ {good,mid,bad}` alors que le client n'a jamais envoyé que `{like,dislike,neutral}` (type `Rating` canonique dans `lib/tasteProfile.ts`). Erreur invisible car `fetch(...).catch(()=>{})` best-effort côté client → aucune alerte, aucune donnée collectée pendant des semaines. Découvert par hasard en câblant le feedback sur Cyclone (2026-05-17), corrigé dans le même commit (`524e546`).

# Pourquoi c'est problématique

Une feature « livrée » et crue fonctionnelle ne produisait rien : zéro donnée béta pour ajuster le style des questions, objectif explicite de Raphaël. Le pattern best-effort silencieux + l'absence de tout test sur l'endpoint = n'importe quelle régression future de payload repassera inaperçue (le client ne criera jamais). Risque identique sur tout endpoint « fire-and-forget » du projet.

# How to apply

1. Ajouter un test d'intégration minimal sur `/api/feedback` dans le harnais existant (`scripts/test-algo.mjs` ou nouveau `scripts/test-feedback.mjs`) : POST like/dislike/neutral → 200 + ligne JSONL écrite ; POST rating inconnu → 400. ~30 min.
2. Lui faire importer le type `Rating` réel (`lib/tasteProfile.ts`) et asserter que `RATINGS` (route) === union du type → empêche tout futur drift client/serveur. ~15 min.
3. Brancher ce test dans la check-list pré-`sync-to-vps` (cf. commentaire d'en-tête du script). ~5 min.
4. Audit transverse : lister les autres `fetch().catch(()=>{})` silencieux du projet (grep), décider lesquels méritent un log dev (`if (process.env.NODE_ENV!=='production') console.warn`) pour ne pas masquer les 4xx en dev. ~20 min.

Acteur : Claude en session dédiée. Gain : une feature de collecte qui collecte vraiment + garde-fou anti-drift permanent.