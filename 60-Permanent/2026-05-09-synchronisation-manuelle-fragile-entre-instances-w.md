---
ai_writable: false
area: null
backlinks:
- 2026-05-10-avis-tripadvisor-hardcodés-pas-dynamiques
- 2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa
- 2026-05-10-edit-échoue-si-classifieur-indispo-retry-résout
- 2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé
- 2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp
- 2026-05-10-structure-paths-uploads-wordpress-instance-acd
- 2026-05-10-supprimer-références-club-med-du-contenu-ljt
- 2026-05-12-mcp-reconnect-workflow-mcp-oauth-browser
- 2026-05-12-services-pausable-durgence-docker-systemd-inventor
- Mu-plugin-jt-seo-extras
- Plugin-jt-migrate
- Site-WordPress
- WP-Migration-Audit-2026-05-05
- _VAULT-INDEX
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
related:
- 2026-05-10-avis-tripadvisor-hardcodés-pas-dynamiques
- 2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa
- 2026-05-10-edit-échoue-si-classifieur-indispo-retry-résout
- 2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé
- 2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp
- 2026-05-10-structure-paths-uploads-wordpress-instance-acd
- 2026-05-10-supprimer-références-club-med-du-contenu-ljt
- 2026-05-10-workflow-modification-contenu-multi-instances-wp
- 2026-05-12-mcp-reconnect-workflow-mcp-oauth-browser
- 2026-05-12-services-pausable-durgence-docker-systemd-inventor
- Mu-plugin-jt-seo-extras
- Plugin-jt-migrate
- Site-WordPress
- _Index
- _MOC-jt-migrate
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

## Related

- [[_Index]] — Index — site-wordpress
- [[Mu-plugin-jt-seo-extras]] — Mu plugin jt seo extras
- [[Plugin-jt-migrate]] — Plugin jt migrate
- [[_MOC-jt-migrate]] — MOC JT-Migrate Plugin
- [[Site-WordPress]] — Site WordPress
- [[2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé]] — Instance C : images affichées mais absentes de la médiathèque
- [[2026-05-10-edit-échoue-si-classifieur-indispo-retry-résout]] — Edit échoue si classifieur indispo, retry résout
- [[2026-05-10-supprimer-références-club-med-du-contenu-ljt]] — Supprimer références Club Med du contenu LJT
- [[2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa]] — Carousel HBook : boutons surdimensionnés et mal espacés
- [[2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp]] — Signaler impacts jt-booking avant clôture tâche WP
- [[2026-05-10-avis-tripadvisor-hardcodés-pas-dynamiques]] — Avis TripAdvisor hardcodés, pas dynamiques
- [[2026-05-10-workflow-modification-contenu-multi-instances-wp]] — Workflow modification contenu multi-instances WP
- [[2026-05-10-structure-paths-uploads-wordpress-instance-acd]] — Structure paths uploads WordPress (Instance A/C/D)
- [[2026-05-12-mcp-reconnect-workflow-mcp-oauth-browser]] — MCP reconnect workflow : /mcp + OAuth browser
- [[2026-05-12-services-pausable-durgence-docker-systemd-inventor]] — Services pausable d'urgence — Docker + systemd inventory