---
backlinks:
- 2026-05-08-frontmatter-enrichi-extrait-insights-durables
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- 2026-05-09-adr-template-et-pattern-docsadr
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-10-stack-cul-sec-pwa-nextjs-14-app-router
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- 2026-05-12-migration-architecture-claude-vps-mac-mini
- INDEX
related:
- 2026-05-08-frontmatter-enrichi-extrait-insights-durables
- '2026-05-12'
- '2026-05-13'
- check-1-critique-2026-05-14-1244
---

# AGENTS.md — orientation universelle pour les IA

> Standard Linux Foundation Agentic AI Foundation. Lu par défaut par Cursor, Codex CLI, Gemini CLI, Aider, et — par symlink vers `CLAUDE.md` — par Claude Desktop / Claude Code.
>
> **Mis à jour 2026-05-07** — vault refondé en cerveau multi-projets auto-alimenté.

## Identité utilisateur

- **Raphaël Di stefano**, owner-operator de l'hôtel **Le Jardin Tropical** (Bouillante, Guadeloupe).
- Stack quotidienne : PMS Next.js custom + site WordPress + dev quotidien avec Claude Code.
- Préférences : explications **concrètes, en français**. À l'aise avec docker / CLI / Linux mais pas dev full-time.
- Mode de collaboration : préfère **agir** plutôt que sur-planifier. Ne pas demander confirmation pour des actions safe et réversibles.

## Architecture du vault — ENTRÉE OBLIGATOIRE

**Règle d'or — Claude/IA ne lit JAMAIS le vault par glob brut.** Hiérarchie d'entrée :

```
1. INDEX.md (racine)               ← navigation par couche, MOCs listés
   ↓
2. _MOC-<projet>.md                ← hub d'entrée du projet courant
   ↓
3. _Index.md (auto-généré)         ← liste des notes du projet par tier
   ↓
4. Note atomique (ouvrir si frontmatter `summary` matche le besoin)
```

Cette hiérarchie est **token-efficient** : on ne lit que ce qui est nécessaire grâce au champ `summary` dans le frontmatter (1 phrase 25 mots max, lue avant le corps).

## Structure PARA enrichie (mai 2026)

```
00-Inbox/                          ← Capture brute, dispatch quotidien (vault-curator)
05-Daily/                          ← Journal auto-généré YYYY-MM-DD.md
10-Projects/<slug>/                ← Projets actifs (avec _MOC-<slug>.md hub)
   ├── pms-jardin-tropical/        ← PMS Next.js custom
   ├── claude-system/              ← Système IA personnel (agents, skills, hooks, vault)
   ├── site-wordpress/             ← Site lejardintropical
   ├── openclaw-plugin/            ← Plugin OpenClaw + gateway IA
   ├── desktop-app-electron/       ← Wrapper desktop PMS
   ├── jt-migrate/                 ← Plugin migration WordPress
   ├── n8n-automations/            ← n8n self-hosted + bus events
   └── montage-video/              ← Pipeline Whisper→Claude→FFmpeg
20-Areas/<slug>/                   ← Responsabilités continues (sans deadline)
   ├── hotel-operations/           ← Gestion hôtel, équipe, RGPD
   ├── dev-tooling/                ← VPS, Tailscale, backups, monitoring
   ├── marketing-comm/             ← Site, SEO, réseaux sociaux
   └── personal/                   ← Profil utilisateur, préférences
30-Resources/                      ← Références réutilisables
   ├── concepts/                   ← Modèles mentaux, abstractions
   ├── workflows/                  ← Procédures
   ├── snippets/                   ← Bouts de code réutilisables
   └── credentials-encrypted/      ← Credentials chiffrés (age/gpg)
40-Archives/                       ← Projets clos (READ-ONLY, ne jamais modifier)
50-MOCs/                           ← Maps of Content transversales
   ├── Decisions-Log.md            ← Toutes les décisions techniques
   ├── Lessons-Learned.md          ← Apprentissages transversaux
   ├── Stack-Tech.md               ← VPS, domaines, ports
   └── Hotel.md                    ← Sujets hôtel
60-Permanent/                      ← Notes atomiques évergreen (Zettelkasten)
90-Meta/
   ├── templates/                  ← note-template.md (à utiliser pour toute nouvelle note)
   ├── schemas/                    ← note-schema.md (référence frontmatter canonique)
   └── bases/                      ← Obsidian Bases (.base files, vues dynamiques)
```

## Frontmatter canonique

Toute note **doit** avoir le frontmatter défini dans `90-Meta/schemas/note-schema.md`. Champs critiques :

- `id` : `YYYYMMDDHHMM-slug`, immuable
- `summary` : 1 phrase 25 mots max — clé pour retrieval token-efficient
- `entities` : 3-7 entités lowercase kebab-case
- `tier` : `hot` | `warm` | `cold` (politique de chargement)
- `embed_model_version` + `embed_hash` : null tant que pas embeddé (Phase 4 future-proof)

## Règles d'écriture pour les IA

1. **Toute note IA va dans `00-Inbox/`** avec frontmatter complet (préfixe `id` horodaté).
2. **Ne JAMAIS modifier** sans `ai_writable: true` ou en `40-Archives/`.
3. **Mode append-only** pour decisions, contracts.
4. **Frontmatter YAML obligatoire** (template : `90-Meta/templates/note-template.md`).
5. **`updated:` strict** à chaque modif.
6. **Wikilinks par titre** sauf si collision → utiliser `id` (`[[20260507-1530-vault-rebuild]]`).
7. **`related:` ≥ 1** sauf MOCs racine (anti-orphelin).
8. **Tags ≤ 3** par note (taxonomie fermée ci-dessous).

## Taxonomie fermée des tags

**Domaines** : `hotel`, `pms`, `wordpress`, `ai`, `automation`, `marketing`, `migration`, `vault`
**Type technique** : `decision`, `bug`, `workflow`, `concept`, `architecture`, `moc`, `index`, `schema`
**Sous-systèmes** : `auth`, `auth-stack`, `nextauth`, `electron`, `desktop`, `n8n`, `whisper`, `obsidian`, `mcp`, `hooks`

Tout nouveau tag ⇒ ajouter ici.

## FAQ qu'aucune IA ne doit me redemander

- **Hébergement principal** : VPS Hostinger, IP 46.202.171.204
- **Accès** : Tailscale uniquement (port 22 fermé public depuis 2026-05-06), `ssh monvps` (Mac), Termius+Tailscale (iPhone)
- **Site WordPress** : https://wp-46-202-171-204.nip.io (en attendant domaine final `lejardintropical.fr`)
- **PMS** : https://pms-46-202-171-204.nip.io
- **Email pro** : `lejardintropical@orange.fr` (à migrer vers domaine pro pour DKIM)
- **Téléphone** : +590 690 75 44 73
- **Stack PMS** : Next.js 15 + PostgreSQL + Prisma 6 + Tailwind, Nginx port 8080, Traefik Docker pour 80/443
- **Stack site** : WordPress 6.6 / PHP 8.3 / MariaDB 11 / Apache, theme custom `jardintropical-child`, plugin booking custom `jt-booking`
- **n8n** : https://n8n-46-202-171-204.nip.io (v1.107.4)
- **Whisper** : `whisper audio.mp3` CLI (faster-whisper large-v3-turbo, CPU only)
- **Outils dev** : Claude Code en daily, Cursor occasionnel, ChatGPT/Gemini parfois
- **Abonnement** : Claude Plan Max 5x sans API, quotas par fenêtre 5h

## Conventions techniques

- **Commits** : conventional commits (`feat:`, `fix:`, `docs:`, etc.)
- **Branches** : feature branches courtes, merge sur `main`
- **Code review** : auto-review avec `code-reviewer` agent avant merge
- **Workflow refonte UI** : preview-then-apply via route `_v2`, jamais modif directe shell prod
- **Permissions** : actions destructives nécessitent confirmation (rm -rf, force push, drop table)
- **Vault git versionné** : commit après chaque modif structurelle, snapshot tarball avant grosses opérations

## Politique de modèles (économie tokens)

- **Sessions Claude principales** (Raphaël qui bosse) : Opus 4.7
- **Hooks Claude Code** (extract_memory en fin de session) : **Haiku 4.5**
- **Vault-curator** (cron quotidien futur) : **Haiku 4.5**
- **Migrator frontmatter** (one-shot) : **Haiku 4.5**
- **Décisions complexes en agents** (architecture, code review) : Sonnet 4.6 ou Opus selon criticité

## Phase de transition (mai 2026)

Le vault est en refonte multi-projets (Phases 0-3 de la roadmap dans `[[20260507-1530-vault-rebuild]]` mémoire CC `project_vault_rebuild.md`). Pendant cette phase :

- Phase 0-1 : structure ✅ (tag git `pre-rebuild-2026-05-07`)
- Phase 2 : migrator frontmatter étendu (en cours)
- Phase 3 : hook Stop extract_memory (à venir)
- Phases 4+ différées : MCP server, semantic search (Smart Connections + nomic-embed-text-v2-moe + sqlite-vec)

Pendant la transition, les anciennes notes peuvent avoir un frontmatter incomplet — c'est normal, le migrator s'en charge.

## Path canonique

- **Path canonique nouveau** : `/srv/vault/`
- **Symlink rétrocompat** : `/srv/vault-jardin-tropical → vault` (toutes les références anciennes continuent de fonctionner)

## Related

- [[2026-05-08-frontmatter-enrichi-extrait-insights-durables]] — Frontmatter enrichi extrait insights durables
- [[2026-05-12]] — Veille IA — Mardi 12 mai 2026
- [[2026-05-13]] — Veille IA — Mercredi 13 mai 2026
- [[check-1-critique-2026-05-14-1244]] — check-1-critique-2026-05-14-1244