---
type: concept
status: active
tags: [schema-org, faq, geo]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Schema FAQPage — booster majeur Google AI Overviews et citations LLM"
ai_writable: false
related:
  - "[[Schema-org-LodgingBusiness]]"
  - "[[GEO-Generative-Engine-Optimization]]"
  - "[[Mu-plugin-jt-seo-extras]]"
id: 202604252028-schema-faqpage
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "Type Schema.org qui structure une page FAQ en Q/R machine-readable. Booster majeur pour :"
entities: [documentation, reference]
topic_cluster: wordpress-schema
intent: concept
tier: warm
---

# ❓ Schema.org — FAQPage

## Principe

Type Schema.org qui structure une page FAQ en Q/R machine-readable. **Booster majeur** pour :
- Google AI Overviews (réponses générées en SERP)
- Citations dans ChatGPT search / Perplexity / Gemini
- Rich snippets "People Also Ask"

## Format JSON-LD

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question 1 ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Réponse complète en 1-3 phrases."
      }
    },
    {
      "@type": "Question",
      "name": "Question 2 ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "..."
      }
    }
  ]
}
```

## Bonnes pratiques 2026

- **6-12 Q/R** typiques (au-delà devient bruit)
- **Réponse directe** en 1-3 phrases
- **Données factuelles** (distances, prix, horaires) — les LLM citent ces réponses verbatim
- **Cohérence** entre la Q/R en JSON-LD et le contenu visible HTML (pas de cloaking, Google demote)

## Implementation Le Jardin Tropical

Cf. [[Mu-plugin-jt-seo-extras]] section 5 :
- 12 Q/R injectées en JSON-LD sur `/faq/`
- Contenu visible identique sur la page
- Couvre : distance Cousteau/aéroport, horaires, animaux, parking, paiement, langues, piscine, restauration, activités, annulation, WiFi

Cf. [[Page-FAQ-2026-04-25]].

## Pièges

- ⚠️ **Google ne sert plus de rich snippet FAQPage classique** depuis août 2023 (sauf sites government / health). MAIS continue à **utiliser** les data dans AI Overviews et knowledge graph.
- Donc : ne pas espérer de "carrousel FAQ" en SERP, mais **gain GEO réel** sur citations LLM.

## Liens

- [[GEO-Generative-Engine-Optimization]]
- [[Page-FAQ-2026-04-25]]
- Spec : https://schema.org/FAQPage
