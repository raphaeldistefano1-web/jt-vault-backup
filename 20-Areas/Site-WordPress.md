---
ai_writable: false
created: 2026-04-25
description: Area site WordPress — vitrine + booking, optimisé en profondeur le 2026-04-25
embed_hash: null
embed_model_version: null
entities:
- docker
- site-wordpress
- wordpress
id: 202604252024-site-wordpress
intent: reference
last-accessed: 2026-04-25
related:
- 2026-05-10-page-hébergements-tableau-structuré-type-emplaceme
- 2026-05-10-supprimer-références-club-med-du-contenu-ljt
- 2026-05-10-tarification-hébergements-structure-95-10-volontai
- '[[Migration-WP-com-vers-VPS-2026-04-25]]'
- '[[Mu-plugin-jt-seo-extras]]'
- '[[Plugin-jt-booking]]'
- '[[Plugin-jt-migrate]]'
- '[[Site-WordPress-Optimisation-2026-04-25]]'
- '[[Theme-jardintropical-child]]'
relevance: high
status: active
summary: Site WordPress optimisé LodgingBusiness — Docker Apache/PHP/MariaDB, theme
  custom, mu-plugin SEO, TTFB 33ms.
tags:
- wordpress
- site-web
tier: hot
topic_cluster: area-hub
type: area
updated: 2026-04-25
---

# 🌐 Site WordPress

## URL et accès

- **Public** : https://wp-46-202-171-204.nip.io/
- **Admin** : https://wp-46-202-171-204.nip.io/wp-admin
- **Login admin** : `diphael` (cf. `/root/.jt-credentials/wordpress-instance.txt`)
- **Domaine cible** : `lejardintropical.fr` (à migrer)

## Stack

- WordPress 6.6 + PHP 8.3 + MariaDB 11 + Apache 2.4
- Docker compose : `/var/www/wordpress-instance/`
- Theme : [[Theme-jardintropical-child]] (custom, ultra pro)
- 10 plugins actifs (cf. [[Site-Plugins-Stack-2026-04-25]])
- Mu-plugin : [[Mu-plugin-jt-seo-extras]] (~600 lignes)

## Composants spécifiques

- [[Plugin-jt-booking]] v1.0.4 — module de réservation custom
- [[Plugin-jt-migrate]] v1.2.1 — plugin migration custom (similaire All-in-One WP Migration)

## Pages publiques (22, 17 dans sitemap)

**Indexées (17)** :
- Accueil, Les Bungalows, Bungalow Junior Family
- Villa Mad'O, Villa Pierre'O, Villa Créole
- [[Reserve-Cousteau|Réserve Cousteau]]
- Activités, Restauration, Galerie
- Réservation, Contact, Infos pratiques
- À propos, Politiques d'annulation
- Nos hébergements, FAQ

**Noindex (5)** :
- Mentions légales, Politique de confidentialité, CGV
- Merci pour votre réservation, Réservation annulée

## Métriques performance

- **TTFB cached** : 33-58 ms (avant optim : ~1170 ms)
- **Home gzipped** : 27 KB
- **0 broken links** sur 441 vérifiés
- **DB total** : 5.17 MB / autoload 0.044 MB

## Décisions clés

- [[Decision-Mu-plugin-vs-RankMath]] — préférer mu-plugin custom au plugin SEO commercial
- [[Decision-Streaming-tar-gz-vs-PharData]] — bug v1.0.0 du jt-migrate
- [[Decision-Redis-Object-Cache-Disabled]] — conflit avec WP-Optimize
- [[Decision-Robots-txt-LLM-Aware]] — stratégie GEO

## Bugs connus theme (à signaler au dev)

- Images sans `srcset` (mobile télécharge full-size)
- Logo schema URL hardcoded vers `lejardintropical.fr`
- Lien `/blog/` dans page À propos même sans blog actif (mitigé via redirect 301 mu-plugin)

## Reste à faire (cf. [[TODO-Site-WP]])

- Configurer Site Kit by Google (OAuth user)
- Wordfence wizard + 2FA
- UpdraftPlus destination
- Complianz wizard
- WebP bulk convert via UI
- Migrer domaine final
- Décision blog GO/NO-GO
- Décision bilingue FR/EN

## Related

- [[2026-05-10-tarification-hébergements-structure-95-10-volontai]] — Tarification hébergements : structure 95 + 10€ volontaire
- [[2026-05-10-supprimer-références-club-med-du-contenu-ljt]] — Supprimer références Club Med du contenu LJT
- [[2026-05-10-page-hébergements-tableau-structuré-type-emplaceme]] — Page hébergements : tableau structuré (Type | Emplacement | Prix/Saison)