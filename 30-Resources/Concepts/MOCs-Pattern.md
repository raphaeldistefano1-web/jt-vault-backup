---
ai_writable: true
backlinks:
- Atomic-Notes-Pattern
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-05-12
description: Stub — pattern Maps of Content (MOC) utilisés dans ce vault pour organiser
  par projet et sujet
embed_hash: null
embed_model_version: null
entities:
- vault
- pattern
- moc
id: 202605120206-mocs-pattern
intent: concept
last-accessed: 2026-05-12
project: null
status: stub
summary: Pattern MOC (Map of Content) — note hub d'entrée par projet ou sujet, structure
  d'index manuelle
tags:
- vault
- pattern
- moc
tier: warm
type: concept
updated: 2026-05-12
---

# 🗺️ MOCs Pattern

> **Stub** — Note référencée par wikilinks orphelins, à compléter.

## Définition

**Map of Content (MOC)** = note hub qui sert de point d'entrée à un projet ou à un sujet. Liste organisée de wikilinks vers les notes pertinentes, avec contexte minimal. Pattern Zettelkasten popularisé par Nick Milo (Linking Your Thinking).

## Différence MOC vs Index auto

- **MOC** : note manuelle, organisée par humain, narrative (sections, hiérarchies)
- **`_Index.md`** : note auto-générée listant toutes les notes du dossier par tier

## Convention dans ce vault

Chaque projet de `10-Projects/<slug>/` a son MOC `_MOC-<slug>.md` :
- `_MOC-pms.md`
- `_MOC-site-wordpress.md`
- `_MOC-jt-migrate.md`
- `_MOC-openclaw.md`
- `_MOC-claude-system.md`
- `_MOC-n8n.md`
- `_MOC-montage-video.md`
- `_MOC-desktop-app.md`

Plus les MOCs transversaux dans `50-MOCs/` :
- `Decisions-Log.md`, `Lessons-Learned.md`, `Stack-Tech.md`, `Hotel.md`, `PMS.md`, `Site-WordPress.md`

## Related

- [[Atomic-Notes-Pattern]]
- [[Frontmatter-Standard]]