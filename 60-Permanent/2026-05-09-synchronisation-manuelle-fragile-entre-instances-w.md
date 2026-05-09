---
ai_writable: false
area: null
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- Instance A
- Instance C
- Instance D
id: 20260509040517-synchronisation-manuelle-fragile-entre-instances-w
intent: gotcha
last-accessed: '2026-05-09'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/site-wordpress/2026-05-08-1132-session-e7718f3c.md
source_session: e7718f3c-afb1-44b0-8090-17e0d1ef32e1
status: active
summary: Chaque changement de contenu (pages enfants) doit être répété manuellement
  dans 3+ instances. Risque haut de désynchronisation.
tags:
- permanent
- synthesized
- wp-test-project
- architecture
- content-sync
- maintenance-burden
tier: warm
title: Synchronisation manuelle fragile entre instances WordPress
topic_cluster: wp-test-project
type: permanent-note
updated: '2026-05-09'
---

Architecture multi-instances (A/C/D) force **réplication manuelle du contenu** sur chaque modification :
- Session : suppression "Club Med" = 5 fichiers × 3 instances = 15 edits
- Pages synchronisées : `page-a-propos.php`, `page-contact.php`, `page-politiques-annulation.php`, `page-villa-pierro.php`
- Chemins : `/var/www/wp-test-project/instance-[A|C|D]/data/wordpress/wp-content/themes/jardintropical-child/page-*.php`

**Piège** : facile d'oublier une instance lors d'une modification. Pas de trigger automatique de sync.

**Mitigation potentielle** : script de validation (vérifier contenu identique sur A/C/D pour pages clés) ou webhook post-save → copie auto entre instances.