---
type: resource
status: active
tags: [pms, openclaw, vps, infra]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Paths, ports, commandes pour le Gateway OpenClaw sur le VPS — loopback 18789"
ai_writable: false
related:
  - "[[Plugin-OpenClaw]]"
  - "[[Stack-Tech]]"
  - "[[VPS-Hostinger]]"
---

# 🔧 OpenClaw VPS — référence

## Endpoints

- **Gateway** : `http://127.0.0.1:18789` (loopback only, pas exposé publiquement)
- Routes principales :
  - `/v1/chat/completions` — proxy vers les LLMs (OpenAI / Anthropic / etc.)

## Paths config

- **Config** : (cf. mémoire `reference_openclaw_vps.md` pour path exact)
- **Auth profiles** : (idem)

## Service systemd

- Nom du service systemd
- **Fix appliqué** : ExecStart pointe vers `node` chargé par NVM (le default `node` ne marche pas)

## Commandes

- Restart : `systemctl restart openclaw-gateway`
- Logs : `journalctl -u openclaw-gateway -f`
- Status : `systemctl status openclaw-gateway`

## Liens

- [[Plugin-OpenClaw]]
- [[Stack-Tech]]
- Mémoire référence : `reference_openclaw_vps.md` (mémoire projet PMS)
