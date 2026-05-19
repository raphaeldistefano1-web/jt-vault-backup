---
applies_to: Cyclone GTM + future SaaS Antilles (pivot oct 2026)
backlinks:
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-10-accès-données-hbook-source-unique-de-vérité
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- '2026-05-17'
- business-plan
date: 2026-05-18
session_id: cyclone-gtm-2026-05-18
status: pending
target: workflow
type: improvement
urgency: medium
---

# Couplage monétisation ↔ qualité des avis ↔ ASO (insight réutilisable)

## Constat
Lors du brainstorm GTM Cyclone (app freemium + abo, croissance 100 % ASO), la revue
adversariale `idea-critic` a mis en évidence une boucle négative non vue initialement :
un abo court (hebdo 2,99 € sur une app d'usage épisodique) génère des reprélèvements
oubliés → demandes de remboursement → avis 1★. Or le **nombre et la note des avis sont
un input direct du classement ASO**. La monétisation empoisonne donc le canal
d'acquisition dont dépend toute la stratégie. Trois variables qu'on traitait comme
indépendantes (pricing, qualité des avis, ranking store) sont en réalité fortement
couplées, négativement, dès que le moteur de croissance repose sur l'ASO.

## Pourquoi c'est utile
Cet insight ne vaut pas que pour Cyclone : **toute app/SaaS distribuée via store et
acquise par ASO** (y compris le futur PMS/SaaS Antilles s'il passe par les stores) est
exposée au même couplage. Le traiter comme une règle de conception évite de répéter
l'erreur : on ne choisit pas un pricing d'abonnement sans modéliser son effet sur le
taux de remboursement et la note moyenne, donc sur l'acquisition.

## How to apply
1. Pour tout produit store-distribué + ASO-driven : avant de figer une grille d'abo,
   estimer `taux de reprélèvement non désiré` × `propension à laisser 1★` et l'intégrer
   au modèle d'acquisition (pas seulement à l'ARPU). (~30 min de modélisation.)
2. Instrumenter dès le J1 les métriques `trial→refund` et `reprélèvement→avis négatif`
   comme métriques de **croissance**, pas seulement de finance. (Inclus dans l'analytics.)
3. Mitigations standard à prévoir par défaut : écran de rappel de prélèvement avant fin
   d'essai, UX d'annulation sans friction, framing d'usage explicite (« pour ta soirée »).
4. Réutiliser cette note comme checklist au moment du design pricing de la SaaS Antilles
   (oct 2026). Acteur : Raphaël / Claude lors du design GTM de chaque produit store.