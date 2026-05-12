---
backlinks:
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- 2026-05-09-impeccable-surpasse-frontend-design-officiel
- 2026-05-09-responsive-design-obligatoire-pour-toute-interface
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
- _Index
category: design
consent_required: false
cost: faible
cost_tokens_estimate: 4000
date_added: 2026-05-08
install_status: installed
intent: plugin-doc
plugin_full_name: Interface Design (Damola Akinleye)
plugin_id: interface-design
project: claude-system
regime: always-on-passive
status: active
synergies:
- impeccable
- emil-design-eng
tags:
- design
- persistence
- anti-drift
- design-system
- decisions
---

# Interface Design

## Quoi
Plugin design qui conserve les decisions visuelles entre sessions pour eviter la derive progressive des interfaces. Son apport cle est la memoire structurelle du systeme visuel dans le repo.

## Quand l'utiliser (situations génériques, multi-projets)
- Maintenir une coherence UI sur des projets long-terme evoluant en plusieurs sessions.
- Stabiliser des choix de spacing, rayons, typographie et composants partages.
- Cadencer un workflow preview-then-apply sur des refontes iteratives.
- Eviter les regressions de style quand plusieurs agents interviennent sur le meme produit.

## Mécanisme
Le plugin ecrit et met a jour un fichier de reference `.interface-design/system.md` dans le repo courant. Les commandes/skills exploitent ce fichier comme source de verite pour re-appliquer les memes decisions dans le temps. Le regime always-on-passive signifie qu'il peut influencer le contexte sans invocation explicite a chaque tour. C'est un mecanisme anti-drift plus qu'un generateur de styles autonome.

## Coût estimé
Environ 4000 tokens par passe de mise a jour du systeme de design. Regime always-on-passive, avec cout faible car reutilisation continue des decisions deja formalisees.

## Synergies
- impeccable : fournit une critique qualitative, interface-design enregistre et stabilise les choix retenus.
- emil-design-eng : fige aussi les decisions motion pour conserver le meme ressenti produit.

## Anti-synergies / contre-indications
- A limiter sur des prototypes jetables tres courts, ou quand aucune persistance repo n'est souhaitee.

## Source
https://github.com/Dammyjay93/interface-design — Damola Akinleye

## Install status
Installé chez Raphaël le 2026-05-08 sous `plugin marketplace: interface-design@interface-design` (skill user / plugin marketplace).