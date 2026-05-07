---
id: 20260507-1122-wp-migration
type: project
title: Migration WordPress — État post-audit (2026-05-05)
project: jt-migrate
area: null
status: active
confidence: high
summary: Migration OVH(Divi) → NEW(theme custom) livrée sur Instance C. HBook 1120 résas, theme bugs fixés, 4 mu-plugins créés, 3 findings critiques résolus.
intent: log
entities: [wordpress, hbook, migration, instance-c, theme-custom, mu-plugins]
topic_cluster: jt-migrate
related: ["[[_MOC-jt-migrate]]"]
moc: "[[_MOC-jt-migrate]]"
source: "memory:project_wp_migration.md"
tier: hot
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07
embed_model_version: null
embed_hash: null
tags: [wordpress, hbook, migration]
ai_writable: true
---

# Migration WordPress — État post-audit

> Note portée depuis la mémoire Claude Code `project_wp_migration.md` le 2026-05-07.

## État au 2026-05-06 (Instance C = brouillon prod final)

Raphaël migre l'ancien site OVH (`www.lejardintropical.fr`, theme Divi 4.27.4, 1120 résas HBook) vers le nouveau site (production `https://wp-46-202-171-204.nip.io`, theme custom `jardintropical-child`).

**Migration effective réalisée le 2026-05-06 sur Instance C** (`https://wp-c-46-202-171-204.nip.io/`) qui devient le brouillon de la future prod. Approche retenue : **HBook greffé sur le NEW propre** (Instance C re-clonée depuis Instance A puis HBook + 4 plugins greffés).

## Greffe HBook réussie sur C

- 1120 résas migrées (975 confirmed + 144 cancelled + 1 new)
- 1097 customers, 2227 email logs, 5 CPT hb_accommodation (IDs 2809/2811/2813/2815/2817 préservés)
- **0 résa orpheline** (FK accom_id intacte)
- Plugin HBook 2.1.6 actif, license `be20a3ed-...` valide
- `hb_invoice_counter_next_value=165` préservé (légal FR)
- `hb_ical_url_feed_key=ETKLLV53LFWT7BJ` préservé (URLs OTAs)
- 174 options hb_* importées + 4 hb_stripe_* WIPÉES définitivement

## Theme bugs fixés

- 3 occurrences `accommodation="X"` → `accom_id="X"` dans `functions.php` (le bon attribute HBook)
- 5 templates page-*.php : `[jt_book type="X"]` (cassé) → `jt_hbook_form( HBOOK_ID_X )` (helper du theme)
- `page-reservation.php` : `[jt_book_search]` → `[hb_accommodation_list]`
- `inc/hbook-constants.php` : 5 placeholders → vrais IDs
- `availableLanguage: ['Français', 'Anglais']` → `['Français']` (décision Raphaël monolingue)

## Plugins ajoutés sur C

- **wp-mail-smtp 4.8.0** + config Brevo importée (mailer=sendinblue, key xkeysib-..., from=contact@lejardintropical.com) — **bloqué par whitelist IP Brevo** (action manuelle Raphaël requise)
- **review-widgets-for-tripadvisor 13.2.7** + 14 options trustindex-* importées (subscription-id 05499654g, page-details Bouillante, style 12) — placement widget à finaliser

## Mu-plugins créés sur C (4 actifs au total)

- `jt-seo-extras.php` (existing, 600+ lignes, theme NEW)
- **`jt-sandbox-c.php`** (nouveau, 2.5KB) : filter wp_mail redirige tout vers raphael.distefano1@gmail.com + `pre_option_hb_stripe_*` filter force `no`/`test` à la lecture + admin banner SANDBOX
- **`jt-contact-form.php`** (nouveau, 7KB) : endpoint REST `/wp-json/jt/v1/contact` + JS handler qui clone le form pour neutraliser le preventDefault decoratif. Honeypot, rate limit 5 req/10min/IP, X-Forwarded-For pour Traefik, strip CRLF anti header-injection.
- **`jt-hbook-redesign.php`** (nouveau, 16KB, 2026-05-06) : restyle le rendu de `[hb_accommodation_list]` en split layout style "herberg" du theme A. Filter PHP `do_shortcode_tag` swap les images server-side, JS promote thumb-link au niveau du grid, CSS inline 266 lignes (badges, prix flottants, eyebrow script, hover lift).

## Bugs HBook découverts et fixés (2026-05-06)

1. **placeholder_escape hash** dans 70 strings de wp_hb_strings + 5 email_templates + 1 document_template + hb_resa_invoice_id : `{HASH}placeholder` au lieu de `%placeholder`. Fix : `REPLACE({HASH}, %)` global.
2. **.hb-clearfix display:none trop large** : cachait aussi les containers internes du booking form HBook → fix scoper à `> .hb-clearfix` direct child.
3. **Split layout HBook** : `.hb-thumbnail-link` est nested dans `.hb-accom-listing-desc`, donc le grid 2 cols sur le wrapper ne fonctionne pas → JS doit promote le link au niveau direct du wrapper.

## Photos finales HBook (post-cleanup)

4 attachments B (IDs 2709/2739/2773/2781) + 116 fichiers `/uploads/2023/12/` supprimés le 2026-05-06. Les 5 thumbnails actuels viennent à 100% d'Instance A :
- 2809 Bungalow Simple → `bungalow_chambre_style-contemporain_01.webp`
- 2811 Junior Family → `bungalow-junior_exterieur_facade_01.webp`
- 2813 Villa Pierre O → `Le_Jardin_Tropical-26-sur-69.webp`
- 2815 Villa Créole → `villa-creole_exterieur_terrasse-piscine_01.webp`
- 2817 Villa Mad O → `villa-mado_exterieur_terrasse-mer_01.webp`

## Audit pré-migration (2026-05-05) en référence

Livrables d'audit dans `/var/www/wp-test-project/` :

- `SYNTHESE-AUDIT.md` (17 KB, 247 l) — comparatif OLD vs NEW + plan migration 8 phases (~20h sur 3-5 jours) — **fichier principal**
- `audit-instance-b.md` (280 l) — ancien site
- `audit-production.md` (397 l) — nouveau site
- `audit-hbook.md` (522 l) — deep-dive HBook + Section K = checklist migration actionnable
- `audit-bloat-keys.md` (287 l) — bloat (957 MB) + API keys (Stripe LIVE, Brevo, Divi)

## 3 findings critiques (résolus)

1. **Nouveau site : booking CASSÉ** — `/reservation/` 0 `<form>`, `jt-booking-v1.0.4` ne rend que des placeholders, CPT `jt_hebergement` vide. **RÉSOLU avec HBook 2.1.6 sur Instance C.**
2. **Nouveau site : formulaire contact = placeholder décoratif** — `e.preventDefault()` sans handler, messages perdus silencieusement. **RÉSOLU avec mu-plugin `jt-contact-form.php`.**
3. **Ancien site : 957 MB de bloat dans `uploads/jt-migrate/`** + 15 MB révisions + 23 tables orphelines + Stripe LIVE actif sur le clone test. **RESOLVED avec cleanup Instance C.**

## Décisions Phase 0 en attente (Raphaël)

Toutes ces décisions doivent être prises AVANT de commencer la migration final vers prod — elles changent radicalement le plan :

- [ ] **Booking engine** : installer HBook 2.1.6 sur le NEW (recommandé vu 1120 résas existantes) OU finir/débugger `jt-booking-v1.0.4` ?
- [ ] **Formulaire contact** : CF7 ? WPForms ? endpoint AJAX custom dans le mu-plugin (sur le modèle §19 newsletter Brevo) ?
- [ ] **i18n** : ajouter Polylang/WPML/TranslatePress sur le NEW (le schema annonce "fr,en"), ou rester monolingue FR (et retirer "Anglais" du schema) ?
- [ ] **Avis TripAdvisor** : porter `review-widgets-for-tripadvisor` sur le NEW, ou intégrer schema `Review`/`AggregateRating` custom ?
- [ ] **Sender email** : unifier sur `lejardintropical@orange.fr` ou `contact@lejardintropical.com` ?
- [ ] **Plugin SMTP** : choisir UN seul (wp-mail-smtp ou easy-wp-smtp) avec Brevo

## Risques majeurs à anticiper

1. **URLs iCal vers OTAs** : changement de domaine = casse Airbnb/Booking.com — préparer le mapping AVANT, mettre à jour juste après DNS switch
2. **Compteur facture `hb_invoice_counter_next_value`** : préservation OBLIGATOIRE (loi FR contre les doublons de numéros)
3. **License HBook CodeCanyon** nominative au domaine — re-validation Maestrel possible si changement
4. **Données RGPD** : 1120 résas + 1097 customers + 2227 email logs — dump à traiter avec confidentialité

## API keys détectées (à gérer pendant la migration)

- **Stripe LIVE** : Clés WIPÉES localement le 2026-05-06 sur Instance B + Instance C. Les vraies clés vivent sur OVH (prod live, intacte) et dans le dashboard Stripe.
- **Brevo API v3** présente en 3 copies → garder une seule
- **License Divi** → **devient obsolète** sur le NEW (theme custom) → révoquer
- **iCal feed key hbook** (15 ch.) → **préserver** sinon URLs OTAs cassent
- **License HBook CodeCanyon** (`hb_purchase_code` 36 ch.) → préserver

## Liens
- MOC parent : [[_MOC-jt-migrate]]
- Source : `memory:project_wp_migration.md`
