---
backlinks:
- 2026-05-09-codex-cli-en-mcp-server-pour-économiser-quota-clau
- 2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi
- 2026-05-10-claude-max-quota-fenêtre-5h-limitée-stratégie-rése
- _Index
category: code-quality
consent_required: false
cost: moyen
cost_tokens_estimate: 7000
date_added: 2026-05-08
install_status: installed
intent: plugin-doc
plugin_full_name: Codex Peer Review (jcputney)
plugin_id: codex-peer-review
project: claude-system
regime: invocable
related:
- 2026-05-10-claude-max-quota-fenêtre-5h-limitée-stratégie-rése
status: active
synergies:
- devils-advocate
- code-reviewer
tags:
- code-review
- peer-review
- codex
- ai-collaboration
---

# Codex Peer Review

## Quoi
Plugin de revue croisee ou Claude et Codex CLI analysent le meme code de facon independante puis confrontent leurs conclusions. L'objectif est d'augmenter la fiabilite des decisions de merge par divergence constructive.

## Quand l'utiliser (situations génériques, multi-projets)
- Avant push d'un commit non trivial modifiant comportement ou architecture.
- Avant merge d'une PR sensible (securite, data, auth, performance).
- Obtenir un second avis structure sur un refactor important.
- Verifier une decision technique qui engage plusieurs sprints.

## Mécanisme
Le plugin declenche un agent dedie (`codex-peer-reviewer`) qui orchestre la revue en aveugle et le debat issue-par-issue. Les statuts d'arbitrage sont deterministes (proposed, accepted, rejected, merged, escalated). L'analyse Codex et l'analyse Claude restent separees jusqu'a la phase de confrontation. Le resultat est un protocole de revue reproductible, pas une simple opinion unique.

## Coût estimé
Environ 7000 tokens pour une revue moyenne, hors cout eventuel de contexte code volumineux. Regime invocable, a utiliser comme gate qualite avant integration.

## Synergies
- devils-advocate : ajoute une couche de critique interne structuree avant ou apres la revue croisee.
- pre-mortem : complete la revue actuelle par une anticipation des echec futurs post-deploiement.

## Anti-synergies / contre-indications
- A eviter sur micro-correctifs evidents, ou en doublon avec un processus de revue deja surcharge lorsque le time-to-fix prime.

## Source
https://github.com/jcputney/agent-peer-review — jcputney

## Install status
Installé chez Raphaël le 2026-05-08 sous `plugin marketplace: codex-peer-review@agent-peer-review-marketplace` (skill user / plugin marketplace).

## Related

- [[2026-05-10-claude-max-quota-fenêtre-5h-limitée-stratégie-rése]] — Claude Max quota — fenêtre 5h limitée, stratégie réservation