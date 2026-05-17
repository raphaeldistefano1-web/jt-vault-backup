---
applies_to: /Users/raphia/Documents/dev/culsec — lib/promo.ts, lib/store.ts
backlinks:
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
- OpenClaw-Etat
- business-plan
- check-1-critique-2026-05-14-1244
date: 2026-05-16
session_id: culsec-2026-05-16
status: pending
target: pms
type: improvement
urgency: medium
---

## Constat

L'écran premium culsec (`app/premium/page.tsx`) débloque le premium 100 % côté client : les codes promo (`CULSEC2026`, `APEROVIP`, `JARDIN`) sont en clair dans `lib/promo.ts` donc dans le bundle JS, et `isPremium` est un simple booléen persisté dans `localStorage` (clé `culsec-store`). N'importe qui via les DevTools peut lire les codes ou forcer `isPremium=true`. Choix assumé : le paiement réel est volontairement stubbé (décision Raphaël 2026-05-16, "écran premium + code promo, paiement stubbé").

## Pourquoi c'est utile / problématique

Tant qu'il n'y a pas de prestataire de paiement, aucun revenu n'est en jeu → risque nul aujourd'hui. Mais au moment de brancher Stripe/RevenueCat, laisser cette validation côté client = premium contournable en 10 s, perte de revenu direct. À traiter AVANT le premier euro encaissé, pas après.

## How to apply

1. Créer une route API signée (`app/api/promo/route.ts`) qui valide le code serveur et renvoie un token opaque (JWT court ou signature HMAC). ~1 h.
2. `redeemPromo` n'appelle plus `checkPromo` local mais l'API ; le store ne persiste que le token opaque, pas `isPremium` brut. ~45 min.
3. Au boot, vérifier la signature du token (clé serveur) avant d'accorder le premium. ~30 min.
4. Gating premium réel : les features (banques, prompts illimités) lisent un helper `usePremium()` qui valide le token, pas le booléen nu. ~1 h.
5. Codes promo → table serveur (usage unique / quota), plus de liste en dur. ~30 min.
Acteur : Claude, quand Raphaël choisit le prestataire de paiement (cf. mémoire `project_pivot_octobre_2026` / décision business à venir).