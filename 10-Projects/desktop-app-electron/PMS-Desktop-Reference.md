---
ai_writable: true
area: null
backlinks:
- PMS-Desktop-Etat
- _Index
confidence: high
created: 2026-05-07
embed_hash: null
embed_model_version: null
entities:
- endpoints
- build-commands
- version-manifest
- gatekeeper
- xattr
id: 20260507-1112-pms-desktop-ref
intent: how-to
last-accessed: 2026-05-07
moc: '[[_MOC-desktop-app]]'
project: pms-desktop
related:
- OpenClaw-VPS-Reference
- VPS-Access-Tailscale
- '[[PMS-Desktop-Etat]]'
- '[[_MOC-desktop-app]]'
source: memory:reference_pms_desktop.md
status: active
summary: Endpoints API tray-summary et hotel-config, version manifest, commandes build/deploy
  VPS, xattr Gatekeeper.
tags:
- pms
- desktop
- api
- build
tier: hot
title: PMS Desktop — Paths, endpoints, commandes
topic_cluster: desktop-app
type: reference
updated: 2026-05-07
---

# PMS Desktop — Paths, endpoints, commandes

> Note portée depuis la mémoire Claude Code `reference_pms_desktop.md` le 2026-05-07.

Référence rapide pour intervenir sur le wrapper Electron du PMS.

## URLs publiques

- **PMS web** : `http://46.202.171.204:3000` (IP VPS Hostinger, hardcodée dans `desktop/main.js:PMS_URL`)
- **Page téléchargement** : `http://46.202.171.204:3000/download` (auto-detect arch + instructions xattr)
- **Version manifest** : `http://46.202.171.204:3000/desktop-version.json` (lu par main process auto-update)

## Endpoints API dédiés desktop

- `GET /api/desktop/tray-summary` — auth-gated, retourne `{ now, occupancy: {occupied,total,pct}, arrivals: [...], unread }` pour le mini-panel tray (1 round-trip)
- `GET /api/hotel-config` — config hôtel (HotelConfig model, valeurs Decimal converties en number)
- `PATCH /api/hotel-config` — update config (auth ADMIN/MANAGER), revalide `/dashboard/settings`

## Commandes utiles VPS

```bash
# Rebuild Electron + copy zips dans public/downloads
cd /var/www/pms-jardin-tropical/desktop && rm -rf dist && npm run build:mac
cd /var/www/pms-jardin-tropical
cp desktop/dist/PMS-JardinTropical-{version}-arm64.zip public/downloads/PMS-JardinTropical-mac-arm64.zip
cp desktop/dist/PMS-JardinTropical-{version}-x64.zip   public/downloads/PMS-JardinTropical-mac-intel.zip

# Bumper la version (3 endroits) :
# 1) desktop/package.json     "version": "1.X.0"
# 2) public/desktop-version.json     { "version": "1.X.0", "notes": "..." }
# 3) (optionnel) commit message

# Build Next + restart
pnpm build && pm2 restart pms-ljt --update-env
```

## Commande Mac user (xattr Gatekeeper)

À exécuter par Raphaël après chaque téléchargement de nouveau .zip pour passer Gatekeeper (app non-signée Apple) :

```bash
xattr -cr /Applications/PMS\ Le\ Jardin\ Tropical.app
```

Si l'app est encore dans Téléchargements :
```bash
xattr -cr ~/Downloads/PMS\ Le\ Jardin\ Tropical.app
```

## Deep links pms://

Schémas supportés :
- `pms://open?path=/dashboard/reservations/abc` (forme query)
- `pms:///dashboard/calendar` (forme path direct)
- `pms://open` (default → `/dashboard`)

Single instance lock garantit qu'un clic sur un lien ouvre la fenêtre existante (pas une nouvelle).

## Service Worker

- `public/sw.js` versionné `pms-sw-v3` (incrémenter à chaque grosse modif des stratégies pour invalider)
- Caches : `pms-sw-v3-static`, `pms-sw-v3-pages`, `pms-sw-v3-api`
- API cachées listées dans `CACHEABLE_API_PATTERNS`
- Pour ajouter un endpoint à cacher : ajouter au tableau et bumper `VERSION`

## Bridge Electron exposé

Côté renderer (dans le PMS web), si on est dans le wrapper :
```ts
window.pmsBridge?.setBadge(unreadCount)
window.pmsBridge?.notify({ title, body, url })
window.pmsBridge?.markAllSeen()
window.pmsBridge?.openDownloadPage()
window.pmsBridge?.onUpdateAvailable((payload) => { ... })
```

Types dans `src/types/desktop-bridge.d.ts` (avec `declare global { interface Window }`).

Toujours utiliser optional chaining `?.` — `pmsBridge` est `undefined` en navigateur classique.

## Liens
- MOC parent : [[_MOC-desktop-app]]
- État du projet : [[PMS-Desktop-Etat]]
- Source : `memory:reference_pms_desktop.md`

## Related

- [[OpenClaw-VPS-Reference]] — OpenClaw-VPS-Reference
- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)