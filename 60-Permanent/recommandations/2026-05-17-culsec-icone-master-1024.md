---
applies_to: culsec — assets/icon-only.png (soumission App Store Phase 5)
backlinks:
- 2026-05-12-refonte-visuelle-non-fialisée-vs-moc-du-projet-cul
date: 2026-05-17
session_id: bff4c7c6-1b83-4749-a5d0-ac39d084f2de
status: pending
target: pms
type: improvement
urgency: medium
---

# Cul Sec — sourcer un master d'icône ≥1024 avant soumission App Store

## Constat

Le seul master d'icône existant est un PNG **512×512** (embarqué dans
`public/icon.svg`, qui n'est PAS du vrai vectoriel — juste un `<image>` base64).
Aucun fichier ≥1024 ni vectoriel. La prép Phase 3 (`assets/icon-only.png`) est
un **upscale 512→1024 via sips** : format App Store conforme (1024², sans alpha)
mais rendu légèrement mou aux grandes tailles (fiche App Store, Réglages iOS).

## Pourquoi c'est utile / problématique

Apple ne rejette pas un icône upscalé, mais l'icône est l'élément de marque le
plus vu (fiche store, springboard, réglages). Un rendu mou pénalise la
conversion ASO et donne une impression "pas pro" sur un produit payant futur.
Coût de correction quasi nul si on retrouve/regénère le master ; coût d'image
élevé si on shippe mou. Medium (pas bloquant pour TestFlight interne, bloquant
qualité pour soumission publique Phase 5).

## How to apply

1. Récupérer le master original de l'icône "ACID NIGHT" (verre néon vert +
   sourire — cf. commit master `feat : icône app A · ACID NIGHT`). Chercher le
   fichier de design source (Figma/Canva/SVG) ; sinon regénérer en ≥1024 natif
   ou en vectoriel propre.
2. Remplacer `assets/icon-only.png` (1024², sans alpha, fond opaque).
3. Si splash concerné : refaire aussi `assets/splash.png` depuis le nouveau logo.
4. Regénérer : `npx @capacitor/assets generate --ios` puis vérifier l'AppIcon
   set dans Xcode. ~30 min si master dispo, +1 h si recréation. Qui : Raphaël
   (sourcing design) + Claude (intégration/regénération).