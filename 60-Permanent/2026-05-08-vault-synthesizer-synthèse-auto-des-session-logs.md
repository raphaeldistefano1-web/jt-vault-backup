---
ai_writable: false
area: null
backlinks:
- 2026-05-07-haiku-pour-curation-veille-ia-économie-tokens
- 2026-05-08-frontmatter-enrichi-extrait-insights-durables
- 2026-05-09-claude-max-5x-fenêtre-courte-à-réserver
- 2026-05-09-schéma-canonique-des-notes-du-vault-atomiques
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- vault-synthesizer
- Haiku 4.5
- 60-Permanent
- session-logs
id: 20260508095955-vault-synthesizer-synthèse-auto-des-session-logs
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-08-frontmatter-enrichi-extrait-insights-durables
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault
- 2026-05-12-audit-infrastructure-claude-code-avant-multi-insta
- CANONICITY
- _Index
- _MOC-claude-system
- note-schema
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-0903-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0950-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0942-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0920-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0935-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0901-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0921-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0928-session-4d0a55cb.md
source_session: 4d0a55cb-ed1e-494e-9202-45857e2bd2b9
status: active
summary: Haiku 4.5 synthétise les logs bruts de sessions Claude Code en insights durables
  (decision/gotcha/pattern/config/lesson) toutes les 4h via cron Paris.
tags:
- permanent
- synthesized
- cron
- automation
- insight-extraction
- pipeline
tier: warm
title: Vault synthesizer — synthèse auto des session-logs
topic_cluster: vault-automation
type: permanent-note
updated: '2026-05-08'
---

**Vault synthesizer** est un cron job (exécution 4h fuseau Paris) qui distille les logs bruts de sessions Claude Code en insights atomiques typés. Il peuple `/srv/vault/60-Permanent/` avec des notes Markdown dotées de frontmatter YAML (intent, topic_cluster, tier, entities, tags, feedback_level).

**Architecture** :
- Input : logs bruts de sessions (contexte complet, commands shell, résultats)
- Agent : Haiku 4.5 (modèle léger, coût réduit, latence faible, scaling transparent)
- Output : notes atomiques evergreen prêtes pour indexation + réutilisation MCP

**Rationale du cron 4h** :
- Fraîcheur : insights à jour sans attendre fin de session
- Charge système : synthèse asynchrone, non-bloquante
- Cost/token : Haiku = faible consumption vs Opus

**Intégration au RAG** :
- Vault RAG (SQLite+vec0+FTS5+MCP) indexe ces notes en temps réel
- Recherche sémantique + lexicale sur 60-Permanent/ accessible via contexte Claude

## Related

- [[_MOC-claude-system]] — MOC Claude System — système IA personnel
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[_Index]] — Index — claude-system
- [[note-schema]] — note schema
- [[2026-05-08-frontmatter-enrichi-extrait-insights-durables]] — Frontmatter enrichi extrait insights durables
- [[2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau]] — Audit one-shot — déduplication 39 mémoires CC vs vault
- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[2026-05-10-config-cron-jobs-pour-curator-et-synthesizer]] — Config : Cron jobs pour curator et synthesizer
- [[2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault]] — Pattern : Scripts maintenance et diagnostic vault
- [[2026-05-12-audit-infrastructure-claude-code-avant-multi-insta]] — Audit infrastructure Claude Code avant multi-instance