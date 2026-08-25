# Artisell Loader

Projet de conteneurisation et d'automatisation du chargement de données pour l'écosystème Artisell.

##  Stack Technique
* **Python** (script de chargement)
* **PostgreSQL** (base de données relationnelle)
* **pgAdmin 4** (interface de gestion)
* **Docker & Docker Compose** (contenurisation et orchestration)

---

##  Structure et Contenu des Scripts

* **`docker-compose.yml`** : Fichier d'orchestration principal. Il configure et lie trois services :
  * `postgres` : Instance de base de données PostgreSQL isolée sur un réseau interne (`artisell-net`), avec un volume persistant pour les données.
  * `pgadmin` : Interface web d'administration connectée à PostgreSQL, accessible sur l'hôte.
  * `loader` : Conteneur éphémère basé sur le script Python, chargé d'exécuter l'insertion/le chargement des données au démarrage.
* **`Dockerfile`** : Fichiers d'instructions pour construire l'image personnalisée du conteneur Python, incluant l'installation des dépendances (`requirements.txt`).
* **`loader.py`** : Script Python principal. Il gère la connexion à la base de données, la lecture/transformation des sources de données et l'insertion en base.
* **`requirements.txt`** : Liste les bibliothèques Python tierces nécessaires au fonctionnement du script (ex: `psycopg2`, `pandas`, etc.).
* **`.env`** : Fichier de configuration contenant les secrets et paramètres propres à notre environnement local (exclu de Git).

---

##  Variables d'Environnement

Le projet nécessite un fichier `.env` à la racine pour fonctionner. Voici les variables à y renseigner :

| Variable | Description | Exemple |
| :--- | :--- | :--- |
| `POSTGRES_USER` | Nom d'utilisateur administrateur de la base de données | `admin` |
| `POSTGRES_PASSWORD` | Mot de passe sécurisé pour l'accès à PostgreSQL | `mon_mot_de_passe` |
| `POSTGRES_DB` | Nom de la base de données par défaut créée au lancement | `quelque chose` |
| `PGADMIN_DEFAULT_EMAIL` | Email de connexion pour l'interface pgAdmin | `quelquechose@admin` |
| `PGADMIN_DEFAULT_PASSWORD` | Mot de passe de connexion pour pgAdmin | `autre_mot_de_passe` |

---

##  Lancement du Projet

### 1. Configuration
Crée ton fichier `.env` à la racine du projet en t'appuyant sur le tableau des variables ci-dessus.

### 2. Démarrage de la stack
Lance les conteneurs en arrière-plan :
```bash
docker compose up -d --build
```
### 3. Gestion et Suivi

Voir les logs de tous les conteneurs :
```bash
docker compose logs -f
```

Voir les logs uniquement du Loader :
```bash
docker compose logs loader
```
### Accès aux services
PostgreSQL : Port 5434 (externe) / 5432 (interne Docker)

pgAdmin : http://localhost:5080


































