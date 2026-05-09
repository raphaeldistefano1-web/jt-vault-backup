---
intent: plugin-doc
plugin_id: impeccable
plugin_full_name: Impeccable (Paul Bakaus)
project: claude-system
category: design
regime: invocable
cost: faible
cost_tokens_estimate: 5000
consent_required: false
install_status: installed
date_added: 2026-05-08
status: active
tags: [design, anti-ai-slop, frontend, polish, audit-design]
synergies: [emil-design-eng, interface-design, color-expert, frontend-design]
---

# Impeccable

## Quoi
Skill design qui force Claude a sortir des patterns UI generiques "AI-look". Il apporte un cadre deterministe avec anti-patterns, regles critiques et commandes de polish.

## Quand l'utiliser (situations génériques, multi-projets)
- Concevoir une nouvelle interface web ou desktop avec une direction visuelle forte.
- Auditer une UI existante avant livraison client ou publication publique.
- Polir un composant transverse (cards, tables, formulaires, nav) sans refaire tout le design system.
- Passer d'un mode "product" a un mode "brand" sur landing, portfolio ou page campagne.

## Mécanisme
Le skill repose sur un fichier Markdown structure autour de patterns reproductibles et d'anti-patterns explicites. L'invocation active des modes comme craft, shape, audit ou critique selon l'objectif. Les commandes de type polish/distill/animate/bolder/quieter servent de "passes" specialisees sur un rendu deja existant. Il n'y a pas de runtime executable: la valeur vient du cadre de decision applique a la generation.

## Coût estimé
Environ 5000 tokens par utilisation complete, variable selon la profondeur d'audit. Regime invocable: on l'active sur demande pour les passes design, pas en permanence.

## Synergies
- emil-design-eng : complete la direction visuelle avec des decisions motion et micro-interactions.
- color-expert : verrouille la palette, les contrastes et les tokens couleur une fois la forme definie.

## Anti-synergies / contre-indications
- A eviter pour une correction purement fonctionnelle/backend sans enjeu d'interface, ou en doublon avec un audit design deja fige dans la meme session.

## Source
https://github.com/pbakaus/impeccable — Paul Bakaus

## Install status
Installé chez Raphaël le 2026-05-08 sous `/root/.claude/skills/impeccable/` (skill user / plugin marketplace).
