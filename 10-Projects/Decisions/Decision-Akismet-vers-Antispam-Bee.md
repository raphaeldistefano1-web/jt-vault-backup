---
type: decision
status: accepted
tags: [decision, wordpress, antispam, rgpd]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Akismet retiré (licence commerciale), remplacé par Antispam Bee (gratuit + RGPD-friendly)"
ai_writable: false
related:
  - "[[Site-Plugins-Stack-2026-04-25]]"
context: "Optim site WP 2026-04-25 — Akismet en place mais licence commerciale exigée"
chosen: "Antispam Bee (gratuit, RGPD-pur)"
alternatives: ["Akismet payant", "Cloudflare Turnstile", "CleanTalk"]
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
