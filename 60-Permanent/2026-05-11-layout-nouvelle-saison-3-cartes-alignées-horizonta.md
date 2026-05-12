---
ai_writable: false
area: null
backlinks:
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- Frontmatter-Standard
- Theme-jardintropical-child
- Workflow-Cross-Feature-Coherence
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- wp-test-project
- jardintropical-child theme
id: 20260511211532-layout-nouvelle-saison-3-cartes-alignées-horizonta
intent: pattern
last-accessed: '2026-05-11'
moc: null
project: null
related:
- Theme-jardintropical-child
- Workflow-Cross-Feature-Coherence
- Frontmatter-Standard
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-1820-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1941-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1841-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1811-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1911-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1938-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1713-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1853-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1716-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1933-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1907-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-0951-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1858-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1932-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1928-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-0934-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1848-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1828-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1920-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1821-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1843-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1829-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1818-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1902-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1717-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-0915-session-0375ba09.md
- 10-Projects/site-wordpress/2026-05-10-0911-session-0375ba09.md
source_session: 0375ba09-478d-4743-8890-c82a03938fb1
status: active
summary: 3 cases saison doivent être sur une ligne, pas empilées.
tags:
- permanent
- synthesized
- layout
- css
- ui-constraint
tier: warm
title: Layout 'nouvelle saison' — 3 cartes alignées horizontalement
topic_cluster: wp-frontend-layout
type: permanent-note
updated: '2026-05-11'
---

Section 'nouvelle saison' : les 3 cartes doivent s'afficher côte-à-côte sur une seule ligne horizontale, non empilées en 2+1.

Constrainte CSS/grid : appliquer `grid-template-columns: repeat(3, 1fr)` ou flexbox avec `flex-wrap: nowrap` sur le conteneur parent. Tester responsiveness mobile (peut wrap sur petit écran, acceptable).

## Related

- [[Theme-jardintropical-child]] — Theme jardintropical child
- [[Workflow-Cross-Feature-Coherence]] — Workflow Cross Feature Coherence
- [[Frontmatter-Standard]] — Frontmatter Standard