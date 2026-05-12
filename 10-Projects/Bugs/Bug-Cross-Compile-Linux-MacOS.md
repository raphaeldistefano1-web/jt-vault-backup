---
ai_writable: true
backlinks:
- 2026-05-12-tailscale-cli-installation-sur-macos
- Desktop-App-Electron
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-05-12
description: Stub — cross-compilation Linux→macOS impossible pour pkg dmg/universal
  sur l'app Electron desktop PMS
embed_hash: null
embed_model_version: null
entities:
- electron
- desktop
- cross-compile
id: 202605120000-bug-cross-compile-linux-macos
intent: log
last-accessed: 2026-05-12
project: Bugs
related:
- 2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées
- 2026-05-12-tailscale-cli-installation-sur-macos
status: stub
summary: Cross-compile Linux→macOS limité pour dmg/universal de l'app Electron desktop
  PMS
tags:
- bug
- electron
- desktop
tier: cold
type: bug
updated: 2026-05-12
---

# Bug Cross Compile Linux→macOS

> **Stub** — Note référencée par wikilinks orphelins, à compléter.

Contexte : développement du wrapper Electron PMS sur VPS Linux. La build cross-compile pour macOS ne produit pas de `.dmg` ni de bundle universal (arm64+x64). Workaround actuel : build local Mac via `npm run build:mac` (cf. mémoire CC `feedback_pms_desktop_dev.md`).

## À documenter

- [ ] Versions electron-builder concernées
- [ ] Erreur exacte (log build)
- [ ] Workaround retenu (build sur Mac local)
- [ ] Alternative (GitHub Actions runner macOS ?)

## Related

- [[Desktop-App-Electron]]
- [[_MOC-desktop-app]]
- [[2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées]] — Sudo silent failures et env vars non-appliquées
- [[2026-05-12-tailscale-cli-installation-sur-macos]] — Tailscale CLI installation sur macOS