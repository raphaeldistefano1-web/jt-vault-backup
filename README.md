# Vault Le Jardin Tropical — Cerveau IA unifié

Vault Obsidian centralisant la mémoire pour Claude / ChatGPT / Gemini / Cursor / Claude Code. Initialisé le **2026-04-25** par Claude.

## Structure (PARA + couche IA)

```
vault/
├── AGENTS.md          # orientation universelle des IA (lue en 1er)
├── CLAUDE.md          # → symlink vers AGENTS.md
├── README.md          # ce fichier
├── 00-Inbox/          # capture rapide, notes brouillons (IA write ici par défaut)
├── 10-Projects/       # actif, deadline (chaque projet = sous-dossier)
├── 20-Areas/          # responsabilités continues (Hotel-Operations, Dev-PMS…)
├── 30-Resources/      # références (Stack-Tech, Email-Infra, Fournisseurs…)
├── 40-Archives/       # dormant, READ-ONLY pour les IA
├── 50-MOCs/           # Maps of Content — entry points par sujet
├── 60-Daily/          # journal / daily notes
└── 90-Meta/
    └── templates/     # templates de notes
```

## Quickstart Obsidian

1. **Clone le vault** sur ton desktop :
   ```bash
   git clone <repo-url> ~/vault-jardin-tropical
   ```
2. **Installe Obsidian** (https://obsidian.md), ouvre le vault.
3. **Plugins community à activer** (Settings → Community Plugins → Browse) :
   - **Smart Connections** (recherche sémantique locale, embeddings BGE)
   - **Obsidian Git** (commits + push automatiques)
   - **Local REST API** (pour exposer le vault aux IA via MCP)
   - **Templater** (templates de notes)
   - **QuickAdd** (capture rapide)
4. **Configure Smart Connections** : embedding model = `BGE-small-en-v1.5` (local, gratuit). Laisse indexer.
5. **Configure Obsidian Git** : commit toutes les 10 min, push toutes les heures.

## Brancher Claude Desktop / Claude Code via MCP

Plugin Local REST API → notes la **clé API** générée. Puis dans `~/.config/claude/claude_desktop_config.json` (ou config Claude Code) :

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

⚠️ Obsidian doit être **ouvert** sur ta machine pour que le MCP marche.

## Convention frontmatter pour toute nouvelle note

```yaml
---
type: note            # note | project | area | resource | reference | meeting | decision
status: active        # active | draft | archived
tags: [hotel, dev]
created: 2026-04-25
updated: 2026-04-25
relevance: high       # high | medium | low
description: "Une phrase qui résume la note pour qu'une IA la classe."
ai_writable: false    # true si IA peut modifier ce fichier
---
```

## Sync VPS

Le VPS pull le vault toutes les 15 min (cron) dans `/srv/vault-jardin-tropical/`. Claude Code sur le VPS lit ce dossier directement.
