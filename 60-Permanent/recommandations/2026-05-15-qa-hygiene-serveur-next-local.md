---
applies_to: vérification QA navigateur de tout projet Next.js local
backlinks:
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- 2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
- 2026-05-12-refonte-visuelle-non-fialisée-vs-moc-du-projet-cul
- 2026-05-12-vérification-pre-cutover-systématique-perf-et-diff
date: 2026-05-15
session_id: culsec-qa-campagne
status: pending
target: workflow
type: improvement
urgency: medium
---

## Constat

Pendant la campagne QA culsec, un "défaut C1" (écran figé "Préparation…" + `Uncaught (in promise)` + 404 ×4) a été conclu à tort comme un bug applicatif. Cause réelle : **plusieurs `next start`/`next-server` empilés sur la même longue session** (pkill par motif imprécis n'avait pas tout tué) + rebuilds successifs sans purge de `.next` → le serveur servait un HTML désynchronisé des hash de chunks → chunks JS/CSS en 404 → React n'hydratait pas → page figée sur le frame SSR. Après teardown complet (kill tous next + `rm -rf .next` + 1 seul build + 1 serveur + contexte navigateur neuf), C1 s'est révélé **déjà correct**. ~5 tours de debug gaspillés, et un agent correcteur a failli être lancé sur un faux bug.

## Pourquoi c'est utile

Sans hygiène d'environnement, la vérification QA produit des faux positifs coûteux (debug à vide, corrections inutiles voire régressions introduites en "réparant" du code sain). Sur une session longue avec multiples rebuilds, le risque est systématique.

## How to apply

Avant toute campagne de vérification QA navigateur sur un Next local, et entre chaque rebuild :
1. Teardown strict : `pkill -f "next-server"; pkill -f "next start"; pkill -f "next dev"` puis vérifier `ps -eo pid,command | grep next` → 0 process.
2. `rm -rf .next` puis **un seul** `npm run build`, **un seul** `npx next start -p <port>`.
3. Vérifier le bon process : `lsof -nP -iTCP:<port> -sTCP:LISTEN` (un seul PID, uptime cohérent avec le restart).
4. Côté navigateur : `isolatedContext` NEUF + premier reload en `ignoreCache:true`.
5. Réflexe diagnostic : si page figée/JS inerte → **d'abord** `list_network_requests` (chercher des `_next/static/chunks/*` en 404) AVANT de soupçonner le code. Chunks 404 mais présents sur disque = serveur/HTML désynchro, pas un bug app.
6. Idéalement : script `scripts/qa-server.sh` qui encapsule teardown+build+start atomique pour ne plus jamais empiler.
Temps : ~5 min de mise en place du script, gain = élimination d'une classe entière de faux positifs. Qui : Claude (créer le script), à utiliser systématiquement ensuite.