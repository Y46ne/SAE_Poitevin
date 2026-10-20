# Stade Poitevin Tennis

Refonte du site du Stade Poitevin Tennis avec Django, Vue 3 et SQLite en
développement.

## Reprendre le projet

Lire d'abord [PROJECT_HANDOFF.md](PROJECT_HANDOFF.md), puis
[PROJECT_PROGRESS.md](PROJECT_PROGRESS.md).

## Lancer le projet

```bash
cd frontend
npm install
npm run build

cd ../backend
../.venv/bin/python manage.py migrate
../.venv/bin/python manage.py runserver
```

Le site est disponible sur <http://127.0.0.1:8000/>.

L'administration est disponible sur
<http://127.0.0.1:8000/admin/>.

## Architecture

Le projet utilise Django pour rendre les pages et Vue pour les interactions
nécessaires. Il n'y a volontairement plus d'API REST publique.

Les modèles et l'administration se trouvent dans `backend/apps/`. Les routes
publiques sont dans `backend/apps/core/site_urls.py` et les vues communes dans
`backend/apps/core/site_views.py`.

## Tests

```bash
cd backend
../.venv/bin/python manage.py check
../.venv/bin/python manage.py test
../.venv/bin/ruff check .

cd ../frontend
npm run test:unit -- --run
npm run lint
npm run build
```