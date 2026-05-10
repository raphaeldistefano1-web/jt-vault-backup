---
ai_writable: false
area: null
backlinks:
- 2026-05-09-claude-max-5x-fenêtre-courte-à-réserver
- 2026-05-09-codex-cli-en-mcp-server-pour-économiser-quota-clau
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- tmux
- claude-quota.py
- codex-quota.py
- btop
id: 20260509040244-tmux-dashboard-3-windows-monitoring-quotas-live-cl
intent: pattern
last-accessed: '2026-05-09'
moc: null
project: null
related:
- 2026-05-09-claude-max-5x-fenêtre-courte-à-réserver
- 2026-05-09-codex-cli-en-mcp-server-pour-économiser-quota-clau
- 2026-05-10-claude-max-quota-fenêtre-5h-limitée-stratégie-rése
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1625-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1345-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1433-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1359-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1401-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1326-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1426-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1325-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1807-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1342-session-d31950cd.md
- 10-Projects/claude-system/2026-05-08-1422-session-d31950cd.md
source_session: d31950cd-6d46-47f9-aab9-3167d0bc3628
status: active
summary: Layout tmux auto-lancé affichant quotas live Claude/Codex + ressources système
  dans 3 windows persistantes.
tags:
- permanent
- synthesized
- monitoring
- quota-tracking
- automation
tier: warm
title: Tmux dashboard 3-windows monitoring quotas live Claude/Codex
topic_cluster: infrastructure-claude
type: permanent-note
updated: '2026-05-09'
---

Setup tmux dans ~/.bashrc crée layout 3-windows au startup : (1) Haut-gauche : quotas live (scripts Python claude-quota.py + codex-quota.py, polling 60s), (2) Main : btop ressources système, (3) Bottom : shell interactif. Permet visibilité temps-réel quand approche plafond Claude Max pour basculer vers Codex. Placement toujours visible pendant travail. Aucun overhead significatif.

## Related

- [[2026-05-09-codex-cli-en-mcp-server-pour-économiser-quota-clau]] — Codex CLI en MCP server pour économiser quota Claude Max
- [[2026-05-09-claude-max-5x-fenêtre-courte-à-réserver]] — Claude Max 5x : fenêtre courte, à réserver
- [[2026-05-10-claude-max-quota-fenêtre-5h-limitée-stratégie-rése]] — Claude Max quota — fenêtre 5h limitée, stratégie réservation