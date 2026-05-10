---
backlinks:
- _Index
category: thinking
consent_required: false
cost: faible
cost_tokens_estimate: 4000
date_added: 2026-05-08
install_status: installed
intent: plugin-doc
plugin_full_name: Pre-Mortem (Matthew Honnibal, créateur spaCy)
plugin_id: pre-mortem
project: claude-system
regime: invocable
status: active
synergies:
- thinking-skills
- devils-advocate
tags:
- pre-mortem
- failure-modes
- deploy
- audit
---

# Pre-Mortem

## Quoi
Skill de prospective "hindsight" qui suppose l'echec futur d'une initiative pour identifier les causes en amont. Il permet de rendre visibles les hypotheses fragiles avant qu'elles ne coutent cher.

## Quand l'utiliser (situations génériques, multi-projets)
- Avant un deploiement production ou une migration irreversible.
- Avant de lancer une nouvelle fonctionnalite a grande surface d'impact.
- Avant de signer un contrat ou une decision engageante.
- Avant une operation technique risquee (refactor massif, changement infra, rotation secrete).

## Mécanisme
Le skill repose sur un protocole Markdown invocable qui force la formulation de scenarios d'echec plausibles. Chaque scenario est retro-analyse en causes racines, signaux precoces et mesures de mitigation. La valeur vient du changement de cadre cognitif, pas d'un script technique. Il peut etre execute rapidement comme gate de securite avant action.

## Coût estimé
Environ 4000 tokens pour une analyse pre-mortem ciblee sur une decision. Regime invocable, ideal juste avant les moments a risque.

## Synergies
- thinking-skills : complete le pre-mortem avec inversion, second-order effects et autres cadres analytiques.
- devils-advocate : ajoute une couche contradictoire independante apres la premiere analyse.

## Anti-synergies / contre-indications
- A eviter en boucle sur des micro-decisions quotidiennes, car cela peut ralentir inutilement l'execution.

## Source
https://github.com/honnibal/claude-skills — Matthew Honnibal

## Install status
Installé chez Raphaël le 2026-05-08 sous `/root/.claude/skills/pre-mortem/` (skill user / plugin marketplace).