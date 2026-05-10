---
ai_writable: true
area: null
backlinks:
- OpenClaw-VPS-Reference
- PMS-Desktop-Reference
- Stack-Tech
- VPS-Hostinger
- Vault-Setup
- _VAULT-INDEX
confidence: high
created: 2026-05-07
embed_hash: null
embed_model_version: null
entities:
- vps
- tailscale
- ssh
- security
- backup-access
id: 20260507-1128-vps-access
intent: how-to
last-accessed: 2026-05-07
moc: '[[Stack-Tech]]'
project: null
related:
- '[[Stack-Tech]]'
source: memory:reference_vps_access.md
status: active
summary: VPS Hostinger port 22 fermé. Accès SSH uniquement via Tailscale (100.98.218.10).
  Alias Mac, iPhone+Termius, backup console VNC.
tags:
- vps
- tailscale
- security
tier: hot
title: Accès VPS via Tailscale (depuis 2026-05-06)
topic_cluster: null
type: reference
updated: 2026-05-07
---

# Accès VPS via Tailscale

> Note portée depuis la mémoire Claude Code `reference_vps_access.md` le 2026-05-07.

VPS Hostinger srv1524600 (IP publique 46.202.171.204) — depuis le 2026-05-06, le port 22 public est **fermé via ufw**. Accès SSH uniquement via le réseau Tailscale.

## Identifiants Tailscale

- Hostname Tailscale : `vps-pms` (MagicDNS) ou FQDN `vps-pms.tail9326f3.ts.net`
- IP Tailscale : `100.98.218.10`
- Owner : raphael.distefano1@gmail.com
- Tailscale SSH activé (`tailscale up --ssh`) → auth via identité Google possible sans clé classique
- Mac de Raphaël dans le tailnet : `macbook-air-de-raphael` (100.127.80.69)
- iPhone : à ajouter au tailnet via app Tailscale + Termius pour SSH mobile (setup en cours 2026-05-06)

## Côté Mac (alias)

`~/.ssh/config` contient :
```
Host monvps
    HostName vps-pms
    User root
    ServerAliveInterval 60
    ServerAliveCountMax 3
    SetEnv TERM=xterm-256color
```

Commande quotidienne : `ssh monvps`

## Côté VPS (état)

- `tmux` 3.4 + `/root/.tmux.conf` (préfixe Ctrl+a, splits `|`/`-`, hjkl)
- Auto-setup dashboard tmux via bloc dans `/root/.bashrc` → appelle `/root/.local/bin/claude-tmux-setup.sh`
  - Window 1 `claude` : Claude Code plein écran
  - Window 2 `dash` : pane gauche shell libre, pane haut-droit `btop`, pane bas-droit `claude-session-tail.sh`
  - Switch via `Ctrl+a → 1` / `Ctrl+a → 2`
- `/root/.local/bin/claude-session-tail.sh` : tail -F du `.jsonl` Claude le plus récent dans `/root/.claude/projects/`, formatté via `jq`
- `btop` installé via apt
- `ufw` actif : deny incoming, allow outgoing, allow `tailscale0`, allow 80/443/tcp, allow 22/tcp depuis `169.254.0.0/16` (Terminal Navigateur Hostinger en backup)
- Tailscale 1.96.4 via repo apt officiel (codename noble)

## Côté iPhone

- App **Tailscale** (iOS) + app **Termius** (free tier) — host configuré sur `100.98.218.10` (ou `vps-pms` si MagicDNS sync) en root, sans clé SSH (Tailscale SSH gère)
- iOS dictation native via le micro du clavier → marche pour dicter à Claude depuis le téléphone (la voix reste locale, seul le texte transite)

## Stratégie d'accès — 3 chemins indépendants

1. **Quotidien** : `ssh monvps` (Tailscale) depuis Mac/iPhone — chemin principal
2. **Backup réseau** : Terminal Navigateur Hostinger (panel hPanel) — fonctionne si Tailscale tombe
3. **Break glass** : Console VNC/Serial dans le panel Hostinger — fonctionne même si SSH cassé sur le VPS

## Modèle de sécurité (à rappeler à Raphaël si question similaire)

- Claude Code tourne sur le VPS → ne voit QUE le VPS. Mac/iPhone restent étanches : ce sont juste écran+clavier+micro.
- Voice dictation (Spokenly ou iOS native) : conversion voix→texte 100% locale sur Mac/iPhone, seul le texte est envoyé via SSH. La voix ne quitte jamais l'appareil.
- Si compromission VPS : Mac/iPhone non impactés. Si vol d'iPhone : révoquer le device dans l'admin Tailscale = coupe l'accès.

## Notes opérationnelles

- En cas de lockout (Tailscale down, etc.) : console VNC dans le panel Hostinger
- Pour rouvrir SSH public temporairement : `sudo ufw allow 22/tcp` puis le re-deny après
- Le `SetEnv TERM=xterm-256color` côté Mac est critique : Ghostty annonce `xterm-ghostty` qui n'est pas reconnu par tmux sur le VPS
- Notes setup complètes : `/root/CLAUDE-CODE-SETUP-NOTES.md` sur le VPS
- Manuel tmux complet (PDF, A4, illustré) : `/tmp/tmux-guide.pdf` sur le VPS, source HTML `/tmp/tmux-guide.html`, Markdown source `/root/TMUX-GUIDE.md`

## Liens
- MOC parent : [[Stack-Tech]]
- Source : `memory:reference_vps_access.md`