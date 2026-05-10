---
ai_writable: true
area: null
backlinks:
- PMS-Desktop-Pieges-Dev
- PMS-Desktop-Reference
- _Index
- _VAULT-INDEX
confidence: high
created: 2026-05-07
embed_hash: null
embed_model_version: null
entities:
- electron
- pms
- desktop-app
- macos
- notifications
- deep-links
- offline-mode
id: 20260507-1110-pms-desktop-etat
intent: log
last-accessed: 2026-05-07
moc: '[[_MOC-desktop-app]]'
project: pms-desktop
related:
- '[[_MOC-desktop-app]]'
- '[[PMS-Desktop-Reference]]'
- '[[PMS-Desktop-Pieges-Dev]]'
source: memory:project_pms_desktop_app.md
status: active
summary: Wrapper Electron v1.3.0 stable pour le PMS Next.js avec notifs macOS, tray
  menu bar, deep links, offline mode et auto-update manuel.
tags:
- pms
- electron
- macos
tier: hot
title: Logiciel desktop PMS Le Jardin Tropical — État (Electron v1.3.0)
topic_cluster: desktop-app
type: project
updated: 2026-05-07
---

# Logiciel desktop PMS Le Jardin Tropical — État

> Note portée depuis la mémoire Claude Code `project_pms_desktop_app.md` le 2026-05-07.

État du logiciel desktop macOS du PMS au 22 avril 2026, version actuelle **1.3.0**.

**Why:** Référence pour les futures évolutions du wrapper Electron. La structure est entièrement fonctionnelle, les patterns natifs macOS sont en place — il faut juste continuer dessus, pas refondre.

**How to apply:** Toute nouvelle feature desktop (ex: extension menu bar, deep link path supplémentaire, notification custom) se branche sur l'infra existante. Voir `[[PMS-Desktop-Reference]]` pour les paths précis.

## Architecture

```
desktop/
├── main.js             ← process principal
├── preload.js          ← bridge main window (window.pmsBridge)
├── tray-preload.js     ← bridge tray window (window.electronTray)
├── tray-popup.html     ← mini-panel HTML standalone (dark mode auto)
├── splash.html         ← cold start
├── error.html          ← VPS injoignable
├── electron-builder.yml ← packaging + CFBundleURLTypes pms://
├── package.json        ← v1.3.0
└── assets/
    ├── icon.png                  ← 1024×1024
    ├── tray-iconTemplate.png     ← 22×22 (template macOS)
    └── tray-iconTemplate@2x.png  ← 44×44 (retina)
```

## Features livrées par version

### v1.0 (base wrapper)
- Frame `hiddenInset` traffic lights overlay style Linear/Notion
- Splash + error page avec URL passée en query param
- Menu natif français complet (PMS / Édition / Affichage / Fenêtre / Aide)
- Page `/download` sur le PMS avec auto-detect Apple Silicon vs Intel + instructions xattr

### v1.1 (polish natif)
- `electron-window-state` : taille + position mémorisées entre lancements
- Drag region topbar (`-webkit-app-region: drag` via classe CSS `electron-drag`)
- `nativeTheme` follow OS (light/dark)
- Raccourcis : ⌘N (résa), ⌘K (recherche via dispatch keyboard event), ⌘1-5 (nav directe), ⌘, (préférences), ⌘R (refresh)
- About dialog natif via `dialog.showMessageBox`
- Single instance lock (anti-doublon)

### v1.1 + Phase 1 (notifs + auto-update)
- **Bridge `window.pmsBridge`** sandbox-safe : `setBadge(n)`, `notify({title,body,url})`, `markAllSeen()`, `onUpdateAvailable(cb)`, `openDownloadPage()`
- `NotificationsBell.tsx` push au bridge à chaque poll → `app.setBadgeCount()` + `new Notification()` pour les nouveaux items (diff via `seenIdsRef`)
- Auto-update : poll `/desktop-version.json` au boot (10s) + toutes les 2h, `versionGreater()` semver → notif système + bannière in-app `<UpdateBanner />` orange dans DashboardShell

### v1.2 + Phase B (tray menu bar)
- Tray icon Jt template dans la barre menu macOS
- `createTrayWindow()` : 320×440, frameless, transparent OFF (rendu propre), preload `tray-preload.js`, partition shared avec main → cookies NextAuth dispos
- Position calculée depuis `tray.getBounds()` + clampée au workArea du display
- Auto-hide on blur, re-load on focus
- Endpoint `/api/desktop/tray-summary` (1 round-trip : rooms count + in-house + 6 arrivées + unread)
- Mini-panel HTML standalone (`tray-popup.html`) avec dark mode `prefers-color-scheme`, fetch côté client avec `credentials: 'include'`
- Clic droit tray → menu natif (Ouvrir, Nouvelle résa, Planning, Messagerie, Quitter)

### v1.3 + Phase D + E (deep links + offline + print + dock menu)
- **Deep links `pms://`** : `app.setAsDefaultProtocolClient('pms')` + handler `app.on('open-url')` macOS + `app.on('second-instance')` Win-style. Format : `pms://open?path=/dashboard/reservations/abc` ou `pms:///dashboard/calendar`. Single instance lock pour ne pas multiplier les fenêtres.
- **Dock menu macOS** : `app.dock.setMenu()` clic droit sur l'icône dock = 5 actions rapides
- **Bouton Imprimer factures** dans `InvoicesList.tsx` : `window.open(/api/invoices/.../pdf)` + `w.print()` au load → dialog Print natif macOS via Electron
- **Service Worker** (`public/sw.js`) avec 4 stratégies :
  - `_next/static/*` → cache-first
  - GET `/api/*` listés (dashboard, notifications, reservations, calendar, etc.) → **stale-while-revalidate**
  - Pages `/dashboard/*` → network-first avec fallback cache
  - **Mutations POST/PATCH/DELETE → network-only** (pas de queue offline pour éviter doublons sur données prod — décision volontaire)
- `<ServiceWorkerRegister />` monté dans DashboardShell, skip dev/file://
- `<OfflineBanner />` : `navigator.onLine` + ping `/api/nav/counts` HEAD toutes les 30s, bandeau warning douce
- `Info.plist` étendu : `CFBundleURLTypes` (`pms://`) + `NSUserNotificationAlertStyle: alert`

## Z-index conventions Electron

L'app desktop utilise les mêmes tokens CSS que le web (cf. globals.css `--z-*`). Aucun overlay Electron-spécifique n'est ajouté côté JS, sauf le tray window qui est une fenêtre séparée.

## Build & déploiement

- Build cross-compile Linux → macOS x64 + arm64 (`electron-builder --mac zip --x64 --arm64`)
- **Universal binary impossible** depuis Linux (lipo macOS-only) → 2 builds séparés
- **DMG impossible** depuis Linux (`dmg-license` requiert lib native macOS) → target `zip` à la place
- Output dans `desktop/dist/PMS-JardinTropical-{version}-{arch}.zip`
- Script de release : `cp desktop/dist/PMS-JardinTropical-{version}-{arch}.zip public/downloads/PMS-JardinTropical-mac-{arm64,intel}.zip` + bump `public/desktop-version.json`
- Auto-update prompt apparaît dans toutes les apps au prochain check (max 2h)

## Limites connues (vs natif Swift)

- Controls custom CSS/HTML (pas NSButton/NSDatePicker)
- Animations CSS (pas spring physics natives)
- Pas de Spotlight indexing, Shortcuts/Raccourcis, Continuity iPhone, Touch ID
- 88-93 Mo par zip (Chromium runtime embarqué)
- Mutations offline non supportées (volontairement)

## Liens
- MOC parent : [[_MOC-desktop-app]]
- Reference détaillée : [[PMS-Desktop-Reference]]
- Pièges dev : [[PMS-Desktop-Pieges-Dev]]
- Source : `memory:project_pms_desktop_app.md`