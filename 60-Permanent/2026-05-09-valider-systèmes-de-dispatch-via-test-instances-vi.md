---
ai_writable: false
applies_to: global
area: null
auto_applied_at: 2026-05-09
backlinks:
- 2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i
- 2026-05-09-hook-dispatch-advisor-pour-suggestions-intelligent
- 2026-05-12-tester-migration-sur-instance-avec-données-réelles
- 2026-05-12-workflow-itératif-valider-par-phase-plutôt-que-bat
- _VAULT-INDEX
confidence: medium
created: '2026-05-09'
created_by: vault-synthesizer
embed_hash: null
embed_model_version: null
entities:
- dispatch_advisor
- testing
- team-agent
feedback_level: MEDIUM
id: 20260509040129-valider-systèmes-de-dispatch-via-test-instances-vi
intent: feedback-rule
last-accessed: '2026-05-09'
last_used: null
moc: null
pinned: false
project: null
proposed_rule: Avant de déclarer un système de dispatch/suggestion (hook, agent, skill)
  prêt à la production, exécuter 3-5 sessions de test sur instances vierges via team
  Agent, documenter anomalies, puis générer recommandations et ajustements.
related:
- 2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- 2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges
- 2026-05-12-workflow-itératif-valider-par-phase-plutôt-que-bat
- codex-peer-review
- devils-advocate
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1442-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1802-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1721-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1459-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1649-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1605-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1613-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1452-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1444-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1433-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1604-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1828-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1449-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1651-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1440-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1616-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1822-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1454-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1622-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1619-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1437-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1656-session-21c4cfc3.md
- 10-Projects/pms-jardin-tropical/2026-05-08-1625-session-21c4cfc3.md
source_session: 21c4cfc3-93d1-4d4d-9bab-ab7b63ed0c6a
status: auto-applied
summary: Tout nouveau système de dispatch/suggestion doit passer par test sur instances
  vierges avant déclaration stable.
tags:
- permanent
- synthesized
- feedback
- pending-review
- system-validation
- testing-discipline
tier: warm
title: Valider systèmes de dispatch via test instances vierges
topic_cluster: quality-assurance
type: permanent-note
updated: '2026-05-09'
usage_count: 0
---

Signal utilisateur explicite : 'tu fais quelques petites sessions de test de ce nouveau système... code via ton outil de team Agent pour voir si tout répond bien. après tu fais des Recommandations'.

Justification : dispatch_advisor introduit de la sophistication (regex, catalogue YAML, multi-agents). Sophistication = edge cases cachés (faux positifs de détection, suggestions non-pertinentes, interactions non-testées entre hooks).

**Protocole** :
1. Créer 3-5 instances vierges (projets différents, contextes frais)
2. Injecter le hook/agent/skill nouveau
3. Exécuter 20-30 prompts variés (design, prose, code-review, decision, debug)
4. Documenter : faux positifs, latence, crashes, suggestions non-pertinentes
5. Générer rapport + recommandations
6. Redéployer patché

**Fréquence** : avant adoption de tout nouveau système.

## Related

- [[2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i]] — Paralléliser tâches complexes via teams + sessions indépendantes
- [[codex-peer-review]] — codex peer review
- [[devils-advocate]] — devils advocate
- [[2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo]] — Trier items capturés : hot (immédiat) vs warm/cold (mémoire)
- [[2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo]] — Hiérarchie persistance : Mémoire vs Vault vs Todo
- [[2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a]] — Nouveaux skills doivent être auto-découverts par agents
- [[2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges]] — Valider systèmes de dispatch via instances vierges
- [[2026-05-12-workflow-itératif-valider-par-phase-plutôt-que-bat]] — Workflow itératif : valider par phase plutôt que batch