---
ai_writable: false
aliases:
- GEO
backlinks:
- Decision-Robots-txt-LLM-Aware
- Mu-plugin-jt-seo-extras
- Robots-txt-LLM-Aware
- Schema-FAQPage
- Schema-org-LodgingBusiness
- llms-txt-standard
created: 2026-04-25
description: GEO = optimisation pour être cité par les moteurs LLM (ChatGPT, Perplexity,
  Google AI Overviews)
embed_hash: null
embed_model_version: null
entities:
- documentation
- llm
- reference
id: 202604252026-geo-generative-engine-optimization
intent: concept
last-accessed: 2026-04-25
related:
- '[[llms-txt-standard]]'
- '[[Robots-txt-LLM-Aware]]'
- '[[Schema-org-LodgingBusiness]]'
- '[[Schema-FAQPage]]'
relevance: high
status: active
summary: Generative Engine Optimization = ensemble de pratiques pour être cité par
  les moteurs LLM ChatGPT search, Perplexity, Go…
tags:
- geo
- llm
- seo
tier: warm
topic_cluster: wordpress-seo
type: concept
updated: 2026-04-25
---

# 🤖 GEO — Generative Engine Optimization

## Définition

**Generative Engine Optimization** = ensemble de pratiques pour **être cité** par les moteurs LLM (ChatGPT search, Perplexity, Google AI Overviews, Gemini, Claude search) quand un user pose une question dont ton contenu est pertinent.

Différence avec SEO classique : SEO veut être **cliqué** (top des SERPs), GEO veut être **cité** dans la réponse générée par l'IA.

## Stratégies clés 2026

### 1. Robots.txt sélectif (cf. [[Robots-txt-LLM-Aware]])

- **Bloquer les crawlers d'entraînement** (qui aspirent pour entraîner les modèles, sans citer) : `GPTBot`, `Google-Extended`, `CCBot`, `ClaudeBot`, `anthropic-ai`, `Bytespider`, `Amazonbot`, `FacebookBot`
- **Autoriser les crawlers de retrieval** (qui citent quand un user pose une question) : `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `Perplexity-User`, `Google-CloudVertexBot`, `Applebot-Extended`

Logique : **maximiser citations** sans donner gratuitement le contenu pour entraînement.

### 2. Schema.org riche

- **Schema spécifique** au domaine (pour Le Jardin Tropical : [[Schema-org-LodgingBusiness|LodgingBusiness]] + `BedAndBreakfast`)
- **FAQPage** schema avec Q/R structurées — booster majeur Google AI Overviews
- **Offer.priceValidUntil** — fix warning GSC + débloque rich snippets
- **BreadcrumbList** + **TouristAttraction** + **TouristTrip** pour entité graph
- Pattern **`@graph` + `@id`** cross-pages → entité unifiée

### 3. Contenu "réponse-friendly"

- H2 = question, paragraphe ouvre par la **réponse directe** en 1-2 phrases (les LLM extraient les 200 premiers tokens d'un H2)
- **Données factuelles redondantes** en clair texte ET schema (distance aéroport, prix, équipements)
- **Citations sortantes** vers sources d'autorité (Wikipedia, Wikidata, Parc National, Météo France)

### 4. Présence sur agrégateurs cités

Les LLMs s'appuient sur Booking.com, TripAdvisor, Wikipedia, Google Maps, Atout France pour les recos hôtelières. **Être présent** sur ces sources externes augmente ta visibilité dans les réponses LLM.

### 5. [[llms-txt-standard|llms.txt]] à la racine

Pas critique (peu adopté en avril 2026) mais coût nul, à mettre en place.

## Implementation Le Jardin Tropical

Cf. [[Site-WordPress-Optimisation-2026-04-25]] — toutes ces stratégies appliquées le 2026-04-25 :
- Robots.txt LLM-aware (53 lignes)
- llms.txt physique racine
- Schema FAQPage 12 Q/R
- Schema Offer.priceValidUntil
- Schema BreadcrumbList automatique
- Schema TouristAttraction + TouristTrip sur /reserve-cousteau/
- @id + @graph cross-pages (en partie)

## Pièges 2026

- Bloquer GPTBot **avant** que ton contenu n'ait servi à entraîner = trop tard pour ce qui a déjà été aspiré
- Trop de schema → Google demote pour "self-serving"
- Citations sortantes vers concurrents → modérément
- Sur-mention de mots-clés = LLM detect spam pattern

## Liens

- [[Site-WordPress]]
- [[Robots-txt-LLM-Aware]]