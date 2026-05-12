---
ai_writable: false
backlinks:
- 2026-05-09-instance-d-wordpress-en-rotation-test
- 2026-05-10-claude-max-quota-fenêtre-5h-limitée-stratégie-rése
- 2026-05-11-audit-migration-wp-phase-0-7-décisions-en-attente
- 2026-05-11-utiliser-ultrareview-avant-merge-de-changements-pl
- 2026-05-11-wp-optimize-minify-décision-de-désactivation-insta
- INDEX
- Lessons-Learned
- _MOC-pms
- _VAULT-INDEX
- note-schema
created: 2026-04-25
description: MOC chronologique des décisions techniques majeures du projet Le Jardin
  Tropical
embed_hash: null
embed_model_version: null
entities:
- akismet
- antispam-bee
- llm
- migration
- site-wordpress
- wordpress
id: 202604252040-decisions-log
intent: decision
last-accessed: 2026-04-25
related:
- 2026-04-25-session-context 2
- 2026-05-09-instance-d-wordpress-en-rotation-test
- 2026-05-11-audit-migration-wp-phase-0-7-décisions-en-attente
- 2026-05-11-wp-optimize-minify-décision-de-désactivation-insta
- '[[INDEX]]'
- '[[Lessons-Learned]]'
relevance: high
status: active
summary: MOC décisions techniques — streaming tar.gz, mu-plugin vs RankMath, robots.txt
  LLM-aware, anti-spam RGPD.
tags:
- decisions
- moc
- log
tier: warm
topic_cluster: decision-log
type: moc
updated: 2026-04-25
---

# 🎯 MOC Decisions Log

## 2026-04-25 (session migration WP + optimisation)

### Migration & infrastructure

- [[Decision-Streaming-tar-gz-vs-PharData]] — refonte JT Migrate pour scaler en RAM
- [[Decision-Disable-WP-Cron-cron-Linux]] — fiabiliser les cron WordPress

### Plugins & SEO

- [[Decision-Mu-plugin-vs-RankMath]] — pas de plugin SEO commercial, mu-plugin custom
- [[Decision-Akismet-vers-Antispam-Bee]] — anti-spam RGPD-friendly gratuit
- [[Decision-Robots-txt-LLM-Aware]] — stratégie GEO bloquer training / autoriser retrieval
- [[Decision-Redis-Object-Cache-Disabled]] — Redis désactivé suite conflit WP-Optimize

## Patterns décisionnels récurrents

### "Custom mu-plugin > plugin commercial"

Quand le theme fait déjà bien son boulot, ne PAS installer un plugin tiers qui voudrait écraser. Pattern documenté dans [[Mu-plugin-vs-Theme-Pattern]].

### "Streaming > tout-en-mémoire"

Pour tout traitement de gros volume (archives, exports DB, image batch), préférer le streaming chunké même si plus de code à écrire. Cf. [[Decision-Streaming-tar-gz-vs-PharData]].

### "Tools self-hosted > SaaS payant"

Pour ce site, le ratio coût/bénéfice penche systématiquement vers du self-hosted ou gratuit (Antispam Bee, mu-plugin custom, Smart Connections local) plutôt que des plans SaaS payants (Akismet, Rank Math Pro, Yoast Premium).

## Liens

- [[INDEX]]
- [[Lessons-Learned]]
- [[Site-WordPress-Optimisation-2026-04-25]]

## Related

- [[2026-05-09-instance-d-wordpress-en-rotation-test]] — Instance D WordPress en rotation test
- [[2026-04-25-session-context 2]] — 2026-04-25-session-context 2
- [[2026-05-11-wp-optimize-minify-décision-de-désactivation-insta]] — WP-Optimize Minify — décision de désactivation Instance C
- [[2026-05-11-audit-migration-wp-phase-0-7-décisions-en-attente]] — Audit migration WP Phase 0 — 7 décisions en attente