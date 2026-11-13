# Produit (PRODUCT.fr.md)

## Plateforme

Web

## Utilisateurs cibles

L'utilisateur principal est un créateur individuel en auto-hébergement : il déploie lui-même la solution et réalise de manière autonome l'ensemble du processus, du roman, scénario abouti ou ressources produits jusqu'au film final. Les décisions d'interface prennent ce profil comme référence par défaut.

Deux axes d'extension connus sont préservés dans la conception :

- **Échelle** : la collaboration multi-utilisateurs et la gestion des rôles ne sont pas fournies pour le moment ; la structure est néanmoins conçue en prévision d'une utilisation éventuelle à plusieurs.
- **Distribution** : le nom de marque est configurable dynamiquement, et l'interface est compatible avec un encapsulage de type client de bureau, en conservant le même système de design.

## Finalité du produit

Organiser l'analyse de contenu, la gestion des ressources, le storyboarding, la génération multimédia, le suivi des coûts et l'export dans une chaîne de production vidéo inspectable et résiliente aux interruptions.
L'état de succès est le suivant : un créateur parcourt de façon autonome l'intégralité du flux, des fichiers sources au film final ou au brouillon Jianying, en pouvant à chaque étape vérifier l'avancement, modifier les résultats et contrôler les coûts réels.

## Positionnement

Trois mécanismes de différenciation, par ordre d'importance :

1. **L'Agent au cœur du flux** : planification du script, ressources, storyboard, génération jusqu'au rendu final peuvent être orchestrés par un Agent, offrant un niveau élevé d'automatisation avec un coût d'apprentissage réduit.
2. **Fournisseurs modulables** : les capacités de texte, d'image, de vidéo et de synthèse vocale (TTS) sont choisies librement par l'utilisateur parmi les fournisseurs et modèles, avec coexistence de fournisseurs intégrés et personnalisés.
3. **Open source, auto-hébergé et livrables Jianying** : les données restent sur la machine de l'utilisateur et les résultats peuvent être exportés sous forme de brouillons Jianying pour être peaufinés manuellement.

## Contexte d'exploitation

- **Prérequis d'utilisation** : aucune configuration complexe n'est requise pour créer un projet. Avant de lancer la production, il convient de configurer dans les paramètres l'Agent et les capacités effectives (texte, image, vidéo, TTS).
- **Chaîne de production** : Fichiers sources ou ressources produits → Analyse de contenu et planification → Personnages, décors, accessoires, produits → Découpage en épisodes et scénario structuré → Images de storyboard ou unités vidéo → Segments vidéo et pistes de narration → Rendu final ou export de brouillon Jianying. Chaque étape peut être orchestrée par l'Agent ou inspectée, éditée et régénérée par le créateur.
- **Mode de déploiement** : service auto-hébergé à compte administrateur unique.
- **Export Jianying** : orienté vers l'édition Chine continentale de Jianying ; la compatibilité avec CapCut n'a pas été validée, l'interface indique « supporte uniquement Jianying ».

## Capacités et contraintes

- **Types de création** : Voix off/Narration, Fiction narrative (drame), Publicité/Court métrage. Modes de génération : Storyboard vers vidéo, Vidéo de référence vers vidéo. Non modifiable après création du projet.
- **Tâches annulables** : les tâches de génération peuvent être annulées. La reprise après interruption est conditionnelle : seules les tâches vidéo dont le fournisseur supporte la vérification de statut et dont l'ID distant est enregistré reprendront automatiquement. Les générations d'images, de doublage et les autres tâches vidéo sont marquées en échec et attendent une relance manuelle, afin d'éviter une double facturation auprès du fournisseur. L'interface affiche en continu l'état d'avancement, les blocages et les échecs nécessitant une intervention.
- **Évaluation préalable aux lots** : une validation préalable est requise avant le lancement groupé de générations vidéo (autorisé, à confirmer, bloqué) ; cette évaluation n'est pas appliquée aux lots d'images ou de doublages audio.
- Les définitions complètes des termes, machines à états et sémantiques de données figurent dans `GLOSSARY.md` et `docs/adr/`.

## Engagements de marque

- Nom : ArcReel, slogan par défaut : « Espace de travail de création vidéo IA orchestré par Agent » (`BRAND.tagline`).
- **Nom de marque configurable** : le nom et le slogan proviennent de `BRAND` dans `frontend/src/branding.ts` et des espaces réservés `[[brand]]` dans les ressources i18n ; ils peuvent être surchargés à la compilation.
- **Le glossaire fait foi pour le vocabulaire d'interface** : les termes d'interface s'alignent rigoureusement sur `GLOSSARY.md`.

## Principes de produit

1. **La validation prime sur l'automatisation** : les résultats automatiques sont par défaut visibles, modifiables et régénérables individuellement.
2. **Le coût précède l'action** : toute action consommant des crédits affiche son périmètre d'impact et son coût estimé avant soumission, particulièrement pour les opérations par lot.
3. **Le statut du serveur fait autorité** : la progression, les blocages et les états des ressources proviennent tous de l'évaluation du serveur ; l'interface ne déduit rien de la simple présence d'un fichier.
4. **Réalisable par une seule personne** : tous les flux critiques peuvent être menés à bien par un créateur solitaire.

## Accessibilité et inclusion

- La synchronisation multilingue exhaustive est une exigence stricte : tous les textes orientés utilisateur doivent posséder une clé de traduction dans l'ensemble des langues supportées. Les mises en page réservent des marges pour les textes plus longs dans certaines langues.

