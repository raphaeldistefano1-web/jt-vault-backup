---
type: concept
status: active
tags: [vault, frontmatter, conventions]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Standard YAML frontmatter pour toutes les notes du vault — IA-readable et Obsidian Bases-compatible"
ai_writable: false
related:
  - "[[Atomic-Notes-Pattern]]"
  - "[[Vault-Setup]]"
---

# 📋 Frontmatter — standard du vault

## Champs obligatoires

```yaml
---
type: ?
status: ?
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
relevance: ?
description: ""
ai_writable: false
---
```

## Vocabulaires contrôlés

### `type:` (obligatoire, 1 valeur)
- `note` — note libre
- `area` — responsabilité continue (PARA Areas)
- `project` — projet avec deadline (PARA Projects)
- `resource` — référence (docs, contacts, configs)
- `concept` — pattern, théorie, standard
- `decision` — décision technique (ADR-style)
- `bug` — bug rencontré + résolution + leçon
- `meeting` — compte rendu réunion
- `moc` — Map of Content
- `daily` — journal quotidien

### `status:` (obligatoire)
- `active` — en cours d'utilisation/dev
- `draft` — pas finalisé
- `archived` — dormant, ne plus utiliser
- `proposed` — pour decisions
- `accepted` — pour decisions
- `superseded` — pour decisions remplacées

### `relevance:` (obligatoire)
- `high` — note centrale, citée souvent
- `medium` — utile mais pas critique
- `low` — référence ponctuelle

### `tags:` (au moins 1)
- Vocabulaire libre mais discipline : préférer **tags existants** avant d'en créer
- Tags principaux : `hotel`, `pms`, `wordpress`, `dev`, `ia`, `geo`, `seo`, `security`, `perf`, `decision`, `bug`, `lesson`

## Champs optionnels

```yaml
related:        # liste de wikilinks vers notes voisines
  - "[[Note1]]"
  - "[[Note2]]"
depends_on:     # dépendances explicites (cette note présuppose ces autres)
  - "[[Concept]]"
supersedes:     # cette note remplace une ancienne
  - "[[Old-note]]"
aliases:        # autres noms pour cette note (Obsidian le respecte)
  - "Synonyme"
context:        # 1 phrase de mise en contexte
chosen:         # pour decisions
alternatives:   # pour decisions
---
```

## Convention `description:` (critique pour IA)

Une **phrase complète** qui résume la note. Sera utilisée par les LLMs pour classer la pertinence sans avoir à lire la note entière. Économie de tokens substantielle.

Exemples :
- ❌ "Plugin"
- ✅ "Plugin WordPress de migration full-fidelity v1.2.1, streaming tar.gz, conflit connu avec Redis Object Cache"

## Convention dates

- Format **ISO** `YYYY-MM-DD`
- `created:` ne change jamais
- `updated:` à actualiser à chaque modif
- IAs doivent ignorer notes avec `updated >` 6 mois sauf demande explicite (mitigation drift)

## Liens

- [[Atomic-Notes-Pattern]]
- [[Vault-Setup]]
