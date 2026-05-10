---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- 2026-05-09-adr-template-et-pattern-docsadr
- INDEX
- _VAULT-INDEX
- note-schema
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- components/games/registry.ts
- ActionVerite
- Paranoia
- Roulette
id: 20260510040511-registry-pattern-centralisateur-jeux-modulaires
intent: pattern
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- note-schema
- INDEX
- 2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a
- 2026-05-09-adr-template-et-pattern-docsadr
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0114-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: Registry.ts centralise tous les jeux (type, composant, metadata) pour ajouter
  rapidement de nouvelles variantes.
tags:
- permanent
- synthesized
- pattern
- modular-design
- extensibility
- registry
tier: warm
title: Registry pattern — centralisateur jeux modulaires
topic_cluster: culsec-architecture
type: permanent-note
updated: '2026-05-10'
---

**Pattern** : fichier `components/games/registry.ts` qui exporte un objet centralisateur de tous les jeux avec : clé (gameId), composant React, metadata (nom FR, min/max joueurs, durée, catégorie).

**Bénéfice** : ajouter un nouveau jeu = créer le composant + ajouter 1 ligne dans registry. Pas besoin de refactorer routing. Catalog page consomme directement le registry.

**Implémentation** : voir `/var/www/culsec/components/games/registry.ts`.

## Related

- [[2026-05-08-vault-para-multi-projets-chemin-canonique]] — Vault PARA multi-projets chemin canonique
- [[note-schema]] — note schema
- [[INDEX]] — INDEX racine — cerveau multi-projets
- [[2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a]] — Nouveaux skills doivent être auto-découverts par agents
- [[2026-05-09-adr-template-et-pattern-docsadr]] — ADR template et pattern docs/adr/