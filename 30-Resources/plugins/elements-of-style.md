---
intent: plugin-doc
plugin_id: elements-of-style
plugin_full_name: Elements of Style / Writing Clearly and Concisely (Jesse Vincent obra)
project: claude-system
category: prose
regime: invocable
cost: faible
cost_tokens_estimate: 3000
consent_required: false
install_status: installed
date_added: 2026-05-08
status: active
tags: [prose, clarte, strunk-white, ecriture]
synergies: [humanizer]
---

# Elements of Style

## Quoi
Skill qui encode les regles de Strunk & White pour ecrire plus clairement et plus concisement. Il force des choix de style concrets: voix active, suppression du superflu, vocabulaire direct.

## Quand l'utiliser (situations génériques, multi-projets)
- Reviser README, guides techniques, specs fonctionnelles ou docs internes.
- Nettoyer des commit messages et descriptions de pull request.
- Simplifier des messages d'erreur ou textes d'interface.
- Ameliorer la clarte de contenus business (memo, compte-rendu, proposition).

## Mécanisme
Le skill est un corpus Markdown structure autour de regles grammaticales, principes de composition et usages lexicaux. L'invocation applique ces regles comme contrainte de re-ecriture sur le texte fourni. Il agit comme filtre de clarte avant d'autres passes stylistiques. Aucun code executable n'est requis: tout repose sur une grille redactionnelle normative.

## Coût estimé
Environ 3000 tokens pour un passage sur un document court a moyen. Regime invocable, ideal en premiere passe de revision redactionnelle.

## Synergies
- humanizer : sequence recommandee = clarte d'abord, puis personnalisation du ton.
- research-companion : utile pour transformer des analyses d'idees en notes de synthese plus nettes.

## Anti-synergies / contre-indications
- A eviter pour des textes litteraires ou marketing volontairement exubérants, ou lorsque la contrainte stylistique contractuelle s'oppose a la simplification.

## Source
https://github.com/obra/the-elements-of-style — Jesse Vincent (obra)

## Install status
Installé chez Raphaël le 2026-05-08 sous `/root/.claude/skills/elements-of-style/` (skill user / plugin marketplace).

