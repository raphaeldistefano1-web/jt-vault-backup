---
ai_writable: false
backlinks:
- Decision-Robots-txt-LLM-Aware
- GEO-Generative-Engine-Optimization
- Mu-plugin-jt-seo-extras
- llms-txt-standard
created: 2026-04-25
description: 'Stratégie robots.txt 2026 : bloquer crawlers d''entraînement LLM, autoriser
  retrieval bots'
embed_hash: null
embed_model_version: null
entities:
- documentation
- llm
- reference
id: 202604252028-robots-txt-llm-aware
intent: concept
last-accessed: 2026-04-25
related:
- '[[GEO-Generative-Engine-Optimization]]'
- '[[llms-txt-standard]]'
- '[[Mu-plugin-jt-seo-extras]]'
relevance: high
status: active
summary: 'Les crawlers IA se divisent en 2 catégories :'
tags:
- robots-txt
- geo
- llm
- seo
tier: warm
topic_cluster: wordpress-seo
type: concept
updated: 2026-04-25
---

# 🤖 robots.txt LLM-aware

## Logique 2026

Les crawlers IA se divisent en 2 catégories :

### 🚫 Crawlers d'entraînement (à BLOQUER)

Ils aspirent ton contenu pour **entraîner** les modèles LLM, sans te citer en retour. Tu donnes gratuitement ton contenu sans bénéfice.

- `GPTBot` (OpenAI training)
- `Google-Extended` (Gemini training)
- `CCBot` (Common Crawl, training data)
- `ClaudeBot` (Anthropic training)
- `anthropic-ai` (Anthropic, ancien)
- `Bytespider` (ByteDance)
- `Amazonbot` (Amazon)
- `FacebookBot` (Meta training)

### ✅ Crawlers de retrieval (à AUTORISER)

Ils crawlent **à la demande** quand un user pose une question dont ton contenu est pertinent. Ils citent leurs sources.

- `OAI-SearchBot` (ChatGPT search)
- `ChatGPT-User` (ChatGPT browse à la demande)
- `PerplexityBot` (Perplexity index)
- `Perplexity-User` (Perplexity à la demande)
- `Google-CloudVertexBot` (Vertex AI retrieval)
- `Applebot-Extended` (Apple Intelligence retrieval)

## Format robots.txt

```
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: Amazonbot
Disallow: /

User-agent: FacebookBot
Disallow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-CloudVertexBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://lejardintropical.fr/wp-sitemap.xml
```

## Implementation Le Jardin Tropical

Cf. [[Mu-plugin-jt-seo-extras]] section 1 — `add_filter('robots_txt', ...)` qui ajoute ces règles automatiquement.

Test : `curl https://wp-46-202-171-204.nip.io/robots.txt` → 53 lignes.

## Limites

- **Politesse, pas barrière** : un crawler peut ignorer robots.txt techniquement. Mais OpenAI/Google/Anthropic respectent (réputationnel).
- **Bloquer GPTBot trop tard** : si ton contenu a déjà été aspiré avant le block, c'est trop tard — il est déjà dans le training data.
- **Compromis** : bloquer training = perte potentielle de visibilité dans les modèles **génératifs** (ce que ChatGPT "sait" sans search). À évaluer au cas par cas.

## Décision Le Jardin Tropical

Cf. [[Decision-Robots-LLM-Aware]] — choix de bloquer training + autoriser retrieval.

## Liens

- [[GEO-Generative-Engine-Optimization]]
- [[Site-WordPress-Optimisation-2026-04-25]]