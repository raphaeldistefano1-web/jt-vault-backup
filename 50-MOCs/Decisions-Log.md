---
type: moc
status: active
tags: [decisions, moc, log]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "MOC chronologique des décisions techniques majeures du projet Le Jardin Tropical"
ai_writable: false
related:
  - "[[INDEX]]"
  - "[[Lessons-Learned]]"
id: 202604252040-decisions-log
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "MOC décisions techniques — streaming tar.gz, mu-plugin vs RankMath, robots.txt LLM-aware, anti-spam RGPD."
entities: [akismet, antispam-bee, llm, migration, site-wordpress, wordpress]
topic_cluster: decision-log
intent: decision
tier: warm
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
