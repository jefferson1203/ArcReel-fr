# Architecture de la documentation ArcReel (docs/README.fr.md)

Ce répertoire contient la documentation interne de conception, d'architecture et de développement d'ArcReel.

## Structure des répertoires

- **`docs/adr/`** : Architecture Decision Records (ADR). Historique complet et formel des décisions de conception et de choix technologiques du projet.
- **`docs/agents/`** : Guides et règles de travail pour les agents d'intelligence artificielle autonomes intervenant sur le dépôt :
  - `escalation.md` : Critères pour solliciter l'utilisateur humain ou décider en autonomie.
  - `testing.md` : Guide d'exécution et choix des suites de tests.
  - `lessons.md` : Retours d'expérience et auto-contrôles de fin de tâche.
  - `issue-tracker.md` : Gestion des tickets et étiquettes GitHub.
- **`docs/standards/`** : Normes de codage et d'ingénierie logicielle (indexées dans `CODING_STANDARDS.md`) :
  - `copy.md` : Règles de rédaction et terminologie.
  - `docs.md` : Conventions de documentation publique.
  - `general.md` : Bonnes pratiques transversales.
- **`docs/research/`** : Études de l'état de l'art, benchmarks et recherches techniques préliminaires.
- **`docs/security/`** : Modèle de menace de sécurité (`threat-model.md`).
- **`docs/api-docs/`** : Documentation technique des points d'accès des fournisseurs.

## Documentation publique

La documentation publique destinée aux utilisateurs et aux opérateurs d'ArcReel se trouve dans `website/docs/` et est déployée sur [docs.arc-reel.com](https://docs.arc-reel.com).

