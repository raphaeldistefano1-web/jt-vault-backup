---
applies_to: culsec — app/crew/page.tsx (CreatePlayerSheet onCreate/handleCreate)
backlinks:
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
date: 2026-05-17
session_id: bff4c7c6-1b83-4749-a5d0-ac39d084f2de
status: pending
target: pms
type: improvement
urgency: low
---

# Cul Sec — fuite photo orpheline à la création de joueur

## Constat

Repéré par le code-reviewer pendant la revue Phase 2a (bug **pré-existant**, non
introduit par l'intégration Capacitor). Dans `app/crew/page.tsx`,
`CreatePlayerSheet` : `handleCreate` (≈ ligne 511) ne vérifie que `name.trim()`,
pas le cap `players.length >= 10`. Si une photo a été uploadée (`savePhoto` →
blobId en IndexedDB) puis `onCreate` part en early-return sur le cap 10 joueurs,
le blob reste orphelin en IDB. Second chemin : `onCreate` retrouve le joueur créé
par `players.find(name)` (lookup par nom) — collision de casse possible →
`photoBlobId` rattaché au mauvais joueur ou perdu.

## Pourquoi c'est utile / problématique

Fuite de stockage IndexedDB silencieuse (plafonnée par `pruneOldestIfFull` à 50,
donc pas critique) + risque de photo sur le mauvais joueur en cas d'homonyme.
Impact réel faible (cap 10 joueurs rarement atteint pile au tap, homonymes rares)
→ urgency low. Mais c'est une dette de robustesse exposée plus souvent par le
flux natif (caméra plus lente, fenêtre de tap concurrente plus large).

## How to apply

1. Dans `handleCreate` (CreatePlayerSheet, `app/crew/page.tsx`), avant `onCreate` :
   si `players.length >= 10` → `if (photoBlobId) await deletePhoto(photoBlobId)`
   puis `return` (ne pas laisser le blob orphelin).
2. Faire retourner l'`id` du joueur créé par `addPlayer` (changer la signature
   store) et l'utiliser pour `updatePlayer(id, { photoBlobId })` au lieu du
   lookup par nom — supprime le bug homonyme.
3. Vérifier : créer 10 joueurs + tenter un 11e avec photo → 0 blob orphelin
   (`keys()` idb-keyval) ; créer 2 joueurs même nom avec photos → photos
   correctes. ~30 min, dev (Claude).