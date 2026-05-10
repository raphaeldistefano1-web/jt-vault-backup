---
ai_writable: false
aliases:
- llms.txt
backlinks:
- GEO-Generative-Engine-Optimization
- Robots-txt-LLM-Aware
- _VAULT-INDEX
created: 2026-04-25
description: Standard llms.txt — index markdown d'un site pour les LLMs, façon robots.txt
  / sitemap.xml
embed_hash: null
embed_model_version: null
entities:
- documentation
- llm
- site-wordpress
id: 202604252026-llms-txt-standard
intent: concept
last-accessed: 2026-04-25
related:
- '[[GEO-Generative-Engine-Optimization]]'
- '[[Robots-txt-LLM-Aware]]'
- '[[Site-WordPress-Optimisation-2026-04-25]]'
relevance: medium
status: active
summary: Fichier markdown à la racine d'un site web /llms.txt qui sert d'index curé
  pour les LLMs. Le format markdown est lisible…
tags:
- llms-txt
- geo
- llm
- seo
tier: warm
topic_cluster: ai-integration
type: concept
updated: 2026-04-25
---

# 📄 llms.txt — standard

## Définition

Fichier markdown à la racine d'un site web (`/llms.txt`) qui sert d'**index curé pour les LLMs**. Le format markdown est lisible par tous les LLMs sans parsing complexe.

Différence avec `robots.txt` (instructions pour crawlers) et `sitemap.xml` (URLs structurées) : llms.txt est un **résumé human-readable** des pages clés avec descriptions.

## Adoption 2026

- Standard non officiel ([llmstxt.org](https://llmstxt.org/))
- Pas (encore) adopté formellement par OpenAI / Anthropic / Google en avril 2026
- **Utilisé par Mintlify, Perplexity** (custom retrievers) et certains agents
- Coût d'adoption nul → ROI faible mais positif

## Format type

```markdown
# Nom du site

> Une-phrase qui décrit ce que c'est.

Paragraphe d'intro, 5-10 lignes max.

## Pages principales

- [Titre 1](url1): description
- [Titre 2](url2): description

## Caractéristiques

- Type, capacité, prix indicatif, etc.

## Optional

- [Blog](url): articles
- [English version](url-en): version anglophone
```

## Différence avec [[Vault-Setup|vault Obsidian]]

- **llms.txt** = pour les LLMs **externes** qui crawlent ton site
- **Vault Obsidian** + AGENTS.md = pour les LLMs que tu **utilises toi-même** (Claude, ChatGPT, etc.)

Les deux sont complémentaires.

## Implementation Le Jardin Tropical

Site WP : `/srv/vault-jardin-tropical/.../site-content/llms.txt` (généré). Servi par Apache à `https://wp-46-202-171-204.nip.io/llms.txt` (cf. [[Site-WordPress-Optimisation-2026-04-25]]).

Contenu : 22 pages WP indexées avec descriptions, infos hôtel (capacité, GPS, prix, langues), liens externes (FB/Insta/TripAdvisor).

## Liens

- [[GEO-Generative-Engine-Optimization]]
- [[Site-WordPress]]
- Spec : https://llmstxt.org