# 🎬 Quiz Cinéma (Django)

Un quiz interactif sur le cinéma développé avec **Django**.
Teste tes connaissances avec 20 questions aléatoires et découvre ton score avec une correction détaillée à la fin.

---

## 🚀 Fonctionnalités

* 🎲 20 questions aléatoires à chaque partie
* ❓ Affichage des questions une par une
* 🧠 Calcul automatique du score
* ✅ Correction complète à la fin du quiz
* 🎨 Interface moderne et simple
* 🔄 Possibilité de rejouer

---

## 📦 Installation complète (Mode d’emploi)

Suivez toutes les étapes ci-dessous pour lancer le projet en local.

---

### 🔹 1. Cloner le projet

```bash
git clone https://github.com/ton-username/quiz_cinema.git
cd quiz_cinema
```

---

### 🔹 2. Créer un environnement virtuel

```bash
python -m venv venv
```

---

### 🔹 3. Activer l’environnement virtuel

#### Sur Windows :

```bash
venv\Scripts\activate
```

#### Sur Mac / Linux :

```bash
source venv/bin/activate
```

---

### 🔹 4. Installer les dépendances

```bash
pip install django
```

---

### 🔹 5. Appliquer les migrations (base de données)

```bash
python manage.py migrate
```

---

### 🔹 6. Ajouter les questions du quiz

```bash
python quiz/seed.py
```

👉 Cette commande va :

* créer une base de données
* ajouter environ 200 questions de cinéma

---

### 🔹 7. Lancer le serveur

```bash
python manage.py runserver
```

---

### 🔹 8. Accéder au site

Ouvre ton navigateur et va sur :

```
http://127.0.0.1:8000/
```

---

## 🧠 Utilisation du quiz

1. Clique sur **"Commencer le quiz"**
2. Réponds aux 20 questions
3. À la fin :

   * tu obtiens ton score
   * tu vois la correction complète
4. Clique sur **"Rejouer"** pour recommencer

---

## 🛠️ Technologies utilisées

* Python 🐍
* Django 🌐
* HTML / CSS 🎨

---

## 📁 Structure du projet

```
quiz/
│
├── models.py
├── views.py
├── urls.py
├── seed.py
│
templates/
└── quiz/
    ├── home.html
    ├── question.html
    └── result.html
```

---

## 📌 Auteur

Projet réalisé par **Ayoub**

---

## ⭐ Améliorations possibles

* 🏆 Système de classement (leaderboard)
* 👤 Authentification utilisateur
* 🎬 Intégration API films
* ⏱️ Ajout d’un timer

---

## 💡 Remarque

Si tu rencontres un problème :

* vérifie que Django est bien installé
* vérifie que l’environnement virtuel est activé
* relance les migrations

---

## 🚀 Lancer rapidement (résumé)

```bash
git clone https://github.com/ton-username/quiz_cinema.git
cd quiz_cinema
python -m venv venv
venv\Scripts\activate   # ou source venv/bin/activate
pip install django
python manage.py migrate
python quiz/seed.py
python manage.py runserver
```

---

🎉 Bon quiz !
