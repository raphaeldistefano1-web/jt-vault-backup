---
backlinks:
- 2026-05-09-impeccable-surpasse-frontend-design-officiel
- 2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée
- _Index
- _VAULT-INDEX
category: design
consent_required: false
cost: moyen
cost_tokens_estimate: 8000
date_added: 2026-05-08
install_status: installed
intent: plugin-doc
plugin_full_name: Color Expert (meodai / David Aerne)
plugin_id: color-expert
project: claude-system
regime: invocable
related:
- 2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée
status: active
synergies:
- impeccable
- interface-design
tags:
- design
- couleur
- palette
- oklch
- apca
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

## Related

- [[2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée]] — Page à-propos : couleur fond « nos valeurs » trop foncée