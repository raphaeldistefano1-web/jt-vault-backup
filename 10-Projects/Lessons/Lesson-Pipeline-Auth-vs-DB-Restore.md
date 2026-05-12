---
ai_writable: true
backlinks:
- Migration-WP-com-vers-VPS-2026-04-25
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-05-12
description: Stub — restaurer une DB WP casse les sessions auth si la pipeline ne
  réinitialise pas les secret keys
embed_hash: null
embed_model_version: null
entities:
- wordpress
- auth
- migration
id: 202605120008-lesson-pipeline-auth-vs-db-restore
intent: log
last-accessed: 2026-05-12
project: Lessons
status: stub
summary: Restore DB WP casse l'auth si les secret keys / cookies ne sont pas mirorés
  ou réinitialisés
tags:
- lesson
- auth
- migration
tier: cold
type: lesson
updated: 2026-05-12
---

# Lesson Pipeline Auth vs DB Restore

> **Stub** — Note référencée par wikilinks orphelins, à compléter.

Voir [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]] qui couvre l'incident. Cette lesson capture la généralisation pour toutes les pipelines de restore (jt-migrate, backups manuels, staging→prod).

## À documenter

- [ ] Cause exacte (wp_users.session_tokens vs wp_options.auth_keys ?)
- [ ] Comportement attendu post-restore (forcer relogin vs préserver sessions)
- [ ] Step à ajouter aux pipelines (purge sessions, rotation salts)

## Related

- [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]]
- [[Lessons-Learned]]