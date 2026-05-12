---
ai_writable: true
created: 2026-05-12
description: Index des wikilinks orphelins du vault — redirections aliases + sujets génériques à arbitrer
embed_hash: null
embed_model_version: null
entities:
- vault
- maintenance
- dangling-links
id: 202605120100-stubs-a-arbitrer
intent: log
last-accessed: 2026-05-12
project: claude-system
status: active
summary: 19 wikilinks orphelins regroupés — 9 aliases (renommages) + 10 sujets génériques à arbitrer
tags: [vault, maintenance, dangling-links]
tier: warm
type: workflow
updated: 2026-05-12
---

# Stubs à arbitrer — 2026-05-12

> **Contexte** : audit dangling wikilinks du vault. 11 stubs structurés (Bugs/Decisions/Lessons/Concepts) déjà matérialisés comme placeholders. Restent **19 wikilinks orphelins** à arbitrer manuellement.

## A. Aliases — wikilinks vers une note qui existe sous un autre nom (9) — ✅ RÉSOLU 2026-05-12

Redirections appliquées dans les notes sources (50-MOCs/PMS.md, 50-MOCs/Site-WordPress.md, 50-MOCs/Hotel.md, 20-Areas/User-Raphael-Distefano.md, 20-Areas/Hotel-Le-Jardin-Tropical.md, 20-Areas/Dev-PMS-Area.md, 30-Resources/Concepts/Robots-txt-LLM-Aware.md, 30-Resources/Whisper-VPS-Reference.md).

| Ancien wikilink (obsolète) | Cible canonique |
|---|---|
| `AI-Assistant` | [[PMS-AI-Assistant]] |
| `Calendar-v2` | [[PMS-Calendar-v2]] |
| `Dashboard-v2` | [[PMS-Dashboard-v2]] |
| `Settings-Hub` | [[PMS-Settings-Hub]] |
| `Desktop-App` | [[Desktop-App-Electron]] |
| `Workflow-Deploy` | [[Workflow-Deploy-PMS]] |
| `PMS-Area` / `Dev-PMS` | [[Dev-PMS-Area]] |
| `Decision-Robots-LLM-Aware` | [[Decision-Robots-txt-LLM-Aware]] |
| `jt-booking` | [[Test-jt-booking-PMS-2026-04-25]] |
| `jt-migrate` | [[_MOC-jt-migrate]] |
| `project_montage_video` | [[_MOC-montage-video]] |

## B. Sujets génériques — ✅ TOUS MATÉRIALISÉS 2026-05-12

Tous les sujets génériques orphelins ont été matérialisés comme placeholders à enrichir (status: stub).

- [[Hotel-Operations]] — `20-Areas/`
- [[Fournisseurs]] — `20-Areas/`
- [[Email-Infra]] — `30-Resources/`
- [[Reserve-Cousteau]] — `30-Resources/Concepts/`
- [[TODO-Site-WP]] — `10-Projects/site-wordpress/`
- [[Linux-Foundation-AAIF]] — `30-Resources/Concepts/`
- [[MOCs-Pattern]] — `30-Resources/Concepts/`
- [[Page-FAQ-2026-04-25]] — `10-Projects/site-wordpress/`
- [[Brainstorm-PMS-Ameliorations-2026-04-25]] — `10-Projects/pms-jardin-tropical/`

## C. Stubs structurés déjà créés (11)

Pour traçabilité. Ces notes sont matérialisées et taggées `status: stub`.

### Bugs
- [[Bug-Cross-Compile-Linux-MacOS]]
- [[Bug-JT-Migrate-v1.1-Import-Extract-Fail]]
- [[Bug-OpenClaw-Plugin-Sandbox]]

### Decisions
- [[Decision-Politique-Annulation]]
- [[Decision-Schema-Offer-priceValidUntil]]

### Lessons (nouveau dossier `10-Projects/Lessons/`)
- [[Lesson-Apache-Timeout-defaut-trop-court]]
- [[Lesson-mu-plugins-WP-com-toxiques-sur-standalone]]
- [[Lesson-PharData-charge-tout-en-RAM]]
- [[Lesson-Pipeline-Auth-vs-DB-Restore]]
- [[Lesson-Server-to-Server-curl-bypass-user]]

### Concepts
- [[Schema-TouristAttraction]]

## D. Faux positifs identifiés (pour mémoire, ne pas toucher)

- 8 wikilinks `[[10-Projects/<projet>/_Index]]` : path-prefixed, Obsidian résout correctement.
- ~40 wikilinks `[[2026-XX-XX-...]]` : encodage NFC/NFD macOS — fichiers existent mais bytes diffèrent.
- `[[Note]]`, `[[Note1]]`, `[[Note2]]`, `[[NN]]`, `[[Note voisine]]`, `[[Concept]]`, `[[Old-note]]`, `[[01]]` : exemples pédagogiques dans `30-Resources/Concepts/` ou syntaxe placeholder du pipeline veille IA.

## Related

- [[_VAULT-INDEX]]
- [[Atomic-Notes-Pattern]]
- [[Frontmatter-Standard]]
