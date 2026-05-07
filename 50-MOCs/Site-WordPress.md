---
type: moc
status: active
tags: [wordpress, site-web, moc]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Map of Content — site WordPress lejardintropical.fr (actuellement sur wp-46-202-171-204.nip.io)"
ai_writable: false
id: 202604252021-site-wordpress
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "MOC WordPress — stack Docker, theme custom, jt-booking, jt-migrate, cache 27ms, schemas LodgingBusiness."
entities: [docker, site-wordpress, wordpress]
topic_cluster: vault-navigation
intent: reference
tier: warm
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

- [[jt-booking]] — module de réservation connecté au PMS
- [[jt-migrate]] v1.2.1 — plugin de migration WP full-fidelity (similaire All-in-One WP Migration)

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
