---
ai_writable: false
area: null
backlinks:
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- CANONICITY
- RUNBOOK-disaster-recovery
- VPS-Access-Tailscale
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- vault-rag
- Mac mini
- Tailscale SSH
- nomic-v2-moe
id: 20260512040408-vault-rag-multi-instance-trade-off-ssh-wrapper-vs-
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- VPS-Access-Tailscale
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- CANONICITY
- RUNBOOK-disaster-recovery
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-11-2202-session-d41c35b1.md
- 10-Projects/claude-system/2026-05-11-2154-session-d41c35b1.md
- 10-Projects/claude-system/2026-05-11-2146-session-d41c35b1.md
- 10-Projects/claude-system/2026-05-11-2125-session-d41c35b1.md
source_session: d41c35b1-20aa-48d5-b5d8-36100ffefa41
status: active
summary: 'Deux chemins pour exposer vault-rag sur Mac mini : SSH (~100ms latence)
  vs install local (~2 GB, 0ms latence)'
tags:
- permanent
- synthesized
- latency
- multi-instance
- architecture
- disk-footprint
tier: warm
title: 'vault-rag multi-instance : trade-off SSH wrapper vs install local'
topic_cluster: vault-architecture
type: permanent-note
updated: '2026-05-12'
---

Quand intégrer Mac mini comme ops/preview instance, vault-rag (MCP SQLite+vec0+nomic-v2-moe) tourne sur VPS. Deux architectures.

**Option A : SSH wrapper via Tailscale**
- Mac queries traverse Tailscale → VPS vault-rag API
- Latence ~100-150ms (réseau fiable)
- Empreinte Mac : ~0 (aucun modèle local)
- Pragmatique pour Mac 256-512 GB SSD

**Option B : Install local nomic modèle**
- Réinstall modèle nomic-v2-moe sur Mac (~2 GB)
- Latence proche 0 (local inference)
- Requiert sync avec VPS (deux copies modèle)
- Idéal si preview workflow latency-critical

**Critères décision** : (1) SSD Mac dispo, (2) fréquence queries preview, (3) tolérance latence réseau, (4) maintenance deux modèles vs pas. Option A : stockage-first. Option B : latency-first. Raphaël contexte : Mac mini récent → probablement 512+ GB → Option B envisageable si preview workflow justifie.

## Related

- [[2026-05-08-syncthing-p2p-vault-sync-tailscale-only]] — Syncthing P2P vault sync Tailscale-only
- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[RUNBOOK-disaster-recovery]] — Runbook — Disaster Recovery vault