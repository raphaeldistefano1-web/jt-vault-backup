---
ai_writable: false
backlinks:
- 2026-05-10-accès-données-hbook-source-unique-de-vérité
- 2026-05-10-avis-tripadvisor-hardcodés-pas-dynamiques
- 2026-05-10-page-hébergements-tableau-structuré-type-emplaceme
- 2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp
- 2026-05-10-tarification-hébergements-structure-95-10-volontai
- _Index
- _MOC-site-wordpress
created: 2026-04-25
description: Review complète + tests batterie de la connexion jt-booking ↔ PMS — clé
  API régénérée, 1 bug theme fixé, Stripe à configurer pour finaliser
embed_hash: null
embed_model_version: null
entities:
- api
- booking
- pms
- site-wordpress
- wordpress
id: 202604252130-test-jt-booking-pms-2026-04-25
intent: reference
last-accessed: 2026-04-25
project: site-wordpress
related:
- 2026-05-10-accès-données-hbook-source-unique-de-vérité
- 2026-05-10-avis-tripadvisor-hardcodés-pas-dynamiques
- 2026-05-10-page-hébergements-tableau-structuré-type-emplaceme
- 2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp
- 2026-05-10-tarification-hébergements-structure-95-10-volontai
- '[[PMS-Stack]]'
- '[[Plugin-jt-booking]]'
- '[[Site-WordPress]]'
- '[[Theme-jardintropical-child]]'
relevance: high
status: completed
summary: 1. Régénération clé API WordPress côté PMS script scripts/regen-wp-key.ts
  — précédente perdue/inaccessible
tags:
- jt-booking
- pms
- test
- integration
tier: hot
topic_cluster: wordpress-stack
type: project
updated: 2026-04-25
---

# 🧪 Test connexion jt-booking ↔ PMS — 2026-04-25

## Setup réalisé

1. **Régénération clé API WordPress** côté PMS (script `scripts/regen-wp-key.ts`) — précédente perdue/inaccessible
2. **Configuration plugin WP** : `pms_url` + `api_key` mis dans `jt_booking_settings`
3. **Recréation pages plugin** : pages 312/313/314 (Merci/Annulation/Composer) avaient été supprimées au cleanup post-import. `JT_Booking_Endpoints::ensure_pages()` recrée → IDs 321/322/323
4. **Test connexion** : `JT_Booking_Settings::test_connection()` → "OK — 5 type(s) d'hébergement reçus"

## Endpoints PMS testés

| Endpoint | Status | Notes |
|---|---|---|
| `GET /api/public/rooms/types` | ✅ | 5 types renvoyés (bungalow_std×10, bungalow_junior, villa_mado, villa_pierreo, villa_creole) |
| `GET /api/public/search` | ✅ | 5 résultats avec dispo + prix + total |
| `GET /api/public/availability` | ✅ | Prix breakdown : nightly, total, taxAmount, totalWithTax, depositAmount 20%, balanceDue |
| `GET /api/public/availability-calendar` | ✅ | Format `{unavailable: [], totalRooms: 10}` (liste les jours indisponibles uniquement) |
| `GET /api/public/booking/status?token=...` | ✅ | 404 sur token fake (comportement attendu) |
| `POST /api/public/booking/intent` | ⚠️ | Crée bien la résa en DB (PENDING WEBSITE) MAIS retourne 500 sur création Stripe Checkout (Stripe pas configuré) |
| `POST /api/public/booking-group/intent` | non testé | Même bloquage Stripe attendu |
| Rate limit booking/intent | ✅ | 10 req/min puis 429 — protection en place |

## Bugs trouvés et corrigés

### Bug 1 — type="junior" dans theme `page-bungalow-junior.php`
**Fichier** : `wp-content/themes/jardintropical-child/page-bungalow-junior.php:641`

**Avant** :
```php
<?php echo do_shortcode( '[jt_book type="junior"]' ); ?>
```

**Après** :
```php
<?php echo do_shortcode( '[jt_book type="bungalow_junior"]' ); ?>
```

**Impact** : la page `/bungalow-junior/` affichait un encadré rouge "Shortcode JT Booking invalide — Type inconnu : junior. Types acceptés : bungalow_std, bungalow_junior, villa_mado, villa_pierreo, villa_creole." → 0 widget réservation visible pour le client.

### Bug 2 — Pages doublons booking (302/303)
Lors du cleanup post-import on avait supprimé les pages 312/313/314 mais oublié 302/303 (Merci pour votre réservation, Réservation annulée — slugs originaux). Ces pages étaient orphelines (le plugin pointait vers 321/322 après recréation).

**Fix** : `wp post delete 302 303 --force`

## Architecture observée

```
WordPress (jt-booking v1.0.4)              PMS Next.js
─ post_content vide pour pages          ─ /api/public/rooms/types
  bungalows/villas/réservation          ─ /api/public/search
─ Theme custom utilise des              ─ /api/public/availability
  page-{slug}.php avec do_shortcode()   ─ /api/public/availability-calendar
─ Templates :                            ─ /api/public/booking/intent
   page-bungalows.php                    ─ /api/public/booking/status
   page-bungalow-junior.php              ─ /api/public/booking-group/intent
   page-villa-mado.php
   page-villa-pierro.php                Auth header : X-JT-API-Key
   page-villa-creole.php                Storage : Integration WORDPRESS
   page-reservation.php                          (encryptedCreds AES-256-GCM)
─ AJAX proxy /wp-admin/admin-ajax.php   ─ Cron cleanup-pending pour
  ?action=jt_proxy → ajoute clé API       résas orphelines PENDING
  côté serveur (jamais en JS client)
```

## État final

- ✅ Plugin actif, connecté au PMS via clé API régénérée
- ✅ 6/6 pages booking (bungalows, bungalow-junior, villa-mado, villa-pierro, villa-creole, réservation) rendent le widget sans erreur
- ✅ Booking intent crée la résa en DB côté PMS
- ✅ Cron cleanup-pending nettoie les orphelines automatiquement
- ❌ **Stripe non configuré** → impossible de finaliser le checkout (BLOQUANT prod)

## Action user requise

**Configurer Stripe** côté PMS via `/dashboard/settings/integrations` :
- `STRIPE_SECRET_KEY` (sk_test_... pour tester, sk_live_... pour prod)
- `STRIPE_PUBLISHABLE_KEY` (pk_test_... / pk_live_...)
- `STRIPE_WEBHOOK_SECRET` (whsec_... — récup depuis Stripe Dashboard → Webhooks)

Sans ça, tout le reste de la chaîne marche mais le client ne peut pas payer.

## Liens

- [[Plugin-jt-booking]]
- [[PMS-Stack]]
- [[Site-WordPress]]
- [[Theme-jardintropical-child]]
- [[Workflow-API-Integrations]]

## Related

- [[2026-05-10-tarification-hébergements-structure-95-10-volontai]] — Tarification hébergements : structure 95 + 10€ volontaire
- [[2026-05-10-accès-données-hbook-source-unique-de-vérité]] — Accès données HBook — source unique de vérité
- [[2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp]] — Signaler impacts jt-booking avant clôture tâche WP
- [[2026-05-10-avis-tripadvisor-hardcodés-pas-dynamiques]] — Avis TripAdvisor hardcodés, pas dynamiques
- [[2026-05-10-page-hébergements-tableau-structuré-type-emplaceme]] — Page hébergements : tableau structuré (Type | Emplacement | Prix/Saison)