---
intent: plugin-doc
plugin_id: humanizer
plugin_full_name: Humanizer (Brent Lader)
project: claude-system
category: prose
regime: invocable
cost: faible
cost_tokens_estimate: 4000
consent_required: false
install_status: installed
date_added: 2026-05-08
status: active
tags: [prose, anti-ai-slop, voice-match, ecriture]
synergies: [elements-of-style]
---

# Humanizer

## Quoi
Skill d'ecriture anti-AI-tells qui reduit les traces stylistiques detectables des textes LLM. Il apporte aussi un mode de voice-matching base sur un echantillon de la voix utilisateur.

## Quand l'utiliser (situations génériques, multi-projets)
- Finaliser un email, une note publique ou un message sensible lu par des humains.
- Reprendre un texte issu de dictee vocale avant diffusion.
- Uniformiser le ton dans une documentation multi-auteurs.
- Nettoyer un brouillon IA avant publication blog, reseaux ou newsletter.

## Mécanisme
Le skill fournit une checklist de patterns linguistiques a detecter et corriger (rythmes repetitifs, tournures artificielles, formules sterotypiques). L'invocation se fait en une ou deux passes sur le texte cible. Le mode voice-match compare un echantillon d'ecriture de reference et applique les ajustements de style au rewrite. Il n'y a pas de script runtime: la transformation est pilotee par consignes de revision.

## Coût estimé
Environ 4000 tokens pour une passe de nettoyage + voice-match sur un texte moyen. Regime invocable, a placer en derniere etape d'ecriture.

## Synergies
- elements-of-style : clarifie d'abord le fond et la structure, puis humanizer adoucit la forme finale.
- deep-research : utile pour transformer un rapport de recherche technique en rendu plus lisible pour non-specialistes.

## Anti-synergies / contre-indications
- A eviter sur textes juridiques/contractuels figés mot a mot, ou quand une voix tres neutre et mecanique est volontaire.

## Source
https://github.com/blader/humanizer — Brent Lader

## Install status
Installé chez Raphaël le 2026-05-08 sous `/root/.claude/skills/humanizer/` (skill user / plugin marketplace).

