---
type: moc
status: active
tags: [index, root, moc]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "INDEX racine du vault — entry point pour humains et IA, navigation par couches"
ai_writable: false
---

# 🧠 INDEX — Cerveau Le Jardin Tropical

> Vault Obsidian pour [[User-Raphael-Distefano|Raphaël]]. Mémoire unifiée pour Claude / ChatGPT / Gemini / Cursor / Claude Code via [[MCP-Model-Context-Protocol|MCP]] + [[AGENTS-md-standard|AGENTS.md]].
>
> Initialisé 2026-04-25.

## 🚀 Quickstart pour une IA qui débarque

1. Lire **[[AGENTS.md]]** (= CLAUDE.md) — orientation 30s
2. Lire ce fichier ([[INDEX]]) — navigation par couche
3. Choisir la **MOC pertinente** selon la question
4. Charger **uniquement les notes nécessaires** (atomic notes 200-1500 mots)

## 🗺️ MOCs (Maps of Content)

Les MOCs sont des **hubs neuraux** — entry points par sujet. Lire la MOC d'abord, charger les notes liées **à la demande**.

| MOC | Sujet | Liens |
|---|---|---|
| [[Hotel]] | Hôtel Le Jardin Tropical (business, capacité, services) | 🌺 |
| [[PMS]] | PMS Next.js custom (dev, archi, état) | 💻 |
| [[Site-WordPress]] | Site WP (vitrine, booking, optims, plugins) | 🌐 |
| [[Stack-Tech]] | Stack technique transversale (VPS, ports, paths) | 🔧 |
| [[Decisions-Log]] | Toutes les décisions techniques (chronologique) | 🎯 |
| [[Lessons-Learned]] | Apprentissages transversaux | 💡 |

## 👤 Identité

- [[User-Raphael-Distefano]] — profil utilisateur, préférences IA
- [[Workflow-Collaboration-IA]] — comment Raphaël collabore avec ses IA

## 🛏️ Areas (PARA)

Responsabilités continues, pas de deadline :

- [[Hotel-Le-Jardin-Tropical]]
- [[Dev-PMS-Area]]
- [[Site-WordPress]]
- [[Workflow-Collaboration-IA]]

## 🚧 Projects (PARA)

### PMS

- [[PMS-Stack]]
- [[PMS-Dashboard-v2]]
- [[PMS-Calendar-v2]]
- [[PMS-Settings-Hub]]
- [[PMS-AI-Assistant]]
- [[Desktop-App-Electron]]
- [[Plugin-OpenClaw]]

### Site Web

- [[Site-WordPress-Optimisation-2026-04-25]] — 3 loops d'optim (perf+SEO+sec+a11y)
- [[Theme-jardintropical-child]]
- [[Mu-plugin-jt-seo-extras]]
- [[Site-Plugins-Stack-2026-04-25]]
- [[Plugin-jt-booking]]

### JT Migrate

- [[Plugin-jt-migrate]] (v1.2.1 active)
- [[Migration-WP-com-vers-VPS-2026-04-25]]
- [[JT-Migrate-v1.0.0]] → [[JT-Migrate-v1.1.0]] → [[JT-Migrate-v1.2.0]] → [[JT-Migrate-v1.2.1]]

### Decisions (chronologique)

- [[Decision-Mu-plugin-vs-RankMath]]
- [[Decision-Streaming-tar-gz-vs-PharData]]
- [[Decision-Redis-Object-Cache-Disabled]]
- [[Decision-Robots-txt-LLM-Aware]]
- [[Decision-Akismet-vers-Antispam-Bee]]
- [[Decision-Disable-WP-Cron-cron-Linux]]

### Bugs / Lessons

- [[Bug-PharData-RAM-OOM]] → leçon : `PharData` pas scalable, streaming USTAR custom
- [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]] → leçon : pipelines doivent ordonner les modifs auth-affecting EN DERNIER
- [[Bug-Apache-Timeout-300-vs-Uploads]] → leçon : Apache default Timeout=300 tue les gros uploads
- [[Bug-Redis-WPO-Advanced-Cache-Conflict]] → leçon : drop-ins WP mutuellement exclusifs
- [[Bug-WP-Image-Encoding-Accent]] → leçon : symlink quand search-replace ne trouve pas
- [[Bug-WP-Link-Blog-404]] → leçon : `parse_request` > `template_redirect` pour 404 redirects

## 📚 Resources

### Concepts / Standards

- [[MCP-Model-Context-Protocol]]
- [[AGENTS-md-standard]]
- [[llms-txt-standard]]
- [[GEO-Generative-Engine-Optimization]]
- [[Schema-org-LodgingBusiness]]
- [[Schema-FAQPage]]
- [[Robots-txt-LLM-Aware]]
- [[Mu-plugin-vs-Theme-Pattern]]
- [[Atomic-Notes-Pattern]]
- [[Frontmatter-Standard]]

### Workflows

- [[Workflow-Preview-Then-Apply]]
- [[Workflow-Deploy-PMS]]
- [[Workflow-API-Integrations]]
- [[Workflow-Cross-Feature-Coherence]]
- [[Workflow-File-Share-Uploads]]

### Stack & Infra

- [[Stack-Tech]]
- [[VPS-Hostinger]]
- [[Sub-agents-internes-PMS]]
- [[OpenClaw-VPS-Reference]]

## 📋 To-do persistante

- [[TODO-centralized]] — actions que [[User-Raphael-Distefano|Raphaël]] doit faire manuellement (à présenter quand il demande "ma to-do")

## 🔍 Pour chercher

- **Recherche sémantique** : Smart Connections (à activer dans Obsidian Settings)
- **Recherche graphe** : Graph view Obsidian + plugin Graph Analysis
- **Via IA** : un agent connecté en MCP peut faire `search`/`list_files`/`read_file` directement

## 📐 Convention frontmatter

Cf. [[Frontmatter-Standard]]. Tous les nouveaux notes doivent avoir au minimum :
```yaml
type, status, tags, created, updated, relevance, description, ai_writable
```

## 🔗 Conventions de liens

- `[[Note]]` simple
- `[[Note|alias]]`
- Frontmatter `related: ["[[Note1]]", "[[Note2]]"]`
- Frontmatter `depends_on:`, `supersedes:`, `superseded_by:`

Cibler **5-15 wikilinks** par note pour densité neuronale (cf. [[Atomic-Notes-Pattern]]).
