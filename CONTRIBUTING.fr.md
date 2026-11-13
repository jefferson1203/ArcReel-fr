# Guide de contribution (CONTRIBUTING.fr.md)

Bienvenue sur le projet ArcReel ! Toutes les contributions sous forme de code, de signalement de bugs ou de suggestions d'améliorations sont les bienvenues.

Les contributions visant principalement la promotion d'un service commercial (comme l'intégration d'un nouveau service tiers non générique ou l'ajout de liens promotionnels dans la documentation) ne passent pas par les Pull Requests et seront fermées ; pour les partenariats, contactez support@arc-reel.com.

Les issues étiquetées `ready-for-agent` comportent des spécifications prêtes pour les agents de codage automatisés. Les PR externes sur ces tickets ne sont pas acceptées.

Avant d'entamer le développement d'une fonctionnalité majeure ou d'une refonte d'envergure, nous vous conseillons d'ouvrir une issue pour échanger sur la direction technique.

Avant la fusion d'une Pull Request, l'auteur doit signer le Contrat de Licence Contributeur (CLA), géré directement en commentaire de PR par CLA Assistant.

ArcReel est conçu pour faciliter le travail avec des agents d'IA de codage. Le fichier `AGENTS.md` à la racine (dont `CLAUDE.md` est un lien symbolique) sert de point d'entrée pour les agents.

## Environnement de développement local

```bash
# Prérequis : Python 3.12+, Node.js 24.12.0+, uv, pnpm (ffmpeg s'installe via la dépendance Python imageio-ffmpeg)
# Version Node pour le site de documentation : fixée dans website/.node-version
# Systèmes supportés : Linux / macOS / Windows WSL2 (sur Windows natif, le bac à sable est restreint à une liste blanche)

# Installation des dépendances
uv sync
cd frontend && pnpm install && cd ..

# Installation des hooks pre-commit (ruff / eslint / actionlint / zizmor)
uv run pre-commit install

# Initialisation de la base de données
uv run alembic upgrade head

# Lancement du backend (Terminal 1)
# Note : il est indispensable de restreindre le rechargement avec --reload-dir pour éviter de scanner l'ensemble des répertoires
uv run uvicorn server.app:app --reload --reload-dir server --reload-dir lib --port 1241

# Lancement du frontend (Terminal 2)
cd frontend && pnpm dev

# Accès à l'application : http://localhost:5173
```

### Site de documentation

Le répertoire `website/` est un paquet autonome avec son propre fichier de verrouillage :

```bash
cd website && pnpm install

pnpm start        # Prévisualisation de développement
pnpm build        # Construction multilingue (liens morts ou ancres invalides bloquent le build)
pnpm typecheck
pnpm lint         # ESLint
pnpm format       # Formatage avec Prettier
pnpm check        # Vérification globale de cohérence
```

## Tests

Pour la boucle de développement et le passage des contrôles de qualité avant soumission, consultez `AGENTS.md` et `docs/agents/testing.md` :

```bash
# Exécution du script de validation avant push
uv run python scripts/gate.py --changed
```

### Tests d'intégration et end-to-end frontend

Le dossier `frontend/e2e/` contient la suite de tests Playwright pour le frontend. Il teste plusieurs résolutions d'écran (de 1024×600 à 2560×1440) et valide l'accessibilité selon WCAG 2.2 AA.

## Qualité du code

Les standards de développement sont décrits dans [`CODING_STANDARDS.md`](CODING_STANDARDS.md) et les documents spécialisés dans `docs/standards/`.

## Flux de travail

### Stratégie de branches (Trunk-based development)

- Seule la branche `main` est permanente. Tout travail s'effectue sur une branche courte créée à partir du dernier `main` et fusionnée par Pull Request.
- Les pushes directs sur `main` sont interdits.

### Nommage des branches

Format : `<type>/<slug>` avec les préfixes conventionnels :
- `feat/` — Nouvelle fonctionnalité
- `fix/` — Correction de bogue
- `refactor/` — Refactorisation
- `docs/` — Documentation
- `chore/` — Tâches d'outillage ou de maintenance
- `ci/` — Intégration continue
- `test/` — Tests

### Format des commits

Les messages de commit suivent la spécification [Conventional Commits](https://www.conventionalcommits.org/) :
```text
feat(scope): résumé en français ou en anglais
fix(scope): description de la correction
```

## Processus de versionnement

Les numéros de versions et le journal des modifications (`CHANGELOG.md`) sont maintenus automatiquement par **release-please**. Les développeurs ne doivent pas modifier manuellement les versions dans `pyproject.toml` ou `frontend/package.json`.

