# blog_api
# blog_api
# Django API Project

## Introduction

Bienvenue dans notre projet Django API, développé avec Django Rest Framework. Ce guide vous expliquera comment installer, configurer et utiliser l'API pour gérer une liste d'utilisateurs et leurs articles de blog.

## Prérequis

- Python 3.x
- Docker
- Docker Compose
- Git

## Installation

### 1. Cloner le dépôt

Clonez le dépôt sur votre machine locale :

```bash
git clone https://github.com/Maeva109/blog_api.git
cd blog_api
```
### 2. Créer et activer un environnement virtuel (optionnel)
Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet :

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```
### 3. Installer les dépendances
Installez les dépendances nécessaires en utilisant le fichier requirements.txt :

```bash
pip install -r requirements.txt
```
### 4. Documentation des EndPoint de L'API
#### Users
##### Créer un utilisateur
POST /api/users
Request Body:
```bash
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```
Reponse :
```bash
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```
##### Obtenir tous les utilisateurs
GET /api/users

Response:
```bash
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
]
```

##### Obtenir un utilisateur par ID
GET /api/users/{id}

Response:

```bash
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```
##### Mettre à jour un utilisateur
PUT /api/users/{id}

Request Body:
```bash

{
  "name": "Johnny Doe",
  "email": "johnny.doe@example.com"
}
```
##### Supprimer un utilisateur
DELETE /api/users/{id}

Response:

```bash
{
  "message": "User deleted successfully"
}
```

#### Posts
##### Créer un post
POST /api/posts

Request Body:

```bash 
{
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "author": 1
}
```
##### Obtenir tous les posts
GET /api/posts

Response:
```bash
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "author": 1
  },
  {
    "id": 2,
    "title": "Another Post",
    "content": "This is another post.",
    "author": 2
  }
]
```

##### Obtenir un post par ID
GET /api/posts/{id}

Response:
```bash 
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "author": 1
}
```

##### Mettre à jour un posts
PUT /api/posts/{id}

Request Body:
```bash

{
  "name": "Johnny Doe",
  "email": "johnny.doe@example.com"
}
```
##### Supprimer un posts
DELETE /api/posts/{id}

Response:

```bash
{
  "message": "posts deleted successfully"
}
```

