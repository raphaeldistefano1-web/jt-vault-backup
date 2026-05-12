---
ai_writable: false
backlinks:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- 2026-05-10-ajouter-google-business-à-côté-de-tripadvisor
- 2026-05-10-avis-tripadvisor-hardcodés-pas-dynamiques
- 2026-05-10-page-hébergements-tableau-structuré-type-emplaceme
- 2026-05-10-supprimer-références-club-med-du-contenu-ljt
- 2026-05-10-tarification-hébergements-structure-95-10-volontai
- 2026-05-10-workflow-modification-contenu-multi-instances-wp
- AGENTS-md-standard
- Bug-WP-Image-Encoding-Accent
- Decision-Disable-WP-Cron-cron-Linux
- Decision-Redis-Object-Cache-Disabled
- GEO-Generative-Engine-Optimization
- Hotel
- Hotel-Le-Jardin-Tropical
- Migration-WP-com-vers-VPS-2026-04-25
- Mu-plugin-jt-seo-extras
- Mu-plugin-vs-Theme-Pattern
- Plugin-jt-booking
- Plugin-jt-migrate
- Site-Plugins-Stack-2026-04-25
- Site-WordPress-Optimisation-2026-04-25
- Stack-Tech
- Test-jt-booking-PMS-2026-04-25
- Theme-jardintropical-child
- User-Raphael-Distefano
- VPS-Hostinger
- llms-txt-standard
created: 2026-04-25
description: Map of Content — site WordPress lejardintropical.fr (actuellement sur
  wp-46-202-171-204.nip.io)
embed_hash: null
embed_model_version: null
entities:
- docker
- site-wordpress
- wordpress
id: 202604252021-site-wordpress
intent: reference
last-accessed: 2026-04-25
related:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- 2026-05-10-ajouter-google-business-à-côté-de-tripadvisor
- 2026-05-10-supprimer-références-club-med-du-contenu-ljt
- 2026-05-10-workflow-modification-contenu-multi-instances-wp
- Site-WordPress
relevance: high
status: active
summary: MOC WordPress — stack Docker, theme custom, jt-booking, jt-migrate, cache
  27ms, schemas LodgingBusiness.
tags:
- wordpress
- site-web
- moc
tier: warm
topic_cluster: vault-navigation
type: moc
updated: 2026-04-25
---

# 🌐 MOC Site WordPress

## URL et accès

- **Public** : https://wp-46-202-171-204.nip.io/
- **Admin** : https://wp-46-202-171-204.nip.io/wp-admin
- **Login** : `diphael` (cf. `/root/.jt-credentials/wordpress-instance.txt` côté VPS)
- **Domaine cible** : `lejardintropical.fr` (à migrer)

## Stack

- WordPress 6.6 / PHP 8.3 / MariaDB 11 / Apache 2.4
- Docker compose dans `/var/www/wordpress-instance/`
- Theme custom `jardintropical-child` (ultra pro, schema LodgingBusiness complet)
- 10 plugins actifs (cf. [[Stack-Tech]])
- Mu-plugin custom `jt-seo-extras.php` (~600 lignes)

## Plugins métier custom

- [[Test-jt-booking-PMS-2026-04-25|jt-booking]] — module de réservation connecté au PMS
- [[_MOC-jt-migrate|jt-migrate]] v1.2.1 — plugin de migration WP full-fidelity (similaire All-in-One WP Migration)

## Optimisations en place (2026-04-25)

- Cache WP-Optimize file-based : home **27ms warm** (gzipped 27 KB)
- Schemas étendus : LodgingBusiness, FAQPage, Offer, BreadcrumbList, TouristAttraction, TouristTrip
- Sécurité : Wordfence + 5 headers + xmlrpc/wp-config bloqués
- GEO/LLM : robots.txt LLM-aware, llms.txt, schema FAQPage
- A11y : skip-link, focus-visible, alt text 30/30
- Mobile : sticky CTA + WhatsApp button

## Reste à faire (cf. todo_raphael)

- Configurer Site Kit by Google (OAuth) — installé par user
- Wordfence wizard + 2FA
- UpdraftPlus destination (Drive/Dropbox)
- Complianz wizard (FR/UE)
- WebP bulk convert via UI
- Migrer vers domaine final lejardintropical.fr

## Décisions liées

- [[2026-04-25-migration-wp-com-vers-vps]]
- [[2026-04-25-stack-plugins-wp-2026]]

## Bugs connus theme

- Images sans `srcset` (mobile télécharge full-size)
- Logo schema URL pointe vers `lejardintropical.fr` (domaine final)
- Lien `/blog/` dans page À propos même sans blog actif

## Related

- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[Site-WordPress]] — Site-WordPress
- [[2026-05-10-supprimer-références-club-med-du-contenu-ljt]] — Supprimer références Club Med du contenu LJT
- [[2026-05-10-ajouter-google-business-à-côté-de-tripadvisor]] — Ajouter Google Business à côté de TripAdvisor
- [[2026-05-10-workflow-modification-contenu-multi-instances-wp]] — Workflow modification contenu multi-instances WP