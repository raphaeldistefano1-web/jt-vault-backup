---
ai_writable: false
area: null
backlinks:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- Site-WordPress
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- Club Med
- Page À propos
- LJT
id: 20260510040752-supprimer-références-club-med-du-contenu-ljt
intent: gotcha
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- _MOC-site-wordpress
- Site-WordPress
- Site-WordPress
- Theme-jardintropical-child
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-09-0840-session-e7718f3c.md
source_session: e7718f3c-afb1-44b0-8090-17e0d1ef32e1
status: active
summary: Contenu Club Med présent dans pages LJT (À propos, Contact, Politiques) doit
  être supprimé lors des migrations/révisions content.
tags:
- permanent
- synthesized
- content
- migration
- cleanup
- maintenance
tier: warm
title: Supprimer références Club Med du contenu LJT
topic_cluster: wp-content-cleanup
type: permanent-note
updated: '2026-05-10'
---

# Gotcha : contenu Club Med hérité

Le thème child WordPress pour LJT contient des références au Club Med dans plusieurs pages (À propos, Contact, Politiques annulation, Villa Pierro) — héritage probable d'une migration antérieure mal nettoyée.

**Problème** : ce contenu n'est PAS pertinent pour Le Jardin Tropical et crée confusion pour les visiteurs.

**Solution** : lors des audits contenu ou migrations, **supprimer systématiquement toute mention Club Med ou autres références de l'ancienne marque**.

**Pages à auditer** : page-a-propos.php, page-contact.php, page-politiques-annulation.php, page-villa-pierro.php

**Conseil** : documenter dans CLAUDE.md quels paragraphes/sections mentionnent Club Med ou autres marques obsolètes pour éviter de les refaire à chaque refonte.

## Related

- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[_MOC-site-wordpress]] — MOC Site WordPress — lejardintropical
- [[Site-WordPress]] — Site WordPress
- [[Site-WordPress]] — Site WordPress
- [[Theme-jardintropical-child]] — Theme jardintropical child