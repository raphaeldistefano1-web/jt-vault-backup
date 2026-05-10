---
ai_writable: false
applies_to: global
area: null
auto_applied_at: 2026-05-09
backlinks:
- 2026-05-09-impeccable-surpasse-frontend-design-officiel
- 2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa
- 2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée
- _VAULT-INDEX
confidence: medium
created: '2026-05-09'
created_by: vault-synthesizer
embed_hash: null
embed_model_version: null
entities:
- responsive-design
- CSS
- UX
- mobile
feedback_level: MEDIUM
id: 20260509040245-responsive-design-obligatoire-pour-toute-interface
intent: feedback-rule
last-accessed: '2026-05-09'
last_used: null
moc: null
pinned: false
project: null
proposed_rule: Toute interface doit être responsive et testée sur 375px, 768px, 1024px+.
  Valider via Chrome devtools mobile AVANT déclaré terminé.
related:
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- 2026-05-09-impeccable-surpasse-frontend-design-officiel
- 2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa
- 2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée
- Workflow-Preview-Then-Apply
- impeccable
- interface-design
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1625-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1345-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1433-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1359-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1401-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1326-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1426-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1325-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1807-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1342-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1422-session-d31950cd.md
source_session: d31950cd-6d46-47f9-aab9-3167d0bc3628
status: auto-applied
summary: Toute interface doit être responsive et s'adapter intelligemment à écrans
  petits. Pas de layouts cassés sur mobile/tablet.
tags:
- permanent
- synthesized
- feedback
- pending-review
- ux
- adaptability
- mobile-first
tier: warm
title: Responsive design obligatoire pour toute interface UI
topic_cluster: ui-design
type: permanent-note
updated: '2026-05-09'
usage_count: 0
---

Raphaël a exprimé frustration : 'ça ne s'adapte pas, je peux pas tout voir, il faudrait qu'il rétrécisse si l'écran est plus petit'. Règle absolue : chaque composant UI/dashboard/form/modal testable sur 375px (mobile), 768px (tablet), 1024px+ (desktop). Utiliser CSS flexbox/grid adaptable, jamais fixed widths ou overflows cassés. Validation obligatoire : ouvrir Chrome devtools mode mobile AVANT de déclarer terminé. Pattern récurrent sur tous projets (PMS, WP, designs).

## Related

- [[impeccable]] — impeccable
- [[2026-05-09-impeccable-surpasse-frontend-design-officiel]] — Impeccable surpasse frontend-design officiel
- [[interface-design]] — interface design
- [[Workflow-Preview-Then-Apply]] — Workflow Preview Then Apply
- [[2026-05-09-3-régimes-dintégration-plugin-distincts]] — 3 régimes d'intégration plugin distincts
- [[2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée]] — Page à-propos : couleur fond « nos valeurs » trop foncée
- [[2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa]] — Carousel HBook : boutons surdimensionnés et mal espacés