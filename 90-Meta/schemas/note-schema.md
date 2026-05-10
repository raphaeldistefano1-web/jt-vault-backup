---
ai_writable: false
backlinks:
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
- 2026-05-08-frontmatter-enrichi-extrait-insights-durables
- 2026-05-08-vault-para-multi-projets-chemin-canonique
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- 2026-05-09-adr-template-et-pattern-docsadr
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- 2026-05-10-decision-defensive-truncation-et-sync-check-vault-
- 2026-05-10-questionsprompts-externalisées-par-jeu
- 2026-05-10-registry-pattern-centralisateur-jeux-modulaires
created: 2026-05-07
description: Schéma canonique du frontmatter pour toutes les notes du vault — référence
  pour humains, Claude, agents, futurs systèmes RAG
related:
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-10-registry-pattern-centralisateur-jeux-modulaires
relevance: high
status: active
tags:
- meta
- schema
- frontmatter
type: schema
updated: 2026-05-07
---

# Note Schema — Frontmatter canonique

## Champs

```yaml
---
# === IDENTIFICATION ===
id: 20260507-1530-vault-rebuild        # YYYYMMDDHHMM-slug, unique, immutable
type: project                           # voir liste types ci-dessous
title: "Refonte vault multi-projets"

# === ROUTING (PARA + projet) ===
project: claude-system                  # slug projet (cf. 10-Projects/<slug>/)
                                        # null si transversal (Areas, Resources, MOCs)
area: dev-tooling                       # null si Project, sinon slug d'Area
status: active                          # active | draft | archived | deleted
confidence: high                        # high | medium | low

# === RETRIEVAL TOKEN-EFFICIENT (clé pour RAG) ===
summary: "Refonte vault Obsidian en cerveau multi-projets auto-alimenté."
                                        # 1 phrase, 25 mots max
                                        # Lue par Claude AVANT d'ouvrir le corps
                                        # Densité d'info maximale
intent: decision                        # decision | reference | log | how-to | exploration | concept
entities: [obsidian, mcp, hooks, para, semantic-search]
                                        # 3-7 entités nommées, lowercase, kebab-case
                                        # Permet filtrage par sujet
topic_cluster: ai-memory-system         # 1 cluster sémantique (slug)
                                        # Permet groupage automatique

# === GRAPHE ===
related: ["[[20260425-2024-vault-base]]", "[[Decisions-Log]]"]
                                        # 2-5 wikilinks vers notes liées
moc: "[[_MOC-claude-system]]"           # MOC parent (1 seule)
source:                                 # Note source brute si dérivée (raw/, transcript)
                                        # null si note originale

# === TIERING (pour token-efficient retrieval) ===
tier: hot                               # hot | warm | cold
                                        # hot   = scanné chaque session du projet (~5k tokens budget)
                                        # warm  = frontmatter scanné, corps à la demande
                                        # cold  = search-only (semantic ou grep)

# === TEMPS ===
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07               # Mis à jour par hook PreToolUse Read

# === SEMANTIC SEARCH FUTURE-PROOF ===
embed_model_version: null               # null tant que pas embeddé
                                        # Sinon "nomic-embed-text-v2-moe" ou autre
embed_hash: null                        # SHA256 du contenu au moment de l'embed
                                        # Permet détection de re-embed nécessaire

# === TAGS ===
tags: [vault, architecture, ai-memory]  # 3 max, taxonomie fermée (cf. AGENTS.md)

# === CONTRÔLE IA ===
ai_writable: true                       # true = Claude peut éditer
                                        # false = lecture-seule (sources brutes, MOCs racine)
---
```

## Types autorisés

| Type | Usage | Dossier typique |
|---|---|---|
| `project` | Note de projet (état, décisions, livrables) | `10-Projects/<slug>/` |
| `area` | Responsabilité continue (sans deadline) | `20-Areas/<slug>/` |
| `concept` | Idée, modèle mental, abstraction réutilisable | `30-Resources/concepts/` ou `60-Permanent/` |
| `decision` | Décision technique avec rationale (ADR-light) | `10-Projects/<slug>/` ou `50-MOCs/Decisions-Log` |
| `bug` | Bug rencontré + solution + contexte | `10-Projects/<slug>/` |
| `workflow` | Procédure réutilisable | `30-Resources/workflows/` |
| `resource` | Doc externe, référence, pointeur | `30-Resources/` |
| `meeting` | Compte-rendu réunion / interaction | `00-Inbox/` puis dispatch |
| `daily` | Journal quotidien | `05-Daily/YYYY-MM-DD.md` |
| `moc` | Map of Content (hub navigable) | `50-MOCs/` ou `_MOC-*.md` racine projet |
| `schema` | Méta-schéma (comme ce fichier) | `90-Meta/schemas/` |
| `note` | Note atomique permanente (Zettelkasten) | `60-Permanent/` |

## Règles de validation

1. **`id` immuable** : ne change jamais après création. Si la note est renommée, le `id` reste.
2. **`summary` ≤ 25 mots** : densité d'info maximale, lu par Claude pour filtrer.
3. **`tags` ≤ 3** : taxonomie fermée définie dans `AGENTS.md` (cap. dur).
4. **`tier` cohérent avec usage** :
   - `hot` réservé aux notes consultées chaque session projet (~5-10 par projet max)
   - `warm` pour notes ouvertes ponctuellement
   - `cold` pour archives, références
5. **`related` ≥ 1** : sauf MOCs racine, toute note doit lier au moins une autre note (anti-orphelin).
6. **Wikilinks par `id` recommandés** quand collision de titres possible.

## Future-proof embedding

`embed_model_version` + `embed_hash` permettront, en Phase 4 (semantic search activée) :
- Re-embedder uniquement les notes dont le `embed_hash` ≠ SHA256 actuel du contenu
- Migration blue-green : embedder en parallèle avec un nouveau modèle, swap atomique quand validé
- Rollback possible vers ancien modèle si dégradation détectée

## Related

- [[2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau]] — Audit one-shot — déduplication 39 mémoires CC vs vault
- [[2026-05-10-registry-pattern-centralisateur-jeux-modulaires]] — Registry pattern — centralisateur jeux modulaires