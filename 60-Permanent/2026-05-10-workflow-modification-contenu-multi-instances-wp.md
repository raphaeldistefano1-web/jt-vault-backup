---
ai_writable: false
area: null
backlinks:
- 2026-05-09-instance-d-wordpress-en-rotation-test
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- Site-WordPress
- WP-Migration-Audit-2026-05-05
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- Instance A
- Instance C
- Instance D
- jardintropical-child
id: 20260510040750-workflow-modification-contenu-multi-instances-wp
intent: pattern
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-09-instance-d-wordpress-en-rotation-test
- _Index
- Site-WordPress
- WP-Migration-Audit-2026-05-05
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-09-0840-session-e7718f3c.md
source_session: e7718f3c-afb1-44b0-8090-17e0d1ef32e1
status: active
summary: Éditer contenu template sur instances A/C/D via fichiers PHP dans jardintropical-child,
  répliquer sur toutes instances.
tags:
- permanent
- synthesized
- wordpress
- multi-instance
- templates
tier: warm
title: Workflow modification contenu multi-instances WP
topic_cluster: wp-instances
type: permanent-note
updated: '2026-05-10'
---

# Workflow modification contenu multi-instances

Quand modifier du contenu template (pages À propos, Contact, Politiques annulation, etc.) sur instances A/C/D :

1. **Localiser le template** : `/var/www/wp-test-project/instance-{X}/data/wordpress/wp-content/themes/jardintropical-child/page-{slug}.php`
2. **Éditer via Read/Edit** : modifications atomiques au niveau template
3. **Répliquer sur instances** : A, C, et D partagent le même thème child → même template structure → copier modifs sur chaque instance
4. **Uploads separés** : images uploadées vivent dans `instance-{X}/data/wordpress/wp-content/uploads/YYYY/MM/` (année/mois), isolées par instance

**Avantage** : modification template = instantanée sur le site rendu, pas de rebuild theme. Chaque instance reste indépendante.

## Related

- [[2026-05-09-instance-d-wordpress-en-rotation-test]] — Instance D WordPress en rotation test
- [[_Index]] — Index — site-wordpress
- [[Site-WordPress]] — Site WordPress
- [[WP-Migration-Audit-2026-05-05]] — Migration WordPress — État post-audit (2026-05-05)