---
ai_writable: false
area: null
backlinks:
- 2026-05-09-codex-cli-en-mcp-server-pour-économiser-quota-clau
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- OpenClaw-VPS-Reference
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- Claude Code
- MCP servers
- OAuth
id: 20260512040305-mcp-reconnect-workflow-mcp-oauth-browser
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- OpenClaw-VPS-Reference
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- _MOC-openclaw
- 2026-05-10-retrouver-contexte-perdu-via-jsonl-logs-claude-cod
- 2026-05-09-codex-cli-en-mcp-server-pour-économiser-quota-clau
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-12-0048-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0102-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0040-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0043-session-13c136f3.md
source_session: 13c136f3-b295-415e-a3a5-7c632218fad1
status: active
summary: Procédure pour reconnecter les MCP servers déconnectés.
tags:
- permanent
- synthesized
- mcp
- setup
- oauth
- troubleshooting
tier: warm
title: 'MCP reconnect workflow : /mcp + OAuth browser'
topic_cluster: mcp-diagnostics
type: permanent-note
updated: '2026-05-12'
---

Quand les MCP servers (Google Drive, WordPress.com, etc.) affichent des erreurs de connexion :

1. Ouvrir Claude Code interactif sur le Mac
2. Taper `/mcp` pour afficher les serveurs connectés
3. Cliquer sur l'entrée du serveur à reconnecter
4. Suivre la connexion OAuth dans le navigateur (~30 sec par serveur)
5. Attendre confirmation du succès

**Timing** : Chaque OAuth prend ~30 secondes (redirection + consentement).

**Cas d'usage** : Reconnect automatique après redémarrage du Mac, changement de réseau, ou expiration de token.

## Related

- [[OpenClaw-VPS-Reference]] — OpenClaw sur le VPS — Paths, ports, config
- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[_MOC-openclaw]] — MOC OpenClaw Plugin
- [[2026-05-10-retrouver-contexte-perdu-via-jsonl-logs-claude-cod]] — Retrouver contexte perdu via JSONL logs Claude Code
- [[2026-05-09-codex-cli-en-mcp-server-pour-économiser-quota-clau]] — Codex CLI en MCP server pour économiser quota Claude Max