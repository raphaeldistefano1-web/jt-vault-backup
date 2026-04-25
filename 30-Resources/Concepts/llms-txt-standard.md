---
type: concept
status: active
tags: [llms-txt, geo, llm, seo]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Standard llms.txt — index markdown d'un site pour les LLMs, façon robots.txt / sitemap.xml"
ai_writable: false
related:
  - "[[GEO-Generative-Engine-Optimization]]"
  - "[[Robots-txt-LLM-Aware]]"
  - "[[Site-WordPress-Optimisation-2026-04-25]]"
aliases: ["llms.txt"]
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
