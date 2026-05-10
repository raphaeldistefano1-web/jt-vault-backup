---
ai_writable: false
alternatives:
- Akismet payant
- Cloudflare Turnstile
- CleanTalk
backlinks:
- Decisions-Log
- Site-Plugins-Stack-2026-04-25
- Site-WordPress-Optimisation-2026-04-25
- _MOC-site-wordpress
chosen: Antispam Bee (gratuit, RGPD-pur)
context: Optim site WP 2026-04-25 — Akismet en place mais licence commerciale exigée
created: 2026-04-25
description: Akismet retiré (licence commerciale), remplacé par Antispam Bee (gratuit
  + RGPD-friendly)
embed_hash: null
embed_model_version: null
entities:
- akismet
- antispam-bee
- site-wordpress
id: 202604252037-decision-akismet-vers-antispam-bee
intent: decision
last-accessed: 2026-04-25
project: Decisions
related:
- '[[Site-Plugins-Stack-2026-04-25]]'
relevance: medium
status: accepted
summary: Akismet était installé sur le site WP migré depuis dealmfr. Akismet est gratuit
  pour usage personnel mais payant pour us…
tags:
- decision
- wordpress
- antispam
- rgpd
tier: warm
topic_cluster: decision-log
type: decision
updated: 2026-04-25
---

# 🎯 Decision : Akismet → Antispam Bee

## Contexte

Akismet était installé sur le site WP migré depuis dealmfr. Akismet est **gratuit pour usage personnel** mais **payant pour usage commercial** (50$/mois minimum pour un site d'hôtel).

## Options considérées

### A. Garder Akismet payant
- ❌ 50$/mois récurrent
- ⚠️ Données envoyées à Automattic (US) — RGPD touchy

### B. **Antispam Bee (gratuit, RGPD-pur)** ✅
- ✅ 100% gratuit
- ✅ Maintenu par pluginkollektiv (DE)
- ✅ **Zéro backend externe** : tout en local, aucune donnée ne sort
- ✅ RGPD by design
- ✅ Filtres heuristiques + DNSBL Spamhaus

### C. Cloudflare Turnstile
- ✅ Gratuit, anti-bot
- ❌ CAPTCHA UX dans formulaires (friction)
- Intéressant en complément, pas en remplacement

### D. CleanTalk
- ❌ Payant, pas RGPD-friendly

## Choix : **B**

## Rationale

- Pas de licence à gérer
- RGPD-clean (important pour un site français commercial)
- Maintenu activement (~500k installs, rating 4.6)
- Aucun conflit connu

## Configuration appliquée

```php
[
  'regexp_check' => 1,
  'spam_ip' => 1,
  'already_commented' => 1,
  'dnsbl_check' => 1,        // Spamhaus
  'country_code' => 1,
  'dont_track_user' => 1,    // RGPD
  'cronjob_enable' => 1,
  'cronjob_interval' => 7,
  // ...
]
```

## Liens

- [[Site-Plugins-Stack-2026-04-25]]