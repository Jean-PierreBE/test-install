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

## Lancement du programme
On peut lancer le programme en tapant sur la ligne de commande de 2 manières :
- python Projet2OC.py "History" : on ne veut que les livres de la catégorie History
- python Projet2OC.py "all" : on veut les livres de toutes les catégories

Si on ne met aucun paramètre ou on met une catégorie érronée , un messge d'erreur sera retourné
De même si le site web à analyser est erroné ou l'une ou l'autre des répertoires de stockage n'existe pas

## Déroulement du programme
Que l'on sélectionne toutes les catégories ou une , le fonctionnement est similaire.
Pour chaque catégorie :
- on parse l'url de chaque livre
- on stocke les informations demandées dans un tableau
- on stocke l'image dans un sous-répertoire catégorie du répertoire images
- une fois tous les livres parsés , on stocke les informations dans un fichier csv

des informations concernant :
- la date et heure de début du programme
- heure de début de chargement de la catégorie
- heure de fin de chargement de la catégorie avec le nombre de livres traités et d'images chargées 
- date et heure de fin du programme
- erreurs éventuelles rencontrées lors de l'exécution du programme
seront stockées dans le fichier LogWebScrapping.log


