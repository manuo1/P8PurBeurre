##
# **Projet 8 OpenClassrooms :**

##
# **Créez une plateforme pour amateurs de Nutella**

## DESCRIPTION

Le projet consistait à développer une application web pour la société Pur Beurre.

Le site permet à quiconque de trouver un substitut sain à un aliment considéré comme &quot;Trop gras, trop sucré, trop salé&quot;.

Il devait être développé avec le framework django et respecter le cahier des charges fournis.

## INSTALATION

Le programme a été développé en langage python dans un environnement virtuel utilise les données alimentaires du site [Open Food Facts](https://fr.openfoodfacts.org/).

Pour le faire fonctionner vous devez :

1. **Installer** Python et PostgreSQL
2. **Créer** un dossier et cloner le repo

«  git clone [https://github.com/manuo1/P8PurBeurre.git](https://github.com/manuo1/P8PurBeurre.git) »

1. **Créer** avecPostgreSQL une base dedonnées et un utilisateur et modifiez les paramètres du projet dans le fichier « purbeurre\purbeurre\settings.py » puis dans « DATABASES »
2. **Créer et activer** un environnement virtuel
3. **Installer** les paquets requis avec : « python -m pip install -r requirements.txt »
4. **Créer** les tables de la base de données avec « python manage.py migrate »
5. **Ajouter** des données alimentaires depuis le site Open Food Facts avec : « python manage.py populatedb 2000 » le chiffre 2000 correspond au nombre d&#39;aliments insérés
6. **Collecter** les fichiers statics avec « python manage.py collectstatic »

## **DEMARRER LE SERVEUR**

« python manage.py runserver »

## **FONCTIONNEMENT**

Inscrivez le nom d&#39;un aliment dans la zone de recherche

## **VERSION EN LIGNE**

[**purbeurre-mo1 sur Heroku**](https://purbeurre-mo1.herokuapp.com/)
