---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- AGENTS
- Atomic-Notes-Pattern
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- frontmatter
- YAML
- intent
- tier
- atomicity
id: 20260508040101-frontmatter-enrichi-extrait-insights-durables
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related:
- note-schema
- 2026-05-09-schéma-canonique-des-notes-du-vault-atomiques
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- AGENTS
schema_version: 1
source_notes:
- 10-Projects/openclaw-plugin/2026-05-07-1325-session-158ff0de.md
- 10-Projects/openclaw-plugin/2026-05-07-1340-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1433-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1532-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1446-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1520-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1437-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1307-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1513-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1551-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1655-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1549-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1517-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1420-session-158ff0de.md
- 10-Projects/pms-jardin-tropical/2026-05-07-1459-session-158ff0de.md
source_session: 158ff0de-03dd-41ec-927d-9cb29780c3d1
status: active
summary: Notes vault avec frontmatter intent+tier pour extraction auto d'insights
  durables.
tags:
- permanent
- synthesized
- metadata
- evergreen
- extraction-auto
- classification
tier: warm
title: Frontmatter enrichi extrait insights durables
topic_cluster: vault-notes
type: permanent-note
updated: '2026-05-08'
---

Enrichir frontmatter YAML de chaque note avec champs structurés :

```yaml
---
title: Titre lisible
intent: decision|gotcha|pattern|config|lesson
topic_cluster: slug-domaine
tier: hot|warm|cold
entities: [service1, file2]
tags: [tag1, tag2]
---
```

**Champs** :
- `intent` : type de savoir (décision technique, piège, recette, config, apprentissage)
- `tier` : fraîcheur (hot = dernière semaine, warm = 1-6 mois, cold = historique)

**Avantages** :
- Recherche par intent (« gotchas Ollama »)
- Classement par fraîcheur
- Extraction auto pour MEMORY.md

Chaque note = atomique (1 concept), evergreen (6+ mois), lisible hors contexte, inclut le POURQUOI.

## Related

- [[note-schema]] — note schema
- [[2026-05-09-schéma-canonique-des-notes-du-vault-atomiques]] — Schéma canonique des notes du vault atomiques
- [[2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs]] — Vault synthesizer — synthèse auto des session-logs
- [[2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo]] — Trier items capturés : hot (immédiat) vs warm/cold (mémoire)
- [[AGENTS]] — AGENTS