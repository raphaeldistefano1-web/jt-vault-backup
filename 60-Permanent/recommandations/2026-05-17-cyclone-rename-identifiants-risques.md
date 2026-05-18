---
type: improvement
target: infra
status: pending
urgency: medium
date: 2026-05-17
session_id: c53c8ea5-58ef-411d-87e5-e45f88720300
applies_to: /Users/raphia/Documents/dev/culsec + VPS /var/www/culsec
---
# Renommage Cyclone — finir les identifiants risqués (différé)

## Constat

Le 2026-05-17 l'app a été renommée Cul Sec → **Cyclone** au niveau user-facing + métadonnées (package.json name, manifest PWA, titres, légal, about, share/referral/recap, AgeGate, commentaires marque). Décision Raphaël : faire le non-risqué maintenant, **laisser les identifiants risqués** mais les tracer ici. Ils restent en `culsec` et créent une dette de cohérence.

Identifiants NON renommés (encore `culsec` / `cul sec`) :

- **Clés de persistance localStorage / idb** (renommer = perte d'état utilisateur sans couche de migration) :
  - `lib/store.ts:246` → `name: "culsec-store"` (Zustand persist — CRITIQUE)
  - `lib/tasteProfile.ts:23` → `"culsec-taste-profile"`
  - `lib/promptHistory.ts:15-16` → `"culsec-prompt-history"`, `"culsec-prompt-ratings"`
  - `lib/photoStorage.ts:19` → `"culsec-photo:"`
  - `components/ui/SwipeFeedback.tsx:29` → `"culsec-feedback-session"`
- **Service worker cache** : `public/sw.js:5` → `CACHE_NAME = "culsec-v4-..."` (+ logs `[culsec sw]`, `[culsec]`)
- **Infra VPS** : dossier `/var/www/culsec`, `/var/lib/culsec/feedback.jsonl`, systemd `culsec.service` (port 3002), remote git `vps`, scripts `sync-to-vps.sh` / `sync-from-vps.sh` / `qa-server.sh`, `.env.production.example`
- **Store / app id** : `components/settings/RateAppRow.tsx:15` → `NEXT_PUBLIC_ANDROID_PACKAGE ?? "app.culsec"` (doit matcher la fiche Play Store — ne PAS changer à la légère)
- **Domaine** : `https://culsec.app` + emails `contact@culsec.app` / `support@culsec.app` (dépend d'un rachat de domaine `cyclone.*` — décision produit/marque)
- **Préfixe CSS** `--cs-*` (~50 occurrences globals.css + composants) : sémantique, pas user-facing, churn élevé pour zéro gain visible
- **scripts/snap.mjs + debug-*.mjs** : seed `localStorage.setItem("culsec-store", ...)` — doit suivre la clé store si elle migre

## Pourquoi c'est utile / problématique

- Risque réel : renommer `culsec-store` sans migration = **tous les utilisateurs perdent crew/réglages/premium** au prochain load (le store premium `redeemPromo` est persisté). Idem profil de goût (algo réapprend de zéro).
- Renommer dossier/service VPS sans fenêtre = **prod morte** (cf. ADR 0001 culsec : déployer depuis la mauvaise branche/chemin tue `culsec.service`).
- Le domaine/emails/app-id dépendent de décisions externes (rachat domaine, fiche store) — pas un simple refactor.
- Tant que non fait : incohérence `culsec` interne vs `Cyclone` public (acceptable court terme, dette à solder avant la soumission store finale / migration App Store).

## How to apply

1. **Couche de migration store** (Claude, ~1 j) : au boot, si `localStorage["cyclone-store"]` absent et `localStorage["culsec-store"]` présent → copier/transformer puis garder un alias lecture 1 version, idem taste-profile / prompt-history / photo / feedback-session. Tests : `npm run test:algo` + scénario "utilisateur existant garde son crew + premium". Bump `persist` version.
2. **SW cache** (Claude, 15 min) : nouveau `CACHE_NAME = "cyclone-v1-..."`, garder un cleanup de l'ancien `culsec-v*` dans l'event `activate`.
3. **Infra VPS** (Raphaël + Claude, ~2 h, fenêtre de coupure) : créer `/var/www/cyclone` + `/var/lib/cyclone`, nouveau `cyclone.service`, migrer remote git, adapter les 3 scripts sync, basculer, vérifier, supprimer l'ancien. Mettre à jour ADR culsec + mémoires `project_culsec.md` / `reference_*`.
4. **Domaine + app-id** (Raphaël, décision marque) : statuer rachat `cyclone.*` (ou garder culsec.app techniquement). Si nouveau domaine : MAJ emails légal/contact + `ANDROID_PACKAGE` aligné fiche store (impossible de changer un package Play déjà publié → nouveau listing).
5. **Préfixe CSS `--cs-*`** (optionnel, Codex délégable, ~30 min) : rename mécanique `--cs-` → `--cy-` sur globals.css + tous composants si on veut la cohérence totale. Faible priorité.

Temps total estimé : ~1,5 j Claude + 2 h Raphaël + 1 décision marque.

## Liens

- Memory : [[project_culsec]] (état rename), ADR `docs/adr/0001-appstore-export-strategy.md`
- Note connexe : [[2026-05-17-culsec-feedback-pipe-cassé-sans-test]]
