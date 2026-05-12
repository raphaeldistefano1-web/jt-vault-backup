---
ai_writable: true
backlinks:
- 2026-05-12-cleanup-post-cutover-supprimer-plugins-temporaires
- Migration-WP-com-vers-VPS-2026-04-25
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-05-12
description: Stub — mu-plugins hérités de WordPress.com peuvent casser un site WP
  standalone après migration
embed_hash: null
embed_model_version: null
entities:
- wordpress
- mu-plugins
- migration
id: 202605120006-lesson-mu-plugins-wp-com-toxiques-standalone
intent: log
last-accessed: 2026-05-12
project: Lessons
status: stub
summary: mu-plugins WP.com hérités via migration → toxiques sur instance standalone,
  à purger
tags:
- lesson
- migration
- wordpress
tier: cold
type: lesson
updated: 2026-05-12
---

# Lesson mu-plugins WP.com toxiques sur standalone

> **Stub** — Note référencée par wikilinks orphelins, à compléter.

Contexte : migration `dealmfr.wpcomstaging.com` → VPS Hostinger. Les mu-plugins hérités de l'environnement WordPress.com (jetpack-related, atomic, sync) sont actifs sur l'instance standalone mais y déclenchent des erreurs / fuites perf.

## À documenter

- [ ] Liste des mu-plugins WP.com hérités à purger
- [ ] Méthode de purge (suppression vs neutralisation)
- [ ] Validation post-purge

## Related

- [[Site-WordPress-Optimisation-2026-04-25]]
- [[Lessons-Learned]]