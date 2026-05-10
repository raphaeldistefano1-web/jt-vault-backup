---
ai_writable: false
area: null
backlinks:
- 2026-04-25-session-context
- 2026-04-25-session-context 2
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-10-registry-pattern-centralisateur-jeux-modulaires
- Decisions-Log
- Lessons-Learned
- Vault-Setup
- _MOC-claude-system
- _MOC-desktop-app
- _MOC-jt-migrate
- _MOC-montage-video
- _MOC-n8n
- _MOC-openclaw
- _MOC-pms
- _MOC-site-wordpress
- _VAULT-INDEX
confidence: high
created: 2026-04-25
embed_hash: null
embed_model_version: null
entities:
- vault
- index
- navigation
id: 20260507-1110-index-root
intent: reference
last-accessed: 2026-05-07
moc: null
project: null
related:
- 2026-04-25-session-context 2
- 2026-05-10-registry-pattern-centralisateur-jeux-modulaires
- '[[AGENTS]]'
- '[[Decisions-Log]]'
- '[[Lessons-Learned]]'
source: null
status: active
summary: Entry point racine du vault — navigation par couches PARA + MOCs par projet.
tags:
- index
- root
- moc
tier: hot
title: INDEX racine — cerveau multi-projets
topic_cluster: meta
type: moc
updated: 2026-05-07
---

# 🧠 INDEX — Cerveau Raphaël Distefano

> Vault Obsidian multi-projets. Mémoire unifiée pour Claude Code / Cursor / ChatGPT / Gemini via [[AGENTS]] (= CLAUDE.md).
>
> Refondé 2026-05-07 en architecture multi-projets auto-alimentée.

## 🚀 Quickstart pour une IA qui débarque

1. Lire **[[AGENTS]]** → orientation 30s
2. Identifier le projet courant (depuis `cwd`, le prompt user, ou demander)
3. Ouvrir le **`_MOC-<projet>`** correspondant (cf. tableau ci-dessous)
4. Lire **uniquement** les notes pertinentes (filtrer par frontmatter `summary` + `tier`)
5. **Jamais de glob brut** sur le vault (cramerait les tokens)

## 🗺️ MOCs par projet (10-Projects)

| Projet | MOC | Status | Tier |
|---|---|---|---|
| PMS Jardin Tropical | [[_MOC-pms]] | 🟢 Actif | hot |
| Claude System | [[_MOC-claude-system]] | 🟢 Actif | hot |
| Site WordPress | [[_MOC-site-wordpress]] | 🟢 Actif | hot |
| OpenClaw Plugin | [[_MOC-openclaw]] | 🟢 Actif | hot |
| Desktop App Electron | [[_MOC-desktop-app]] | 🟡 Maintenance | warm |
| JT-Migrate | [[_MOC-jt-migrate]] | 🟡 Audit en cours | warm |
| n8n Automations | [[_MOC-n8n]] | 🟢 Actif | hot |
| Montage Vidéo | [[_MOC-montage-video]] | 🟠 Démarrage | warm |

## 🌐 MOCs transversales (50-MOCs)

| MOC | Contenu | Filter |
|---|---|---|
| [[Decisions-Log]] | Toutes les décisions techniques (chronologique) | par `project:` |
| [[Lessons-Learned]] | Apprentissages transversaux | par `topic_cluster:` |
| [[Stack-Tech]] | VPS, ports, paths, infra | global |
| [[Hotel]] | Business, capacité, services | global |

## 🏛️ Areas (20-Areas) — responsabilités continues

| Area | Sujet |
|---|---|
| `hotel-operations/` | Gestion quotidienne, équipe, RGPD |
| `dev-tooling/` | VPS, Tailscale, backups, monitoring |
| `marketing-comm/` | Site, SEO, réseaux sociaux |
| `personal/` | Profil utilisateur, préférences |

## 📚 Resources (30-Resources)

- `concepts/` — Modèles mentaux réutilisables
- `workflows/` — Procédures
- `snippets/` — Bouts de code réutilisables
- `credentials-encrypted/` — Secrets chiffrés (age/gpg)

## 🌱 Permanent notes (60-Permanent)

Notes atomiques évergreen (style Zettelkasten). À enrichir au fil du temps avec les apprentissages durables transversaux aux projets.

## 📥 Inbox (00-Inbox) — capture brute

Notes en attente de dispatch. Vidée par le **vault-curator** quotidien (Phase 5 future) ou manuellement.

## 📅 Daily (05-Daily)

Journal quotidien `YYYY-MM-DD.md` auto-généré (Phase 5 future).

## 🗄️ Archives (40-Archives) — READ-ONLY

Projets clos. Aucune IA ne doit les modifier.

## 📦 Meta (90-Meta)

- `templates/` — `note-template.md` à utiliser pour toute nouvelle note
- `schemas/` — `note-schema.md` (référence frontmatter)
- `bases/` — Obsidian Bases (.base files) — vues dynamiques

## 🔍 Recherche & retrieval

**À 67 notes (état actuel)** : `grep` + frontmatter `summary` suffisent.

**À ~300 notes (Phase 4 future)** : activation **semantic search** :
- Plugin Smart Connections + Ollama + `nomic-embed-text-v2-moe`
- Stockage `sqlite-vec` (hybrid BM25 + semantic)
- MCP `dan6684/smart-connections-mcp` côté Claude

## 📊 État du vault (2026-05-07)

- Notes totales : **67** (pré-refonte)
- Wikilinks : **619+**
- Projets avec MOC : **8** (créés Phase 1)
- Frontmatter étendu : **0%** (Phase 2 à venir)
- Auto-alimentation hooks : **Pas active** (Phase 3 à venir)
- Semantic search : **Pas active** (Phase 4 future, seuil ~300 notes)
- Path canonique : `/srv/vault/` (symlink rétro `/srv/vault-jardin-tropical/`)
- Versionning : git (tag `pre-rebuild-2026-05-07` posé avant refonte)

## Related

- [[2026-04-25-session-context 2]] — 2026-04-25-session-context 2
- [[2026-05-10-registry-pattern-centralisateur-jeux-modulaires]] — Registry pattern — centralisateur jeux modulaires