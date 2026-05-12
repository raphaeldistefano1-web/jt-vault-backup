---
ai_writable: true
created: 2026-05-12
description: Stub — infrastructure email Le Jardin Tropical (Brevo, Orange, DKIM/SPF/DMARC, migration domaine pro)
embed_hash: null
embed_model_version: null
entities:
- email
- brevo
- orange
- dns
id: 202605120202-email-infra
intent: reference
last-accessed: 2026-05-12
project: null
status: stub
summary: Stack email — Brevo transac PMS/WP, lejardintropical@orange.fr boîte pro (à migrer)
tags: [email, infra, hotel]
tier: warm
type: reference
updated: 2026-05-12
---

# 📧 Email Infrastructure

> **Stub** — Note référencée par wikilinks orphelins, à compléter.

## État actuel

- **Boîte pro** : `lejardintropical@orange.fr` (à migrer vers `@lejardintropical.fr` une fois le domaine acheté)
- **Transactionnel PMS/WP** : [[n8n]] et Brevo (cf. [[reference_n8n]])
- **DNS** : domaine `lejardintropical.fr` non encore acheté → DKIM/SPF/DMARC à configurer après acquisition

## À documenter

- [ ] Comparatif providers email pro (Google Workspace, Zoho, OVH MX Plan, mail-in-a-box)
- [ ] Choix retenu + raison
- [ ] Records DNS (DKIM, SPF, DMARC, MX, BIMI)
- [ ] Plan de migration depuis Orange (forwarding, archivage)
- [ ] Aliases fonctionnels (contact@, reservation@, info@)

## Related

- [[VPS-Hostinger]]
- [[Stack-Tech]]
- [[Hotel-Le-Jardin-Tropical]]
