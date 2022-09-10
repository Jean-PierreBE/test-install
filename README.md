# Projet 2 OpenClassRoom : Scrapping d'un site web en Python
## Pour commencer
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

## Pré-requis 
le projet comporte 4 fichiers

