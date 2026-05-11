---
id: vault-index
type: moc
title: "Vault Index — point d'entrée racine"
project: claude-system
status: active
summary: "MOC racine auto-régénéré. Pointe vers les projets, clusters thématiques et intents principaux."
intent: reference
tier: hot
tags: [moc, index, auto-generated, root]
ai_writable: false
auto-generated: true
updated: 2026-05-11
---

# 🗂️ Vault Index

> Auto-régénéré le **2026-05-11 04:35** par `vault-build-index`. Ne pas éditer — les modifs seront écrasées au prochain run.

Ce vault suit la structure **PARA** (Projects, Areas, Resources, Archives) + un dossier **60-Permanent** pour les insights atomiques distillés. Chaque note a un frontmatter riche (`intent`, `topic_cluster`, `tier`, `related`) parseable.

## 🔧 Projets actifs

- [[10-Projects/claude-system/_Index|claude-system]] (252 notes)
- [[10-Projects/desktop-app-electron/_Index|desktop-app-electron]] (4 notes)
- [[10-Projects/jt-migrate/_Index|jt-migrate]] (88 notes)
- [[10-Projects/montage-video/_Index|montage-video]] (0 notes)
- [[10-Projects/n8n-automations/_Index|n8n-automations]] (2 notes)
- [[10-Projects/openclaw-plugin/_Index|openclaw-plugin]] (13 notes)
- [[10-Projects/pms-jardin-tropical/_Index|pms-jardin-tropical]] (37 notes)
- [[10-Projects/site-wordpress/_Index|site-wordpress]] (51 notes)

## 🧠 Top topic clusters

### `veille-ia-youtube` (12)
- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-07-structure-répertoires-srvveille-ia-config-external]] — Structure répertoires /srv/veille-ia (config externalisée)
- [[2026-05-07-critères-filtrage-youtube-veille-ia]] — Critères filtrage YouTube veille-ia

### `pms-stack` (8)
- [[PMS-Dashboard-v2]] — PMS-Dashboard-v2
- [[_MOC-pms]] — MOC PMS Le Jardin Tropical
- [[PMS-Stack]] — PMS-Stack

### `vault-architecture` (7)
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo]] — Décision — CANONICITY.md pour déduplication vault↔mémoires CC
- [[2026-05-08-vault-para-multi-projets-chemin-canonique]] — Vault PARA multi-projets chemin canonique

### `decision-log` (7)
- [[Decisions-Log]] — Decisions-Log
- [[Decision-Redis-Object-Cache-Disabled]] — Decision-Redis-Object-Cache-Disabled
- [[Decision-Disable-WP-Cron-cron-Linux]] — Decision-Disable-WP-Cron-cron-Linux

### `bug-log` (6)
- [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]] — Bug-JT-Migrate-Auth-Loss-After-DB-Restore
- [[Bug-WP-Image-Encoding-Accent]] — Bug-WP-Image-Encoding-Accent
- [[Bug-PharData-RAM-OOM]] — Bug-PharData-RAM-OOM

### `wordpress-stack` (6)
- [[Theme-jardintropical-child]] — Theme-jardintropical-child
- [[Plugin-jt-booking]] — Plugin-jt-booking
- [[Mu-plugin-jt-seo-extras]] — Mu-plugin-jt-seo-extras

### `wp-migration` (6)
- [[Migration-WP-com-vers-VPS-2026-04-25]] — Migration-WP-com-vers-VPS-2026-04-25
- [[JT-Migrate-v1.0.0]] — JT-Migrate-v1.0.0
- [[Plugin-jt-migrate]] — Plugin-jt-migrate

### `area-hub` (5)
- [[Hotel-Le-Jardin-Tropical]] — Hotel-Le-Jardin-Tropical
- [[User-Raphael-Distefano]] — User-Raphael-Distefano
- [[Site-WordPress]] — Site-WordPress

### `vault-navigation` (4)
- [[Lessons-Learned]] — Lessons-Learned
- [[Hotel]] — Hotel
- [[PMS]] — PMS

### `general` (4)
- [[2026-04-25-session-context 2]] — 2026-04-25-session-context 2
- [[2026-04-25-session-context]] — 2026-04-25-session-context
- [[decision]] — decision

### `vps-memory` (3)
- [[2026-05-07-vps-guardrails-4-gb-swap-ollama-memorymax25g]] — VPS guardrails : 4 GB swap + Ollama MemoryMax=2.5G
- [[2026-05-08-ollama-systemd-memorymax-guardrail-et-swap]] — Ollama systemd MemoryMax guardrail et swap
- [[2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite]] — Ollama bge-m3 consomme 5.6 GB sans limite

### `vault-obsidian-infrastructure` (3)
- [[2026-05-10-config-cron-jobs-pour-curator-et-synthesizer]] — Config : Cron jobs pour curator et synthesizer
- [[2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault]] — Pattern : Scripts maintenance et diagnostic vault
- [[2026-05-10-gotcha-fichiers-temporaires-indexés-par-rag]] — Gotcha : Fichiers temporaires indexés par RAG

## 🎯 Notes par intent

### `decision` (23)
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-10-decision-defensive-truncation-et-sync-check-vault-]] — Decision : Defensive truncation et sync-check vault RAG
- [[2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo]] — Décision — CANONICITY.md pour déduplication vault↔mémoires CC

### `pattern` (20)
- [[2026-05-10-registry-pattern-centralisateur-jeux-modulaires]] — Registry pattern — centralisateur jeux modulaires
- [[2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i]] — Paralléliser tâches complexes via teams + sessions indépendantes
- [[2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe]] — Embedding model : nomic-embed-text-v2-moe (305M MoE)

### `gotcha` (15)
- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[2026-05-09-claude-max-5x-fenêtre-courte-à-réserver]] — Claude Max 5x : fenêtre courte, à réserver
- [[2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé]] — Instance C : images affichées mais absentes de la médiathèque

### `config` (11)
- [[2026-05-09-schéma-canonique-des-notes-du-vault-atomiques]] — Schéma canonique des notes du vault atomiques
- [[2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g]] — systemd override.conf pour Ollama : MemoryMax=2.5G
- [[2026-05-10-service-worker-offline-pour-pwa-cul-sec]] — Service Worker offline pour PWA CUL SEC

### `lesson` (5)
- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-10-claude-max-quota-fenêtre-5h-limitée-stratégie-rése]] — Claude Max quota — fenêtre 5h limitée, stratégie réservation

### `how-to` (12)
- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[Whisper-VPS-Reference]] — Whisper large-v3-turbo VPS — Paths, usage, performances
- [[PMS-Desktop-Pieges-Dev]] — Pièges du dev — Electron PMS Desktop

### `reference` (57)
- [[INDEX]] — INDEX racine — cerveau multi-projets
- [[Hotel-Le-Jardin-Tropical]] — Hotel-Le-Jardin-Tropical
- [[User-Raphael-Distefano]] — User-Raphael-Distefano

### `feedback-rule` (6)
- [[2026-05-09-responsive-design-obligatoire-pour-toute-interface]] — Responsive design obligatoire pour toute interface UI
- [[2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi]] — Valider systèmes de dispatch via test instances vierges
- [[2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo]] — Trier items capturés : hot (immédiat) vs warm/cold (mémoire)

### `plugin-doc` (12)
- [[color-expert]] — color-expert
- [[humanizer]] — humanizer
- [[thinking-skills]] — thinking-skills

### `concept` (11)
- [[llms-txt-standard]] — llms-txt-standard
- [[MCP-Model-Context-Protocol]] — MCP-Model-Context-Protocol
- [[Schema-FAQPage]] — Schema-FAQPage

### `log` (10)
- [[PMS-Desktop-Etat]] — Logiciel desktop PMS Le Jardin Tropical — État (Electron v1.3.0)
- [[OpenClaw-Etat]] — Plugin OpenClaw du PMS — État (avr 2026)
- [[n8n-Etat]] — n8n + Bus d'événements PMS — État (post-session 26-04)

### `monitor` (3)
- [[_FEEDBACK-PENDING]] — 📋 Feedback rules en attente — 0 rule
- [[_HEALTH]] — 🚨 Vault Health Check
- [[_RULES-APPLIED]] — 📋 Rules apprises cette semaine — 0 appliquées, 0 archivées

## 📚 Couches du vault

- **`00-Inbox/`** — captures non encore rangées. Curator (3h) déplace vers le bon projet.
- **`10-Projects/`** — un dossier par projet actif, contient ses session-logs.
- **`20-Areas/`** — domaines récurrents (dev PMS, hébergement, équipe).
- **`30-Resources/`** — références techniques réutilisables.
- **`40-Archives/`** — projets clos (rare).
- **`50-MOCs/`** — Maps of Content thématiques.
- **`60-Permanent/`** — insights atomiques distillés par le synthesizer (4h).
- **`90-Meta/`** — templates, schemas, configs internes du vault.

## ℹ️ Pour une IA qui crawl le vault

- Recherche RAG via MCP `vault` : `vault_search`, `vault_get_note`, `vault_list_recent`. Hybride BM25 + sémantique (nomic-embed-text-v2-moe).
- Tous les frontmatter incluent `intent`, `topic_cluster`, `tier`, `related`. Filtrer par ces champs avant de lire le body.
- Les notes `60-Permanent/` sont les plus denses en signal durable.
- Les notes `_*.md` sont auto-régénérées (rapports/index) — les ignorer comme contenu.
- Backlinks matérialisés dans le frontmatter `backlinks:` (régénérés par `vault-rag-backlinks`).
