---
type: moc
title: Recommandations système et Claude
---
# Recommandations — Map of Content

Cet espace stocke en continu les **améliorations possibles** détectées par Claude pendant nos sessions (frictions, configs sous-optimales, automatisations utiles, lacunes dans le système, patterns positifs à généraliser).

Chaque note suit le template `_TEMPLATE.md` avec un frontmatter `status: pending | applied | rejected | postponed`.

Tous les dimanches à **18h CET**, le pipeline `~/improvements/bin/weekly-digest.py` consolide les notes `status: pending` et envoie un email récapitulatif à `raphael.distefano1@gmail.com` avec :
- Le constat
- Pourquoi c'est utile / problématique
- Les étapes concrètes d'application

Raphaël lit, décide, met à jour le frontmatter (`status: applied` ou `rejected` ou `postponed`).

## Cibles possibles (`target` frontmatter)

| Target | Quoi | Exemples |
|---|---|---|
| `system` | Infra, VPS, hooks, configuration globale | Migrer X service, durcir Y config, ajouter monitoring Z |
| `claude` | Mes règles, mémoire, comportement | Capturer pattern P, créer agent A, charger skill S sur task T |
| `workflow` | Process de travail Raphaël | Discipline preview-then-apply généralisée, raccourci tmux |
| `infra` | Hostinger, Tailscale, Syncthing, etc. | Backup, monitoring, scaling |
| `pms` | Le Jardin Tropical specific | Refacto module, fix UX, automatisation |
| `vault` | Système de mémoire/knowledge | Nouveau MOC, restructuration |

## Statuts

- `pending` — en attente d'arbitrage (présentée dans le digest hebdo)
- `applied` — réalisée (gardée pour audit trail, retirée du digest)
- `rejected` — refusée explicitement (idem, audit trail)
- `postponed` — reportée à plus tard (réapparaît dans digest avec `defer_until` si fixé)

## Comment Claude doit capturer

Cf. `/Users/raphia/.claude/CLAUDE.md` section "Capture des recommandations". TL;DR : pendant les sessions, dès qu'une amélioration potentielle est repérée, créer une note ici plutôt que la mentionner en passant.

## Liens

- [[_TEMPLATE]] — squelette de note
- Vault parent : [[../00-Index]] (si existe)
