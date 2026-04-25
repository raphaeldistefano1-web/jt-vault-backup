---
type: concept
status: active
tags: [schema-org, seo, hotel]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Schema.org LodgingBusiness / BedAndBreakfast — type structuré pour hôtel/location vacances"
ai_writable: false
related:
  - "[[GEO-Generative-Engine-Optimization]]"
  - "[[Schema-FAQPage]]"
  - "[[Schema-TouristAttraction]]"
  - "[[Theme-jardintropical-child]]"
---

# 🏨 Schema.org — LodgingBusiness

## Définition

Type Schema.org pour un établissement d'hébergement. Sous-types pertinents pour [[Hotel-Le-Jardin-Tropical|Le Jardin Tropical]] :
- **`LodgingBusiness`** — générique
- **`BedAndBreakfast`** — petit hôtel familial avec petit-déj (le plus précis)
- **`Hotel`** — hôtel classique
- **`Resort`** — complexe avec activités
- **`VacationRental`** — pure location

## Champs essentiels (2026)

```json
{
  "@context": "https://schema.org",
  "@type": "BedAndBreakfast",
  "@id": "https://lejardintropical.fr/#hotel",
  "name": "Le Jardin Tropical",
  "description": "...",
  "url": "https://lejardintropical.fr/",
  "telephone": "+590 690 75 44 73",
  "email": "contact@lejardintropical.fr",
  "image": ["https://...jpg", ...],
  "logo": "https://.../logo.png",
  "priceRange": "€€",
  "currenciesAccepted": "EUR",
  "paymentAccepted": "Cash, Credit Card, Bank Transfer",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Bouillante",
    "postalCode": "97125",
    "addressRegion": "Guadeloupe",
    "addressCountry": "FR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 16.1273,
    "longitude": -61.7673
  },
  "checkinTime": "16:00",
  "checkoutTime": "12:00",
  "numberOfRooms": 14,
  "petsAllowed": false,
  "smokingAllowed": false,
  "starRating": {"@type": "Rating", "ratingValue": "..."},
  "amenityFeature": [
    {"@type": "LocationFeatureSpecification", "name": "Piscine", "value": true},
    ...
  ],
  "availableLanguage": ["fr", "en"],
  "sameAs": [
    "https://www.facebook.com/...",
    "https://www.tripadvisor.fr/...",
    "https://www.booking.com/..."
  ]
}
```

## Champs souvent oubliés (mais critiques)

- **`priceValidUntil`** sur les `Offer` — Google Search Console signale "Missing field" sinon. Cf. [[Decision-Schema-Offer-priceValidUntil]]
- **`@id`** stable cross-pages — permet le pattern `@graph` qui unifie l'entité
- **`amenityFeature`** détaillé (pas juste "WiFi", lister 8-10 features)
- **`sameAs`** vers profils sociaux + agrégateurs (Google Maps, TripAdvisor) — GEO booster

## Implementation Le Jardin Tropical

Le [[Theme-jardintropical-child|theme custom]] injecte déjà un schema `LodgingBusiness` ULTRA complet :
- name, description, telephone, email, priceRange, image
- address PostalAddress complet
- geo (16.1273, -61.7673)
- numberOfRooms 14
- 8 amenityFeature détaillées
- checkinTime / checkoutTime
- availableLanguage FR + EN
- paymentAccepted, currenciesAccepted
- smokingAllowed, petsAllowed
- sameAs Facebook/Instagram/TripAdvisor

C'est pour ça qu'on a [[Decision-Mu-plugin-vs-RankMath|décidé de ne PAS installer Rank Math]] — il aurait écrasé/dupliqué.

## Schemas additionnels (ajoutés via [[Mu-plugin-jt-seo-extras]])

- **[[Schema-FAQPage]]** sur /faq/
- **`Offer.priceValidUntil`** sur la home
- **`BreadcrumbList`** sur pages internes
- **[[Schema-TouristAttraction]]** sur /reserve-cousteau/
- **`TouristTrip`** sur /reserve-cousteau/

## Liens

- Spec : https://schema.org/LodgingBusiness
- Validation : https://validator.schema.org/
- Rich Results Test : https://search.google.com/test/rich-results
