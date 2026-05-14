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
updated: 2026-05-14
---

# 🗂️ Vault Index

> Auto-régénéré le **2026-05-14 04:30** par `vault-build-index`. Ne pas éditer — les modifs seront écrasées au prochain run.

Ce vault suit la structure **PARA** (Projects, Areas, Resources, Archives) + un dossier **60-Permanent** pour les insights atomiques distillés. Chaque note a un frontmatter riche (`intent`, `topic_cluster`, `tier`, `related`) parseable.

## 🔧 Projets actifs

- [[10-Projects/claude-system/_Index|claude-system]] (362 notes)
- [[10-Projects/desktop-app-electron/_Index|desktop-app-electron]] (5 notes)
- [[10-Projects/jt-migrate/_Index|jt-migrate]] (100 notes)
- [[10-Projects/montage-video/_Index|montage-video]] (0 notes)
- [[10-Projects/n8n-automations/_Index|n8n-automations]] (2 notes)
- [[10-Projects/openclaw-plugin/_Index|openclaw-plugin]] (18 notes)
- [[10-Projects/pms-jardin-tropical/_Index|pms-jardin-tropical]] (51 notes)
- [[10-Projects/site-wordpress/_Index|site-wordpress]] (53 notes)

## 🧠 Top topic clusters

### `veille-ia-youtube` (12)
- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-07-structure-répertoires-srvveille-ia-config-external]] — Structure répertoires /srv/veille-ia (config externalisée)
- [[2026-05-07-critères-filtrage-youtube-veille-ia]] — Critères filtrage YouTube veille-ia

### `vault-architecture` (8)
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo]] — Décision — CANONICITY.md pour déduplication vault↔mémoires CC
- [[2026-05-08-vault-para-multi-projets-chemin-canonique]] — Vault PARA multi-projets chemin canonique

### `pms-stack` (8)
- [[PMS-Dashboard-v2]] — PMS-Dashboard-v2
- [[_MOC-pms]] — MOC PMS Le Jardin Tropical
- [[PMS-Stack]] — PMS-Stack

### `area-hub` (7)
- [[Hotel-Le-Jardin-Tropical]] — Hotel-Le-Jardin-Tropical
- [[Fournisseurs]] — Fournisseurs
- [[User-Raphael-Distefano]] — User-Raphael-Distefano

### `decision-log` (7)
- [[Decisions-Log]] — Decisions-Log
- [[Decision-Redis-Object-Cache-Disabled]] — Decision-Redis-Object-Cache-Disabled
- [[Decision-Disable-WP-Cron-cron-Linux]] — Decision-Disable-WP-Cron-cron-Linux

### `jt-migrate` (6)
- [[2026-05-11-defensive-architecture-pour-import-fail-safe-optio]] — Defensive architecture pour import: fail-safe optional steps
- [[2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl]] — Scripts pre-cutover cleanup et post-import reenable
- [[2026-05-11-testing-vérification-obligatoires-après-chaque-éta]] — Testing + vérification obligatoires après chaque étape migration

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

### `project-culsec` (5)
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m]] — Service Worker offline PWA: stratégie cache-first + manifest
- [[2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p]] — Stack CUL SEC: Next.js 14 App Router + Framer Motion PWA offline

### `vault-navigation` (4)
- [[Lessons-Learned]] — Lessons-Learned
- [[Hotel]] — Hotel
- [[PMS]] — PMS

### `general` (4)
- [[2026-04-25-session-context 2]] — 2026-04-25-session-context 2
- [[2026-04-25-session-context]] — 2026-04-25-session-context
- [[decision]] — decision

## 🎯 Notes par intent

### `decision` (34)
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-10-decision-defensive-truncation-et-sync-check-vault-]] — Decision : Defensive truncation et sync-check vault RAG
- [[2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo]] — Décision — CANONICITY.md pour déduplication vault↔mémoires CC

### `pattern` (35)
- [[2026-05-12-cleanup-post-cutover-supprimer-plugins-temporaires]] — Cleanup post-cutover : supprimer plugins temporaires
- [[2026-05-10-registry-pattern-centralisateur-jeux-modulaires]] — Registry pattern — centralisateur jeux modulaires
- [[2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i]] — Paralléliser tâches complexes via teams + sessions indépendantes

### `gotcha` (21)
- [[2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées]] — Sudo silent failures et env vars non-appliquées
- [[2026-05-11-brevo-doi-template-erreur-redirection-url-is-missi]] — Brevo DOI template — erreur 'Redirection url is missing'
- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress

### `config` (16)
- [[2026-05-09-schéma-canonique-des-notes-du-vault-atomiques]] — Schéma canonique des notes du vault atomiques
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g]] — systemd override.conf pour Ollama : MemoryMax=2.5G

### `lesson` (11)
- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-12-audit-infrastructure-claude-code-avant-multi-insta]] — Audit infrastructure Claude Code avant multi-instance

### `how-to` (12)
- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[Whisper-VPS-Reference]] — Whisper large-v3-turbo VPS — Paths, usage, performances
- [[PMS-Desktop-Pieges-Dev]] — Pièges du dev — Electron PMS Desktop

### `reference` (60)
- [[INDEX]] — INDEX racine — cerveau multi-projets
- [[Hotel-Le-Jardin-Tropical]] — Hotel-Le-Jardin-Tropical
- [[Fournisseurs]] — Fournisseurs

### `feedback-rule` (9)
- [[2026-05-12-auto-arrêt-à-80-cpu-notification-email]] — Auto-arrêt à 80% CPU + notification email
- [[2026-05-09-responsive-design-obligatoire-pour-toute-interface]] — Responsive design obligatoire pour toute interface UI
- [[2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi]] — Valider systèmes de dispatch via test instances vierges

### `log` (21)
- [[_STUBS-A-ARBITRER-2026-05-12]] — _STUBS-A-ARBITRER-2026-05-12
- [[PMS-Desktop-Etat]] — Logiciel desktop PMS Le Jardin Tropical — État (Electron v1.3.0)
- [[OpenClaw-Etat]] — Plugin OpenClaw du PMS — État (avr 2026)

### `concept` (15)
- [[Reserve-Cousteau]] — Reserve-Cousteau
- [[Schema-TouristAttraction]] — Schema-TouristAttraction
- [[llms-txt-standard]] — llms-txt-standard

### `plugin-doc` (12)
- [[color-expert]] — color-expert
- [[humanizer]] — humanizer
- [[thinking-skills]] — thinking-skills

### `monitor` (3)
- [[_FEEDBACK-PENDING]] — 📋 Feedback rules en attente — 0 rule
- [[_HEALTH]] — 🚨 Vault Health Check
- [[_RULES-APPLIED]] — 📋 Rules apprises cette semaine — 6 appliquées, 0 archivées

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
