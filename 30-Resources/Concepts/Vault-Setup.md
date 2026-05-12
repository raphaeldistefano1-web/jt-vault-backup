---
ai_writable: false
backlinks:
- 2026-04-25-session-context
- 2026-04-25-session-context 2
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- AGENTS-md-standard
- Atomic-Notes-Pattern
- Frontmatter-Standard
- MCP-Model-Context-Protocol
- VPS-Hostinger
- llms-txt-standard
created: 2026-04-25
description: Setup du vault Obsidian — installer Obsidian, plugins clés, MCP, sync
  git
embed_hash: null
embed_model_version: null
entities:
- documentation
- obsidian
- reference
id: 202604252041-vault-setup
intent: concept
last-accessed: 2026-04-25
related:
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- VPS-Access-Tailscale
- '[[AGENTS-md-standard]]'
- '[[Atomic-Notes-Pattern]]'
- '[[Frontmatter-Standard]]'
- '[[MCP-Model-Context-Protocol]]'
relevance: high
status: active
summary: /srv/vault-jardin-tropical/ sur le VPS Hostinger 46.202.171.204.
tags:
- vault
- setup
- obsidian
tier: warm
topic_cluster: vault-architecture
type: concept
updated: 2026-04-25
---

# 🛠️ Vault Setup

## Path serveur

`/srv/vault-jardin-tropical/` sur le VPS Hostinger 46.202.171.204.

Cron sync à mettre en place : `git pull` toutes les 15 min pour avoir un vault à jour côté Claude Code VPS.

## Setup côté desktop (Obsidian)

### 1. Installer Obsidian
- Télécharger https://obsidian.md
- Versions desktop (Mac/Linux/Windows) + mobile (iOS/Android)

### 2. Cloner le vault
```bash
git clone <repo-url> ~/vault-jardin-tropical
```

Ouvrir le dossier dans Obsidian → "Open folder as vault".

### 3. Plugins community à activer

Settings → Community Plugins → Browse, installer puis activer :

| Plugin | Pour quoi |
|---|---|
| **Smart Connections** | Embeddings locaux (BGE), semantic search, suggested links |
| **Obsidian Git** | Commit + push automatiques |
| **Local REST API** | Expose vault sur 127.0.0.1:27123 pour MCP |
| **Templater** | Templates de notes |
| **Graph Analysis** (optionnel) | Centralité, communautés Louvain |

### 4. Configurer Smart Connections

Settings → Smart Connections → Embedding model = `BGE-small-en-v1.5` (local, gratuit).
Laisser indexer (~30s à 5min selon taille du vault).

### 5. Configurer Obsidian Git

Settings → Git → Auto commit-and-sync : 10 min, Pull interval : 15 min.

## Setup côté Claude Desktop / Claude Code via MCP

### 1. Local REST API plugin
Settings → Local REST API → Note la **clé API** générée.

### 2. Configurer le client MCP
Dans `~/.config/claude/claude_desktop_config.json` (Claude Desktop) ou config Claude Code :

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["obsidian-mcp-server"],
      "env": {
        "OBSIDIAN_API_KEY": "<clé du plugin>",
        "OBSIDIAN_BASE_URL": "http://127.0.0.1:27123",
        "OBSIDIAN_VERIFY_SSL": "false"
      }
    }
  }
}
```

⚠️ **Obsidian doit être ouvert** pour que MCP fonctionne via Local REST API.

### 3. Tester
Dans Claude Desktop : "list files in my Obsidian vault" → doit lister les fichiers.

## Conventions

- [[Atomic-Notes-Pattern]] — 1 idée = 1 note, 200-1500 mots, 5-15 wikilinks
- [[Frontmatter-Standard]] — YAML strict obligatoire
- **AGENTS.md** symlink vers **CLAUDE.md** (cf. [[AGENTS-md-standard]])
- Structure PARA + couches : 00-Inbox, 10-Projects, 20-Areas, 30-Resources, 40-Archives, 50-MOCs, 60-Daily, 90-Meta

## Sync VPS ↔ Desktop

- **Vault canonique** : VPS `/srv/vault-jardin-tropical/`
- **Sync** : git push depuis desktop, cron `git pull` côté VPS
- **Claude Code sur VPS** : lit le vault directement par filesystem (pas besoin de MCP côté VPS)
- **Claude Desktop / Claude Code sur desktop** : lit via MCP Obsidian

## Liens

- [[INDEX]]
- [[MCP-Model-Context-Protocol]]
- [[AGENTS-md-standard]]
- [[Atomic-Notes-Pattern]]

## Related

- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[2026-05-08-syncthing-p2p-vault-sync-tailscale-only]] — Syncthing P2P vault sync Tailscale-only
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS