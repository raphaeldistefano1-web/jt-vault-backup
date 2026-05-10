---
ai_writable: false
applies_to: global
area: null
auto_applied_at: 2026-05-09
backlinks:
- 2026-05-09-hook-dispatch-advisor-pour-suggestions-intelligent
- 2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi
- 2026-05-10-registry-pattern-centralisateur-jeux-modulaires
- 2026-05-10-service-worker-offline-pour-pwa-cul-sec
- 2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges
- Sub-agents-internes-PMS
- elements-of-style
- impeccable
confidence: medium
created: '2026-05-09'
created_by: vault-synthesizer
embed_hash: null
embed_model_version: null
entities:
- agents
- skills
- auto-discovery
feedback_level: MEDIUM
id: 20260509040323-nouveaux-skills-doivent-être-auto-découverts-par-a
intent: feedback-rule
last-accessed: '2026-05-09'
last_used: null
moc: null
pinned: false
project: null
proposed_rule: Les agents doivent auto-découvrir les skills disponibles via le registry
  (file-based ou API) au lieu d'une liste statique à mettre à jour manuellement.
related:
- 2026-05-09-hook-dispatch-advisor-pour-suggestions-intelligent
- 2026-05-10-service-worker-offline-pour-pwa-cul-sec
- 2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges
- Sub-agents-internes-PMS
- elements-of-style
- humanizer
- impeccable
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1021-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-1034-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-1013-session-4d0a55cb.md
- 10-Projects/pms-jardin-tropical/2026-05-08-1007-session-4d0a55cb.md
source_session: 4d0a55cb-ed1e-494e-9202-45857e2bd2b9
status: auto-applied
summary: Quand un nouveau skill est ajouté au registry, les agents doivent le découvrir
  automatiquement sans mise à jour manuelle de liste.
tags:
- permanent
- synthesized
- feedback
- pending-review
- automation
- developer-experience
tier: warm
title: Nouveaux skills doivent être auto-découverts par agents
topic_cluster: agents-skills-registry
type: permanent-note
updated: '2026-05-09'
usage_count: 0
---

Raphaël ajouta explicitement que lors de l'ajout de nouveaux skills au fil du temps, il souhaite que les agents les détectent **automatiquement** sans intervention manuelle. Actuellement, quand un skill est créé/enregistré, il faut éditer à la main une liste de skills disponibles dans chaque agent ou dans une configuration centralisée.

**Pattern souhaité** : système auto-découverte (registry + watcher, ou introspection du répertoire `/usr/local/bin/`) plutôt que liste statique.

**Applies to** : agents Anthropic officiels + agents projet PMS.

## Related

- [[Sub-agents-internes-PMS]] — Sub agents internes PMS
- [[impeccable]] — impeccable
- [[2026-05-09-hook-dispatch-advisor-pour-suggestions-intelligent]] — Hook dispatch_advisor pour suggestions intelligentes
- [[humanizer]] — humanizer
- [[elements-of-style]] — elements of style
- [[2026-05-10-service-worker-offline-pour-pwa-cul-sec]] — Service Worker offline pour PWA CUL SEC
- [[2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges]] — Valider systèmes de dispatch via instances vierges