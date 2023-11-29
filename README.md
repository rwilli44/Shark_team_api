Projet Python création API

## Description

Ce projet de 5 jours, fait dans le cadre de la formation "Concepteur, Développeur d'application" réalisée par Diginamic, a pour but de créer une API permettant de simuler l'achat de livre via un site web.
Ce projet nous a permis de travailler en trinome et mettre en pratique les cours qui nous ont été donnés sur Python, les connexions avec base de données (via SQLAlchemy) à partir de routes qui ont été crées tout en testant notre code.

## Fonctionnalités

- L'application utilise le framework FastAPI pour créer une API.
- Elle se connecte à une base de données MariaDB : la gestion de l'ORM est assurée par la librairie SqlAlchelmy.
- Les tests unitaires sont mis en place avec le module unittest.
- Le serveur d'application est démarré à l'aide de la librairie Uvicorn.

## Architecture du Projet

Le projet suit l'architecture suivante :

```
nom_projet/
    |- README.md
    |- requirements.txt
    |- .gitignore
    |- .env
    |- index.html
    |- assets/
        |- search.js
    |- src/
        |- __init__.py
        |- main.py
        |- config/
            |- __init__.py
            |- connexion.py
        |- models/
            |- __init__.py
            |- ...
        |- router/
            |- __init__.py
            |- ...
        |- schema/
            |- __init__.py
            |- ...
    |- tests/
        |- __init__.py
        |- ...
    |- docs/
        |- librairie.sql
        |- ETUDE_DE_CAS.pdf
        |- ...

```

- Le dossier `src/` contient le code source de l'application, avec ses différents modules.
- Le script SQL pour créer la base de données pour les tests unitaires est placé dans le dossier `tests/`. Les tests unitaires sont dans le dossier `src/` car on n'arrivait pas à le faire reconnaître les modules dans `src/` autrement.
- Les fichiers de documentation se trouvent dans le dossier `docs/`.
- Les configurations serveur se trouvent dans le dossier `config/`.
- Vos identifiants de connexion à la database doivent être rentrés dans le document `.env`.
- Pour tester le front, lancer le front sur un serveur comme Go Live. Si la porte n'est pas 5500, pensez à la changer dans le variable origins dans le fichier main. Lancer également l'API avec uvicorn et vous devriez pouvoir chercher des livres dans la base de données.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir **Python 3.11** installé sur votre système.
3. Créez votre database au nom souhaité avec MariaDB
4. Dans le fichier connexion.py, rentrer le nom de votre database (à la place de librairie)
5. Dans le fichier .env mettez votre username et password utilisés lors de la création de votre database MariaDB
6. Le programme principal utilisant plusieurs librairie, en cas de défaut, utiliser la ligne de commande pip install
7. Installez un outils de lecture de database (DBeaver par exemple) si ce n'est déjà fait

## Utilisation

1. Accédez au répertoire src.
2. Exécutez la commande suivante dans le terminal pour démarrer le serveur d'application :
   ` uvicorn projet.main:app --reload`
   Cela lancera le serveur d'application sur `http://localhost:8000`.
3. Accédez au Swagger de FastAPI en rajoutant à l'url `/docs`
4. Modifiez le Swagger à votre convenance en fonction des commentaires de chaque rubrique à côté des POST/GET/DELETE/PATCH : vous pourrez alors voir, via votre lecteur de database, les tables évoluer avec les données que vous avez rentrées.
5. Pour réaliser des tests unitaires, créer une base de données qui s'appelle test et utiliser le script SQL `create_test_db.sql` pour créer et remplir les tables. Utiliser le script `drop_tables_test_db.sql` si besoin pour supprimer les tables avant de les recréer si les tests sont répétés. Dans le fichier config, changer le nom de base de données à test. Ensuite, depuis le fichier src, lancer le script des tests avec python -m tests_unitaire.

## Contributions

Ce projet a été développé par Rachel Williams, Tarik Sadkhi et Damien Vialla de Soleyrol avec l'aide de notre formateur, Robin Hotton.
