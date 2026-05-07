---
type: concept
status: active
tags: [mcp, ai, protocol, standard]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Standard 2026 pour exposer outils/données aux LLMs — MCP donné à la Linux Foundation par Anthropic"
ai_writable: false
related:
  - "[[AGENTS-md-standard]]"
  - "[[Vault-Setup]]"
  - "[[Linux-Foundation-AAIF]]"
aliases: [Model Context Protocol]
id: 202604252025-mcp-model-context-protocol
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "Standard ouvert pour exposer des outils functions et des ressources read-only data à des LLMs/agents. Permet à Claude/Ch…"
entities: [llm, mcp, obsidian, postgres]
topic_cluster: ai-integration
intent: concept
tier: warm
---

# 🔌 MCP — Model Context Protocol

## Définition

Standard ouvert pour exposer des **outils** (functions) et des **ressources** (read-only data) à des LLMs/agents. Permet à Claude/ChatGPT/Gemini de **read/write** dans un système externe (Obsidian, Postgres, Slack…) via une interface uniforme.

## Histoire

- **Créé par Anthropic** en 2024
- **Donné à la Linux Foundation** (Agentic AI Foundation) en **décembre 2025**
- Cohabite désormais avec [[AGENTS-md-standard|AGENTS.md]] (donné par OpenAI) et **Goose** (donné par Block)
- Devient le **standard de fait** en 2026 (60k+ repos exposent un MCP server ou un AGENTS.md)

## Architecture

- **MCP Client** : intégré dans Claude Desktop, Claude Code, ChatGPT Desktop, Cursor, etc.
- **MCP Server** : process séparé qui expose tools/resources via JSON-RPC
- **Transport** : stdio (local) ou HTTP/SSE (remote)

## Usage Le Jardin Tropical

Pour le [[Vault-Setup|cerveau IA]] :
- Plugin Obsidian **Local REST API** expose le vault sur `127.0.0.1:27123`
- **`obsidian-mcp-server`** (Cyanheads) bridge ça en MCP stdio pour Claude Desktop
- Claude peut alors `read_file`, `write_file`, `search`, `list_files`, `get_frontmatter`, etc. directement dans le vault

## Prérequis

- Obsidian doit être **ouvert** (sinon Local REST API down → MCP fail)
- Node 18+ pour `npx obsidian-mcp-server`
- Clé API du plugin Local REST API

## MCP servers Obsidian comparés

| Server | Note |
|---|---|
| `cyanheads/obsidian-mcp-server` | Le plus mature, 8 outils complets — **recommandé** |
| `MarkusPfundstein/mcp-obsidian` | Simple, équivalent |
| `jacksteamdev/obsidian-mcp-tools` | Apporte semantic search + Templater |
| **Obsidian Claude Code MCP plugin** (Ian Sinnott) | Installé DANS Obsidian, expose port 22360 — pas besoin de Local REST API |

## Limitations connues

- Latence ~50-200 ms par call
- **Obsidian doit tourner** : pas de mode headless trivial
- Risque de quota / rate-limit si l'agent abuse des calls
- Les "tools" peuvent halluciner des chemins → toujours `list` avant `read`

## Liens

- [[Vault-Setup]]
- [[Stack-Tech]]
- Spec : https://modelcontextprotocol.io
