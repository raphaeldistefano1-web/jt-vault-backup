---
ai_writable: false
created: 2026-04-25
description: Wrapper Electron v1.3.0 du PMS — notifs natives, badge dock, tray menu
  bar, deep links pms://, mode offline lecture
embed_hash: null
embed_model_version: null
entities:
- api
- electron
- pms
id: 202604252031-desktop-app-electron
intent: reference
last-accessed: 2026-04-25
project: desktop-app-electron
related:
- '[[Dev-PMS-Area]]'
- '[[PMS-Stack]]'
- '[[Bug-Cross-Compile-Linux-MacOS]]'
relevance: high
status: deployed
summary: ✅ Déployée prod cf. mémoire projectpmsdesktopapp.md.
tags:
- pms
- electron
- desktop
- app
tier: warm
topic_cluster: pms-desktop
type: project
updated: 2026-04-25
---

# 🖥️ Desktop App Electron v1.3.0

## État

✅ **Déployée prod** (cf. mémoire `project_pms_desktop_app.md`).

## Fonctionnalités

- **Notifications natives** OS (macOS Notification Center, Windows toast, Linux libnotify)
- **Badge dock** macOS (compteur d'événements en attente)
- **Tray menu bar** macOS — accès rapide aux actions PMS sans ouvrir la fenêtre principale
- **Deep links `pms://`** — l'app intercepte les liens custom (utile pour notifications cliquables)
- **Mode offline lecture** — accès aux données déjà chargées même sans réseau
- **Auto-update prompt** — détecte nouvelles versions et propose la MAJ

## Endpoints API utilisés

- `tray-summary` : compteur événements pour le badge/tray
- `hotel-config` : récup config hôtel pour personnalisation app

## Path serveur

Cf. mémoire `reference_pms_desktop.md` pour :
- URL téléchargement
- Endpoints API précis
- Commandes build/deploy
- Workaround xattr Gatekeeper macOS

## Pièges connus

[[Bug-Cross-Compile-Linux-MacOS]] :
- Cross-compile Linux → macOS limites (pas de dmg/universal)
- Pas de mutations en mode offline
- Gatekeeper xattr obligatoire pour macOS distribution
- Partition cookies tray (séparé de fenêtre principale)
- CSS `drag region: no-drag` sur les boutons cliquables

## Liens

- [[Dev-PMS-Area]]
- [[PMS-Stack]]
- Mémoire référence : `project_pms_desktop_app.md` + `reference_pms_desktop.md`