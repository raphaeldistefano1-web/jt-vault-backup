---
ai_writable: false
area: null
backlinks:
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-responsive-design-obligatoire-pour-toute-interface
- 2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- culsec
- MOC
- UI redesign
- design specs
id: 20260512040710-refonte-visuelle-non-fialisée-vs-moc-du-projet-cul
intent: lesson
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- _RULES-APPLIED
- 2026-05-09-responsive-design-obligatoire-pour-toute-interface
schema_version: 1
source_notes:
- 10-Projects/pms-jardin-tropical/2026-05-12-0207-session-0d81ecb1.md
source_session: 0d81ecb1-2006-4cb3-ad96-6d7224a30db7
status: active
summary: 'Refonte UI incomplète a ignoré plusieurs éléments visuels du MOC : certains
  composants/states n''ont pas été retravaillés selon les specs initiales.'
tags:
- permanent
- synthesized
- design-validation
- visual-specs
- incomplete-refactor
tier: warm
title: Refonte visuelle non-fialisée vs MOC du projet culsec
topic_cluster: culsec-ui-design
type: permanent-note
updated: '2026-05-12'
---

Lors d'une refonte visuelle, il est critique de **valider chaque page/composant contre le MOC visuel avant de déclarer le travail terminé**.

Dans culsec, des éléments du MOC (layout, spacing, couleurs, states visuels) n'ont pas été assez respectés lors de la refonte précédente. Cela a laissé des incohérences : certaines pages mélangent ancien et nouveau style, certains états manquent (hover, active, disabled).

**À l'avenir** : Avant de finaliser une refonte UI, faire un diff visuel page-par-page contre le MOC (screenshots, checklist). Marquer chaque élément comme "Respecte MOC" ou "Diverge intentionnellement (raison documentée)". Ne pas merger sans validation visuelle.

## Related

- [[2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée]] — Page à-propos : couleur fond « nos valeurs » trop foncée
- [[2026-05-09-anti-pattern-redonder-info-du-contexte-injecté]] — Anti-pattern : redonder info du contexte injecté
- [[2026-05-09-3-régimes-dintégration-plugin-distincts]] — 3 régimes d'intégration plugin distincts
- [[_RULES-APPLIED]] — 📋 Rules apprises cette semaine — 6 appliquées, 0 archivées
- [[2026-05-09-responsive-design-obligatoire-pour-toute-interface]] — Responsive design obligatoire pour toute interface UI