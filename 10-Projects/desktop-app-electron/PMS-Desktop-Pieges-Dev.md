---
ai_writable: true
area: null
backlinks:
- 2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées
- 2026-05-12-tailscale-cli-installation-sur-macos
- PMS-Desktop-Etat
- _Index
- _VAULT-INDEX
confidence: high
created: 2026-05-07
embed_hash: null
embed_model_version: null
entities:
- cross-compile
- gatekeeper
- offline-mutations
- drag-region
- cookies-partition
id: 20260507-1114-pms-desktop-pieges
intent: how-to
last-accessed: 2026-05-07
moc: '[[_MOC-desktop-app]]'
project: pms-desktop
related:
- 2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées
- 2026-05-12-tailscale-cli-installation-sur-macos
- '[[PMS-Desktop-Etat]]'
- '[[_MOC-desktop-app]]'
source: memory:feedback_pms_desktop_dev.md
status: active
summary: Cross-compile Linux→macOS limites (pas dmg/universal), mutations offline
  désactivées, Gatekeeper xattr, cookies tray, drag region no-drag.
tags:
- pms
- desktop
- electron
- piege
tier: warm
title: Pièges du dev — Electron PMS Desktop
topic_cluster: desktop-app
type: feedback
updated: 2026-05-07
---

# Pièges du dev — Electron PMS Desktop

> Note portée depuis la mémoire Claude Code `feedback_pms_desktop_dev.md` le 2026-05-07.

Pièges rencontrés lors de la livraison du logiciel desktop PMS sur la session avr 2026.

## Cross-compile Linux → macOS : limitations

**Build .dmg impossible.**
**Why:** `dmg-license` (dépendance d'electron-builder pour DMG) requiert une lib native macOS (`iconv-corefoundation`) qui n'a pas de binaire Linux compilé. Tentatives `npm install --force --os=darwin` échouent à l'exécution avec "invalid ELF header".
**How to apply:** utiliser **target `zip` à la place de `dmg`** dans `electron-builder.yml`. Même UX user (le Mac décompresse auto, glisser-déposer dans Applications), juste pas de fenêtre d'installation jolie.

**Universal binary (fat x64+arm64) impossible.**
**Why:** `@electron/universal` utilise `lipo` qui est un outil Apple macOS-only.
**How to apply:** builds **séparés** `--x64 --arm64` qui produisent 2 zips. Page `/download` détecte l'arch via `navigator.userAgentData.getHighEntropyValues(['architecture'])` (Chrome/Edge only) avec fallback heuristique sur "Apple Silicon par défaut" (~80% du parc Mac récent). Toggle manuel dispo si user Intel.

## Apple Gatekeeper sans signature

**App refusée "endommagée" sur macOS Sonoma+ même après clic-droit → Ouvrir.**
**Why:** Sans signature Apple ($99/an), le bit `com.apple.quarantine` posé par le navigateur lors du téléchargement empêche Gatekeeper de laisser passer, même avec le contournement clic-droit historique.
**How to apply:** documenter `xattr -cr /Applications/PMS\ Le\ Jardin\ Tropical.app` dans la page `/download` comme étape 4 conditionnelle. Refaire après chaque update du .zip. Pour éviter à terme : payer la signature Apple Developer Program (99 $/an) + notarisation via `electron-builder` avec credentials API Connect.

## Pas de mutations offline (volontaire)

**Le Service Worker NE met PAS en queue les POST/PATCH/DELETE.**
**Why:** Risques élevés sur un PMS prod : doublons (création résa 2× au retour), conflits de versions (modif locale vs distante), états incohérents (paiement appliqué mais sync KO). Pas de mécanisme idempotence côté API actuellement.
**How to apply:** stratégie `network-only` pour toutes les mutations dans `public/sw.js`. Le `<OfflineBanner />` indique clairement à l'utilisateur "modifications désactivées". Si un jour on veut vraiment l'offline-first, faut redesign API avec : ETags, idempotency keys client-generated UUID, conflict resolution (last-write-wins ou CRDT).

## Tray window doit partager les cookies de la main window

**Sinon le mini-popover voit `401 Unauthorized` sur `/api/desktop/tray-summary`.**
**Why:** Par défaut chaque BrowserWindow Electron utilise `defaultSession`, mais si on lui passe un `partition`, il a sa propre session isolée — sans les cookies NextAuth.
**How to apply:** **ne PAS spécifier de partition** sur la trayWindow → utilise `defaultSession` comme la mainWindow → cookies partagés. Le HTML standalone (`tray-popup.html`) fetch avec `credentials: 'include'` côté JS.

## preload.js doit être dans `webPreferences.preload` ET listé dans `electron-builder.yml > files`

**Sinon le bridge `window.pmsBridge` est `undefined` au runtime.**
**Why:** electron-builder ne packagebait que les fichiers explicitement listés dans `files:` du config. Le `main.js` est inclus par défaut, pas le preload.
**How to apply:** liste explicite dans le config :
```yaml
files:
  - main.js
  - preload.js
  - tray-preload.js
  - splash.html
  - error.html
  - tray-popup.html
  - assets/**/*
  - package.json
```

## Auto-update sans signature : workflow simplifié

**Pas d'`electron-updater` complet (qui suppose signature pour le replace silent).**
**How to apply:** notre auto-update est **manuel-assisté** :
1. Main process poll `/desktop-version.json` au boot + toutes les 2h
2. Si `versionGreater(remote, app.getVersion())` → notif système + bannière in-app (UpdateBanner.tsx)
3. User clique "Télécharger" → ouvre `/download` dans Safari
4. User refait `xattr -cr` après replacement dans Applications

C'est moins magique qu'electron-updater officiel, mais ça marche sans signature et ne nécessite aucun serveur de release Electron-spécifique (juste un fichier JSON statique).

## Drag region : ne pas oublier `electron-no-drag` sur les boutons

**Si tu mets `-webkit-app-region: drag` sur un parent (ex: la topbar), TOUS les enfants deviennent draggables — y compris les boutons interactifs qui ne répondent plus au clic.**
**How to apply:** classes CSS dans `globals.css` :
```css
.electron-drag { -webkit-app-region: drag; }
.electron-no-drag { -webkit-app-region: no-drag; }
```
Et appliquer `electron-no-drag` sur **chaque** bouton/lien/input dans la zone draggable. Sinon clic mort.

## Tray icon : nom DOIT contenir `Template` pour macOS

**`tray-icon.png` standard = couleur fixée, pas de support light/dark mode.**
**Why:** macOS regarde le suffixe `Template` dans le nom de fichier ; si présent, traite l'image comme un masque monochrome qu'il colore selon le thème menu bar (noir en light mode, blanc en dark mode, accent quand sélectionné).
**How to apply:** nommer le fichier `tray-iconTemplate.png` (sans tiret, suffixe accolé). Le SVG source doit être en **noir uni sur transparent** (pas de couleur, sinon macOS l'ignore et ne fait pas l'inversion auto).

## Liens
- MOC parent : [[_MOC-desktop-app]]
- État du projet : [[PMS-Desktop-Etat]]
- Source : `memory:feedback_pms_desktop_dev.md`

## Related

- [[2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées]] — Sudo silent failures et env vars non-appliquées
- [[2026-05-12-tailscale-cli-installation-sur-macos]] — Tailscale CLI installation sur macOS