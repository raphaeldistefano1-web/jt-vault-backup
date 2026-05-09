---
intent: plugin-doc
plugin_id: color-expert
plugin_full_name: Color Expert (meodai / David Aerne)
project: claude-system
category: design
regime: invocable
cost: moyen
cost_tokens_estimate: 8000
consent_required: false
install_status: installed
date_added: 2026-05-08
status: active
tags: [design, couleur, palette, oklch, apca]
synergies: [impeccable, interface-design]
---

# Color Expert

## Quoi
Base de connaissances couleur tres complete pour prendre des decisions palette solides et mesurables. Le skill pousse une approche moderne (OKLCH/OKLAB, APCA, accessibilite reelle, perception humaine).

## Quand l'utiliser (situations génériques, multi-projets)
- Definir ou refondre une palette pour web app, dashboard, site contenu ou application desktop.
- Construire des ramps couleur et des design tokens utilisables en code.
- Auditer les contrastes et la lisibilite d'une interface en conditions reelles.
- Preparer un theme dark mode avec fidelite visuelle et bonne separation des niveaux.

## Mécanisme
Le skill combine une couche Markdown d'orchestration avec un corpus de references volumineux (`references/`, 144 fichiers). Lors de l'invocation, Claude s'appuie sur ces references pour arbitrer conversions, contrastes et harmonies selon le contexte. La logique privilegie APCA pour la perception du contraste, au-dela de simples seuils WCAG. C'est un skill de raisonnement applique, pas un package runtime integre au build.

## Coût estimé
Environ 8000 tokens pour une session couleur complete (palette + validation). Regime invocable: pertinent sur des decisions couleur structurantes, pas pour de micro-corrections texte.

## Synergies
- impeccable : apporte la direction visuelle globale, puis color-expert verrouille la dimension couleur.
- interface-design : persiste les decisions de tokens et evite les divergences chromatiques entre sessions.

## Anti-synergies / contre-indications
- A eviter pour des taches sans enjeu visuel (scripts backend, migrations de donnees) ou quand la palette est deja verrouillee contractuellement.

## Source
https://github.com/meodai/skill.color-expert — David Aerne (meodai)

## Install status
Installé chez Raphaël le 2026-05-08 sous `/root/.claude/skills/color-expert/` (skill user / plugin marketplace).

