# Application de Réservation de Bar

Ce dépôt contient une application de réservation de bar avec une interface web client développée en Vue.js et une API backend développée en Python avec le framework FastAPI.

## Architecture

L'application suit une architecture client-serveur, avec le front-end et le back-end séparés dans des dossiers distincts.

- Le dossier `front` contient le code source de l'application front-end développée en Vue.js. Il utilise le framework Vue 3 et est configuré avec Vue Router pour la gestion des routes. Le code source se trouve dans le dossier `src`.

- Le dossier `back` contient le code source de l'API backend développée en Python avec FastAPI. Le fichier `main.py` contient les endpoints de l'API, et les dépendances sont répertoriées dans le fichier `requirements.txt`.

## Fonctionnalités

L'application de réservation de bar offre les fonctionnalités suivantes :

- Authentification : Les utilisateurs peuvent se connecter avec leur nom d'utilisateur et leur mot de passe pour accéder à l'application.

- Liste des Cocktails : Les utilisateurs peuvent consulter la liste des cocktails disponibles dans le bar. Chaque cocktail est affiché avec son nom et une quantité sélectionnable à l'aide d'un compteur.

- Commande : Les utilisateurs peuvent sélectionner la quantité de chaque cocktail souhaitée et envoyer leur commande au bar.

## Installation et Exécution

Pour exécuter l'application, suivez les étapes ci-dessous :

### Frontend

1. Assurez-vous que vous avez Node.js et npm installés sur votre machine.
2. Naviguez vers le dossier `front` : `cd front`.
3. Installez les dépendances : `yarn`.
4. Démarrez l'application en mode de développement : `yarn serve`.
5. Accédez à l'application dans votre navigateur à l'adresse `http://localhost:8080`

### Backend

1. Assurez-vous que vous avez Python 3.x installé sur votre machine.
2. Naviguez vers le dossier `back` : `cd back`.
3. Démarrez l'API backend : `poetry run uvicorn src.main:app --reload`.
4. L'API sera accessible à l'adresse `http://localhost:8000`
