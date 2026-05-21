---
type: improvement
target: cyclone
status: pending
urgency: high
date: 2026-05-20
session_id: remote-control-2026-05-20
applies_to: cyclone-ios (App Store track)
---

# Cyclone — bundle ID `com.cyclone.app` contesté par Apple

## Constat

Pendant le setup signature device sur `~/Documents/dev/cyclone-ios` (Personal
Team `FZ99ZN8WN5` / `TMKT8V5Q6L`, Apple ID `rafou97125@gmail.com`), Apple a
refusé le bundle ID `com.cyclone.app` :

```
Failed Registering Bundle Identifier:
The app identifier "com.cyclone.app" cannot be registered to your development
team because it is not available.
```

Cause possible : soit un autre développeur a déjà réservé ce bundle ID auprès
d'Apple, soit Apple bloque l'usage du mot "cyclone" en suffixe court pour
empêcher squatting/confusion de marque.

Workaround appliqué (build dev uniquement) : bascule sur
`com.cyclone.app.dev`, build signé OK avec profile auto.

La mémoire `project_culsec.md` (pivot 2026-05-19) avait fixé `com.cyclone.app`
comme bundle ID cible App Store : **caduc**, à arbitrer.

## Pourquoi c'est utile / problématique

Le bundle ID est **irréversible post-publish App Store**. Si on lance la
soumission en pensant pouvoir récupérer `com.cyclone.app` plus tard et qu'on
n'y arrive pas, on est coincé sur un bundle ID secondaire pour la vie de
l'app. Mieux vaut trancher maintenant qu'à 24h de la submission.

Il existe aussi un risque que le **nom "Cyclone" lui-même** soit contesté côté
App Store (recherche INPI/WIPO non faite). Si Apple bloque déjà le bundle ID,
c'est un signal faible que le nom de marque est peut-être déjà occupé.

## How to apply

1. **Vérifier dispo du nom "Cyclone"** côté App Store en parallèle des
   démarches INPI/WIPO (déjà listé dans `project_culsec.md` chemin critique
   Jour 1). Outil rapide : `appfigures.com/tools/app-name-availability` ou
   recherche manuelle App Store FR + US.
2. **Quand la licence Apple Developer payante est active** : retenter
   l'enregistrement de `com.cyclone.app` via App Store Connect → Identifiers →
   App IDs. Si Apple accepte → on rebascule le bundle ID, on rebuild.
3. **Si Apple refuse même avec licence payante** : choisir un bundle ID
   définitif unique. Candidats (à valider Raphaël) :
   - `app.cyclone.party` (suffixe lié au use case soirée)
   - `fr.cyclone.app` (TLD pays)
   - `com.raphdistefano.cyclone` (namespace personnel)
   - `com.cyclone.app.ios` (peu propre, à éviter)
4. **Mettre à jour `cyclone-ios/project.yml`** avec le bundle ID retenu,
   xcodegen, rebuild. Garder une dernière itération dev avant de geler.
5. Documenter la décision finale dans un ADR
   `cyclone-ios/docs/adr/0001-bundle-id.md` (pattern ADR CLAUDE.md).

Estimation : 30 min de vérification + 15 min de bascule projet. Action
Raphaël (étapes 1 et 3 surtout).
