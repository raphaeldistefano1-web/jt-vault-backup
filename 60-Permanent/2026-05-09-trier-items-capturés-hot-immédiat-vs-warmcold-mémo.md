---
ai_writable: false
applies_to: global
area: null
auto_applied_at: 2026-05-09
backlinks:
- 2026-05-08-frontmatter-enrichi-extrait-insights-durables
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
- 2026-05-12-mémoire-claude-accumule-sans-archivage-audit-pério
- 2026-05-12-workflow-itératif-valider-par-phase-plutôt-que-bat
confidence: medium
created: '2026-05-09'
created_by: vault-synthesizer
embed_hash: null
embed_model_version: null
entities:
- priorité
- mémorisation
- triage
feedback_level: MEDIUM
id: 20260509040209-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
intent: feedback-rule
last-accessed: '2026-05-09'
last_used: null
moc: null
pinned: false
project: null
proposed_rule: 'Quand capturant des infos/décisions, respecter le tier proposé par
  l''utilisateur : hot (actionner immédiatement, ajouter todo), warm (mémoriser, relire
  1-2 semaines), cold (archive). Ne pas traiter cold comme hot (waste motionnel).'
related:
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16
- 2026-05-12-mémoire-claude-accumule-sans-archivage-audit-pério
- 2026-05-15-qa-hygiene-serveur-next-local
- CANONICITY
- TODO-centralized
- note-schema
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1726-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1811-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1821-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1832-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1753-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1823-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1755-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1732-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1758-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1736-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1743-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1809-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1825-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1750-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1827-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1802-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1740-session-96ce7c71.md
source_session: 96ce7c71-9b8d-45c1-a608-8a8a0cffb777
status: auto-applied
summary: Certains items doivent être actionnés immédiatement (hot/todo), d'autres
  gardés en mémoire pour plus tard (warm/cold). Respecter le tier proposé par l'utilisateur.
tags:
- permanent
- synthesized
- feedback
- pending-review
- triage
- action
- mémorisation
tier: warm
title: 'Trier items capturés : hot (immédiat) vs warm/cold (mémoire)'
topic_cluster: knowledge-management
type: permanent-note
updated: '2026-05-09'
usage_count: 0
---

Signal observé : "tu peux le faire tout de suite. Pour le reste, garde en mémoire."

## Tier hot
- Action immédiate demandée explicitement
- Impact urgent (deadlines, blockers, infrastructure)
- À ajouter à todo_raphael.md avec priorité HIGH
- Exécuter cette session ou après

## Tier warm
- Contexte à mémoriser mais pas urgent
- Ajouter à Mémoire Claude ou Vault
- Relifter proactivement dans 1-2 semaines ou quand contexte resurface
- Exemples : décisions archi, apprentissages, configs

## Tier cold
- Archive, support uniquement si contexte resurface
- Rester accessible mais ne pas relifter proactivement
- Exemples : anciennes décisions supersédées, contexte historique

## Application
Quand l'utilisateur dit "fais X maintenant, garde Y en mémoire" : respecter ce tri, ne pas élever cold en priorité par zèle.

## Related

- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-09-anti-pattern-redonder-info-du-contexte-injecté]] — Anti-pattern : redonder info du contexte injecté
- [[TODO-centralized]] — TODO centralized
- [[note-schema]] — note schema
- [[2026-05-09-3-régimes-dintégration-plugin-distincts]] — 3 régimes d'intégration plugin distincts
- [[2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau]] — Audit one-shot — déduplication 39 mémoires CC vs vault
- [[2026-05-10-analyse-métier-valider-source-de-données-réelle]] — Analyse métier — valider source de données réelle
- [[2026-05-12-hydration-mismatch-418-avec-zustand-nextjs-16]] — Hydration mismatch (#418) avec Zustand + Next.js 16
- [[2026-05-12-mémoire-claude-accumule-sans-archivage-audit-pério]] — Mémoire Claude accumule sans archivage — audit périodique requis
- [[2026-05-15-qa-hygiene-serveur-next-local]] — 2026-05-15-qa-hygiene-serveur-next-local