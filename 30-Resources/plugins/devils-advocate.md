---
backlinks:
- 2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi
- 2026-05-10-claude-max-quota-fenêtre-5h-limitée-stratégie-rése
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- 2026-05-11-testing-vérification-obligatoires-après-chaque-éta
- 2026-05-11-utiliser-ultrareview-avant-merge-de-changements-pl
- _Index
category: thinking
consent_required: false
cost: faible
cost_tokens_estimate: 5000
date_added: 2026-05-08
install_status: installed
intent: plugin-doc
plugin_full_name: Devil's Advocate (Brandon Simpson)
plugin_id: devils-advocate
project: claude-system
regime: invocable
related:
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- 2026-05-11-testing-vérification-obligatoires-après-chaque-éta
status: active
synergies:
- codex-peer-review
- pre-mortem
tags:
- self-critique
- adversarial
- code-review
- plan-review
---

# Devil's Advocate

## Quoi
Plugin de critique contradictoire qui challenge automatiquement code ou plan avec une grille d'evaluation explicite. Son point fort est la separation auteur/critique via un subagent independant pour reduire le biais de confirmation.

## Quand l'utiliser (situations génériques, multi-projets)
- Apres une implementation non triviale avant de declarer "termine".
- Apres la redaction d'un plan d'execution ou d'une strategie produit.
- Avant merge d'un changement a impact architecture, securite ou performance.
- Pour obtenir un contre-argument solide sur une decision deja prise.

## Mécanisme
Le plugin detecte le type de sortie (code vs plan) puis applique des criteres adaptes par dimensions d'evaluation. Il declenche un subagent de critique distinct de l'agent auteur pour eviter l'auto-complaisance. Les issues sont journalisees avec statuts et arbitrages explicites. C'est un mecanisme de revue adversariale operationnelle, pas seulement un checklist statique.

## Coût estimé
Environ 5000 tokens pour une revue ciblee d'un lot moyen. Regime invocable, recommande en gate avant push/merge sur sujets sensibles.

## Synergies
- codex-peer-review : combine critique interne et avis externe en aveugle pour renforcer la robustesse.
- pre-mortem : couvre a la fois les failles presentes et les modes d'echec futurs.

## Anti-synergies / contre-indications
- A eviter pour des edits mineurs cosmetiques, ou quand le delai impose une correction immediate sans cycle de revue complet.

## Source
https://github.com/brandonsimpson/devils-advocate — Brandon Simpson

## Install status
Installé chez Raphaël le 2026-05-08 sous `plugin marketplace: devils-advocate@devils-advocate` (skill user / plugin marketplace).

## Related

- [[2026-05-11-testing-vérification-obligatoires-après-chaque-éta]] — Testing + vérification obligatoires après chaque étape migration
- [[2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos]] — Git init empty baseline pour ultrareview sur repos existants