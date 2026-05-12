---
ai_writable: false
area: null
backlinks:
- 2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé
- 2026-05-10-structure-paths-uploads-wordpress-instance-acd
- 2026-05-10-workflow-modification-contenu-multi-instances-wp
- 2026-05-12-tester-migration-sur-instance-avec-données-réelles
- Decisions-Log
- Plugin-jt-migrate
- WP-Migration-Audit-2026-05-05
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- Instance D
- wordpress
id: 20260509040516-instance-d-wordpress-en-rotation-test
intent: config
last-accessed: '2026-05-09'
moc: null
project: null
related:
- 2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé
- 2026-05-10-structure-paths-uploads-wordpress-instance-acd
- 2026-05-10-workflow-modification-contenu-multi-instances-wp
- 2026-05-12-tester-migration-sur-instance-avec-données-réelles
- Decisions-Log
- Mu-plugin-jt-seo-extras
- WP-Migration-Audit-2026-05-05
- _Index
- _MOC-jt-migrate
schema_version: 1
source_notes:
- 10-Projects/site-wordpress/2026-05-08-1132-session-e7718f3c.md
source_session: e7718f3c-afb1-44b0-8090-17e0d1ef32e1
status: active
summary: Instance D (4e instance test) modifiée en parallèle d'A/C. À ajouter au registre
  des instances actives.
tags:
- permanent
- synthesized
- wp-test-project
- multi-instances
- docker
tier: warm
title: Instance D WordPress en rotation test
topic_cluster: wp-test-project
type: permanent-note
updated: '2026-05-09'
---

Session révèle utilisation d'une **Instance D** en plus des instances A (clone NEW), B (sauvegarde OVH figée), C (sandbox migration). Instance D reçoit mêmes modifications que A/C (pages enfants jardintropical-child, suppression contenu Club Med).

**Chemins** : `/var/www/wp-test-project/instance-d/` (même pattern que A/C/D). Statut/rôle d'Instance D non explicité—clarifier si c'est une 4e instance de test parallèle ou une rotation temporaire.

**Action** : Mettre à jour `reference_wp_test_project.md` pour inclure Instance D dans le registre (avec statut/port/rôle).

## Related

- [[WP-Migration-Audit-2026-05-05]] — Migration WordPress — État post-audit (2026-05-05)
- [[_Index]] — Index — site-wordpress
- [[_MOC-jt-migrate]] — MOC JT-Migrate Plugin
- [[Decisions-Log]] — Decisions Log
- [[Mu-plugin-jt-seo-extras]] — Mu plugin jt seo extras
- [[2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé]] — Instance C : images affichées mais absentes de la médiathèque
- [[2026-05-10-workflow-modification-contenu-multi-instances-wp]] — Workflow modification contenu multi-instances WP
- [[2026-05-10-structure-paths-uploads-wordpress-instance-acd]] — Structure paths uploads WordPress (Instance A/C/D)
- [[2026-05-12-tester-migration-sur-instance-avec-données-réelles]] — Tester migration sur instance avec données réelles, pas vierge