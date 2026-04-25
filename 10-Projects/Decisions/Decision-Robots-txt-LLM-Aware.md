---
type: decision
status: accepted
tags: [decision, geo, llm, seo]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Stratégie GEO : bloquer crawlers d'entraînement LLM, autoriser retrieval bots — maximiser citations sans donner contenu pour entraînement"
ai_writable: false
related:
  - "[[Robots-txt-LLM-Aware]]"
  - "[[GEO-Generative-Engine-Optimization]]"
  - "[[Mu-plugin-jt-seo-extras]]"
context: "Optim site WP 2026-04-25 — décision stratégique GEO"
chosen: "Bloquer training crawlers, autoriser retrieval crawlers"
alternatives: ["Tout bloquer", "Tout autoriser", "Bloquer training + retrieval"]
---

# 🎯 Decision : robots.txt LLM-aware

## Contexte

Avec la prolifération des crawlers IA en 2026 (GPTBot, Google-Extended, ClaudeBot, PerplexityBot, etc.), 4 stratégies possibles pour le `robots.txt`.

## Options considérées

### A. Tout autoriser (status quo)
- ✅ Maximise visibilité dans les modèles génératifs ("ChatGPT sait que tu existes")
- ❌ Donne le contenu gratuitement pour entraînement, pas de citation systématique
- ❌ "Vol" propriétés intellectuelles

### B. Tout bloquer
- ✅ Privacy max
- ❌ Perte totale de visibilité IA, ChatGPT/Perplexity ne te citent JAMAIS
- ❌ Mauvais pour SEO/business

### C. Bloquer training + retrieval
- ✅ Contrôle max
- ❌ Tu te coupes des citations LLM = perte de trafic

### D. **Bloquer training, autoriser retrieval** ✅

Logique : **maximiser citations** sans donner gratuitement le contenu pour entraînement.

#### Bloqués (training)
- `GPTBot` (OpenAI training)
- `Google-Extended` (Gemini training)
- `CCBot` (Common Crawl)
- `ClaudeBot` (Anthropic training)
- `anthropic-ai`
- `Bytespider`
- `Amazonbot`
- `FacebookBot`

#### Autorisés (retrieval)
- `OAI-SearchBot` (ChatGPT search)
- `ChatGPT-User` (ChatGPT browse à la demande)
- `PerplexityBot`
- `Perplexity-User`
- `Google-CloudVertexBot`
- `Applebot-Extended`

## Choix : **D**

## Rationale

- **Avoir le beurre et l'argent du beurre** : pas dans le training data, mais cité quand on demande
- Pour un hôtel : **citation > présence dans modèles génératifs**. Un user qui demande "hôtel Bouillante" à Perplexity et reçoit notre nom + lien convertit. Un user qui demande à ChatGPT sans search ne convertit pas.
- **Réputationnel** : OpenAI/Google/Anthropic respectent robots.txt → effective.

## Limites

- Politesse, pas barrière : un crawler peut ignorer techniquement (mais les majors respectent)
- Si contenu déjà aspiré avant le block, c'est trop tard

## Implementation

Cf. [[Mu-plugin-jt-seo-extras]] section 1 — `add_filter('robots_txt', ...)`.

53 lignes finales dans le robots.txt.

## Liens

- [[Robots-txt-LLM-Aware]]
- [[GEO-Generative-Engine-Optimization]]
