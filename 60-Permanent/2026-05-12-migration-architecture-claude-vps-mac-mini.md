---
ai_writable: false
area: null
backlinks:
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- CANONICITY
- VPS-Access-Tailscale
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- Mac mini
- VPS Hostinger
- Mémoire Claude
- MCP servers
- Codex CLI
id: 20260512040304-migration-architecture-claude-vps-mac-mini
intent: decision
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-12-upgrade-whisper-model-apple-silicon
- AGENTS
- CANONICITY
- VPS-Access-Tailscale
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-12-0048-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0102-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0040-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0043-session-13c136f3.md
source_session: 13c136f3-b295-415e-a3a5-7c632218fad1
status: active
summary: Basculer écosystème Claude de VPS Hostinger vers Mac mini comme nœud principal.
tags:
- permanent
- synthesized
- migration
- architecture
- setup
- mac
tier: warm
title: 'Migration architecture Claude : VPS → Mac mini'
topic_cluster: claude-system-migration
type: permanent-note
updated: '2026-05-12'
---

**Contexte** : L'écosystème Claude (mémoire, MCP servers, Codex CLI, agents) a migré du VPS Hostinger vers le Mac mini M2 de Raphaël en mode « main basse ».

**Éléments impliqués** :
- Mémoire Claude (`~/.claude/projects/`)
- MCP servers (Google Drive, WordPress.com, Codex CLI, Context7)
- Codex CLI OAuth (ChatGPT Plus)
- Vault Obsidian (sync via Tailscale + Syncthing)
- Tmux dashboard (quotas live)

**Rationale** : Cette architecture permet un contrôle local plus fin, latence réduite pour certaines opérations, et centralise les décisions sur la machine principalement utilisée (vs. exécution VPS distante).

**Implications** : Claude Code sur le Mac devient le point d'entrée principal; VPS devient exécuteur secondaire pour tâches longues/coûteuses (builds, deployments, scraping).

## Related

- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[AGENTS]] — AGENTS
- [[2026-05-08-syncthing-p2p-vault-sync-tailscale-only]] — Syncthing P2P vault sync Tailscale-only
- [[2026-05-12-upgrade-whisper-model-apple-silicon]] — 2026-05-12-upgrade-whisper-model-apple-silicon