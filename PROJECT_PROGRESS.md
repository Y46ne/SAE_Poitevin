# Suivi du projet — Stade Poitevin Tennis

> Source de vérité pour suivre l'avancement du projet.
> Mettre ce fichier à jour après chaque étape importante.

## Dernière mise à jour

- Date : 2026-10-20
- Branche de travail : `backend`
- Étape en cours : pages métier Django sans API REST

## Objectif du projet

Refondre le site du Stade Poitevin Tennis avec :

- un backend Django classique ;
- un frontend Vue 3 en JavaScript ;
- une base PostgreSQL en cible ;
- Django Admin pour gérer les contenus ;
- une interface moderne et responsive ;
- une section complète pour l'Open Masculin 86.

## Stack actuelle

| Partie | Technologie |
| --- | --- |
| Backend | Python 3.12, Django 5.1 |
| Frontend | Vue 3, Composition API, JavaScript |
| Base cible | PostgreSQL 16 |
| Base locale sans serveur | SQLite |
| Tests backend | Django TestCase, à compléter avec pytest si retenu |
| Tests frontend | Vitest, Vue Test Utils, Playwright |
| Administration | Django Admin |

Docker n'est pas utilisé actuellement. Le projet fonctionne localement avec SQLite si
`DATABASE_URL` n'est pas défini. PostgreSQL sera utilisé dès qu'un serveur sera disponible.

## Ce qui est terminé

### Architecture backend

- [x] Suppression de l'ancienne application `legacy`.
- [x] Découpage des modèles en apps Django métier :
  - `core`
  - `content`
  - `home`
  - `club`
  - `training`
  - `competition`
  - `partners`
  - `open86`
- [x] Séparation des modèles dans un fichier par modèle.
- [x] Migrations Django initiales.
- [x] Admin Django séparé par application.
- [x] Contraintes et validations métier principales.

### Modèles principaux

- [x] Médias et modèles communs.
- [x] Articles, catégories et tags.
- [x] Page d'accueil et blocs modulables.
- [x] Profil, histoire, management et documents du club.
- [x] Saisons, offres, tarifs et enseignants.
- [x] Compétitions, éditions, équipes, matchs, joueurs et palmarès.
- [x] Partenaires du club et de l'Open.
- [x] Éditions Open 86, éditos, photos, programme et tableaux.

### Rendu Django/Vue

- [x] Suppression de DRF, de CORS et des routes REST publiques.
- [x] Vue Django `/` pour la page d'accueil.
- [x] Transmission des blocs d'accueil au template avec `json_script`.
- [x] Bundle Vue produit par Vite dans les fichiers statiques Django.
- [x] Premier composant Vue d'accueil avec affichage interactif des blocs.
- [x] Tests Django de la vue d'accueil.
- [x] Pages Django du Club, des Articles, de la Formation, de la Compétition, des Partenaires et de l'Open 86.
- [x] Navigation globale vers toutes les sections publiques.
- [x] États vides propres quand aucun contenu n'est publié.

### Qualité

- [x] Noms de code en anglais simple et lisible.
- [x] Libellés administratifs et textes du site en français.
- [x] Secrets prévus via `.env`.
- [x] SQLite disponible sans serveur PostgreSQL.
- [x] Contrôle Django validé.
- [x] Migrations vérifiées.
- [x] Tests backend validés.
- [x] Ruff validé lors de la dernière vérification.

## État actuel

Le backend contient les modèles métier, l'administration Django et les pages publiques
de chaque domaine. Django rend les données et Vue enrichit l'accueil avec ses
interactions. Les détails et formulaires spécifiques pourront être enrichis ensuite.

## Prochaine étape

La prochaine étape est d'enrichir les pages métier avec leurs détails, médias et
formulaires, puis de préparer les tests navigateur.

## Étapes suivantes

1. Détails, médias et formulaires des pages métier.
2. Configuration des uploads et des fichiers médias.
3. Tests frontend et tests Playwright.
4. Gestion des permissions et du groupe bénévole.
5. CI et préparation du déploiement.

## Décisions prises

- Les modèles sont séparés par domaine métier.
- `legacy` a été supprimée car elle n'était plus utilisée.
- Les modèles sont dans un dossier `models/`, avec un fichier par modèle.
- Les fonctions et variables utilisent des noms anglais simples.
- PostgreSQL est la base cible.
- SQLite est utilisé localement sans serveur PostgreSQL.
- Docker est hors du projet pour le moment.
- Django rend les pages et fournit les données initiales aux composants Vue.
- Vite génère les fichiers statiques consommés par Django.

## Commandes de validation

Depuis `backend/` :

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
ruff check backend
```

Depuis `frontend/` :

```bash
npm run lint
npm run test:unit -- --run
npm run build
```

## Notes pour les prochains agents

- Lire `CLAUDE.md`, `.claude/` et ce fichier avant toute modification.
- Ne pas recréer une app `legacy`.
- Ne pas remettre Docker sans décision explicite.
- Garder les fonctions et variables en anglais simple.
- Garder les textes du site et les libellés admin en français.
- Ne pas recréer une API REST : utiliser les vues, templates et formulaires Django.
- Mettre à jour ce fichier après chaque étape importante.
