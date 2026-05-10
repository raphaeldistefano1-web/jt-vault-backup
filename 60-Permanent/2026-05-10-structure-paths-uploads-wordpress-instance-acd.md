---
ai_writable: false
area: null
backlinks:
- 2026-05-09-instance-d-wordpress-en-rotation-test
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- Bug-WP-Image-Encoding-Accent
- Mu-plugin-jt-seo-extras
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- uploads
- Instance A
- Instance C
- Instance D
id: 20260510040754-structure-paths-uploads-wordpress-instance-acd
intent: config
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- 2026-05-09-instance-d-wordpress-en-rotation-test
- Bug-WP-Image-Encoding-Accent
- Mu-plugin-jt-seo-extras
- _Index
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-09-0840-session-e7718f3c.md
source_session: e7718f3c-afb1-44b0-8090-17e0d1ef32e1
status: active
summary: Images uploadées dans `/var/www/wp-test-project/instance-{X}/data/wordpress/wp-content/uploads/YYYY/MM/`
  (année/mois, par instance).
tags:
- permanent
- synthesized
- wordpress
- paths
- filesystem
tier: warm
title: Structure paths uploads WordPress (Instance A/C/D)
topic_cluster: wp-config
type: permanent-note
updated: '2026-05-10'
---

# Paths uploads WordPress

## Structure standard

```
/var/www/wp-test-project/instance-{A|C|D}/data/wordpress/wp-content/uploads/
├── 2026/
│   ├── 04/  ← images d'avril 2026
│   ├── 05/  ← images de mai 2026
│   └── ...
```

Chaque instance a son propre répertoire uploads isolé.

## Diagnostic d'images

Pour localiser une image (ex: `bungalow_exterieur_jardin-tropical_01`) :

```bash
ls /var/www/wp-test-project/instance-c/data/wordpress/wp-content/uploads/2026/04/ | grep -i 'bungalow'
```

**Note importante** : WordPress génère automatiquement des thumbnails avec suffixes `-WIDTHxHEIGHT.ext`. Pour trouver le fichier original, filtrer via `grep -v '\-[0-9]\+x[0-9]\+\.'` pour exclure les variantes dimensionnelles.

## Related

- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[2026-05-09-instance-d-wordpress-en-rotation-test]] — Instance D WordPress en rotation test
- [[Bug-WP-Image-Encoding-Accent]] — Bug WP Image Encoding Accent
- [[Mu-plugin-jt-seo-extras]] — Mu plugin jt seo extras
- [[_Index]] — Index — site-wordpress