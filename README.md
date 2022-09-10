# Projet 2 OpenClassRoom : Scrapping d'un site web en Python
## Présentation du projet
le but de ce projet est d'extraire une liste de livres à partir du site http://books.toscrape.com/ .
Les livres sont regroupées par catégories ex : Travel , History etc ...
Il faut extraire pour chaque livre les renseignements suivants et les mettre dans un fichier csv par catégorie :
- product_page_url : url du livre sur le site
- universal_ product_code (upc) : code UPC
- title : titre du livre
- price_including_tax : prix ttc
- price_excluding_tax : prix hors taxes
- number_available : nombre disponible pour le livre sélectionné
- product_description : résumé du livre
- category : catégorie à laquelle appartient le livre
- review_rating : nombre d'étoiles
- image_url : url de l'image associée au livre

les images de chaque livre seront extraites également et stokées dans un répertoire avec comme nom la catégorie

## composition 
le projet comporte 4 fichiers
- requirements.txt : contient les packages python necessaires au projet à installer
- parameters.txt : fichier json contenant l'URL du site à analyser et les répertoires où installer les csv et les images
- Projet2OC.py : programme à lancer sur la ligne de commande pour exécuter le traitement
- AnalizeWeb.py : package appellé par le programme ci-dessus pour exécuter le traitement

## Installation
- choisissez votre répertoire où exécuter vos programmes python
- créer votre environnement virtuel
- installer les packages python du fichier requirements.txt
- mettre au même niveau du répertoire choisi parameters.txt,Projet2OC.py ,AnalizeWeb.py
- vérifier que les répertoires où stocker les csv et les images existent , sinon les créer (le programme fera un contrôle mais ne les créera pas)

