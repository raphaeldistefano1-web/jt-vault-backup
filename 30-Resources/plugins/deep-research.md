---
intent: plugin-doc
plugin_id: deep-research
plugin_full_name: Claude Deep Research Skill (199-biotechnologies)
project: claude-system
category: research
regime: invocable
cost: lourd
cost_tokens_estimate: 20000
consent_required: false
install_status: installed
date_added: 2026-05-08
status: active
tags: [research, citation-tracking, multi-source, due-diligence]
synergies: [research-companion, codex-peer-review]
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

