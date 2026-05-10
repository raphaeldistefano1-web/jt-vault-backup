---
ai_writable: false
backlinks:
- 2026-05-09-schéma-canonique-des-notes-du-vault-atomiques
- Frontmatter-Standard
- Vault-Setup
created: 2026-04-25
description: Pattern atomic notes pour ce vault — 1 idée = 1 note, densément liée,
  pour réduire les tokens IA
embed_hash: null
embed_model_version: null
entities:
- documentation
- reference
id: 202604252028-atomic-notes-pattern
intent: concept
last-accessed: 2026-04-25
related:
- 2026-05-08-frontmatter-enrichi-extrait-insights-durables
- '[[Frontmatter-Standard]]'
- '[[MOCs-Pattern]]'
- '[[Vault-Setup]]'
relevance: high
status: active
summary: 1 idée = 1 note. Inspiré du Zettelkasten de Niklas Luhmann + framework "Linking
  Your Thinking" LYT de Nick Milo + Andy M…
tags:
- vault
- zettelkasten
- methodology
tier: warm
topic_cluster: vault-architecture
type: concept
updated: 2026-04-25
---

# ⚛️ Atomic Notes — pattern

## Principe

**1 idée = 1 note**. Inspiré du Zettelkasten de Niklas Luhmann + framework "Linking Your Thinking" (LYT) de Nick Milo + Andy Matuschak (evergreen notes).

## Pourquoi pour les IA ?

- **Embeddings propres** : 1 concept par chunk → meilleure pertinence sémantique
- **Tokens économisés** : on ne charge que les notes pertinentes + leurs voisins directs (graph traversal) au lieu de stuffer tout le contexte
- **Réutilisation** : la même note référencée depuis plusieurs MOCs / projets sans duplication

## Conventions taille

- **200-1500 mots** par note (sweet spot pour embeddings + readability humaine)
- **< 200 mots** : embeddings deviennent bruyants, les chunks sont trop courts pour être discriminants
- **> 1500 mots** : l'IA chunke mal, perte de cohérence sémantique

## Convention nommage

- Noms **sémantiques** (pas timestamps Zettelkasten classique) : `MCP-Model-Context-Protocol.md`, `Decision-Streaming-tar-gz-vs-PharData.md`
- Préfixes pour les types : `Decision-`, `Bug-`, `Workflow-`, `Schema-`, `Plugin-`, `Theme-`, `Pattern-`
- Utiliser **kebab-case** ou **PascalCase** consistant (kebab préféré pour ce vault)

## Densité de liens (clé)

**Cible : 5-15 wikilinks par note** vers d'autres notes du vault. C'est ce qui donne la **topologie neuronale** que [[User-Raphael-Distefano|Raphaël]] cherche.

Types de liens :
- `[[Note]]` simple — référence basique
- `[[Note|alias]]` — texte affiché différent
- Frontmatter `related:` — liens "voisins" sémantiques
- Frontmatter `depends_on:` — dépendances explicites
- Frontmatter `supersedes:` — note remplace une ancienne

## Anatomie d'une bonne atomic note

```markdown
---
type: concept | decision | bug | workflow | resource | project
status: active | draft | archived
tags: [tag1, tag2]
created: 2026-04-25
updated: 2026-04-25
relevance: high | medium | low
description: "Une phrase qui résume — sera utilisée par l'IA pour classer"
ai_writable: false
related: ["[[Note1]]", "[[Note2]]"]
---

# Titre clair

## Définition / Principe
1-3 phrases qui ouvrent par la réponse directe.

## Sections...

## Liens
- [[Note voisine]]
- [[Note voisine 2]]
```

## Quand splitter une note en plusieurs

Signaux qu'une note est trop dense :
- > 1500 mots
- Plusieurs `## h2` qui pourraient être des notes autonomes
- Plusieurs concepts indépendants évoqués
- Chaque section a ses propres références sortantes

## Quand fusionner

Signaux qu'une note est trop atomique :
- < 100 mots
- Toujours lue avec une autre
- Pas de référence entrante propre

## Liens

- [[Vault-Setup]]
- [[Frontmatter-Standard]]

## Related

- [[2026-05-08-frontmatter-enrichi-extrait-insights-durables]] — Frontmatter enrichi extrait insights durables