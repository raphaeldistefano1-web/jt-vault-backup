---
backlinks:
- 2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i
- 2026-05-08-team-interne-task-list-pour-paralléliser-multi-fin
- 2026-05-09-hook-dispatch-advisor-pour-suggestions-intelligent
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- _Index
category: research
consent_required: false
cost: lourd
cost_tokens_estimate: 20000
date_added: 2026-05-08
install_status: installed
intent: plugin-doc
plugin_full_name: Claude Deep Research Skill (199-biotechnologies)
plugin_id: deep-research
project: claude-system
regime: invocable
status: active
synergies:
- research-companion
- codex-peer-review
tags:
- research
- citation-tracking
- multi-source
- due-diligence
---

# Deep Research

## Quoi
Skill de recherche structuree en pipeline multi-phases pour produire des resultats traces, cites et auditables. Il est concu pour la due diligence et les sujets ou l'hallucination documentaire est un risque critique.

## Quand l'utiliser (situations génériques, multi-projets)
- Comparer des stacks techniques avant un choix d'architecture.
- Produire un etat de l'art sur un sujet IA, produit ou marche.
- Verifier des claims sensibles avant publication ou decision d'investissement.
- Construire une veille periodique avec shortlist argumentee et sources robustes.

## Mécanisme
Le workflow suit des etapes explicites: cadrage, plan, retrieval parallele, triangulation, synthese, critique, raffinement et packaging final. Le skill applique du scoring de credibilite des sources et impose des exigences de densite de preuves par claim. Des scripts Python (dont `source_evaluator.py`) soutiennent l'evaluation des sources et la qualite de citation. Les sorties sont ecrites dans `~/Documents/[Topic]_Research_[Date]/` pour archivage.

## Coût estimé
Environ 20000 tokens minimum pour un dossier solide multi-sources, souvent plus selon l'ampleur du sujet. Regime invocable et ponctuel: a reserver aux decisions a fort impact.

## Synergies
- research-companion : aide a prioriser quelles pistes passer en deep-research complet.
- codex-peer-review : fournit une relecture contradictoire des conclusions avant action.

## Anti-synergies / contre-indications
- A eviter pour des questions triviales ou urgentes a faible enjeu, car le cout et la latence sont volontairement eleves.

## Source
https://github.com/199-biotechnologies/claude-deep-research-skill — 199-biotechnologies

## Install status
Installé chez Raphaël le 2026-05-08 sous `/root/.claude/skills/deep-research/` (skill user / plugin marketplace).