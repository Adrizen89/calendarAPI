### Documentation de l'API Calendrier
# Introduction
Cette API vous permet d'obtenir une liste formatée des jours d'un mois spécifique d'une année donnée.

# Installation
Pour installer cette API, utilisez la commande pip suivante :

bash
Copy code
`pip install nom_de_lapi`
Assurez-vous d'avoir pip installé et à jour avant de procéder à l'installation.

# Comment utiliser l'API dans votre projet
Après avoir installé l'API via pip, vous pouvez simplement l'importer dans votre projet et commencer à l'utiliser.

# Fonctionnalités
Méthode get_days_of_month_formatted
Cette méthode statique vous permet d'obtenir une liste formatée des jours d'un mois spécifique d'une année donnée.

Signature de la méthode :

python
Copy code
`def get_days_of_month_formatted(year: int, month: int) -> list:
    ...`
Paramètres :

year : L'année pour laquelle vous souhaitez obtenir les jours. (Type : int)
month : Le mois pour lequel vous souhaitez obtenir les jours. (Type : int)
Retour :

La méthode renvoie une liste de chaînes de caractères formatées représentant chaque jour du mois spécifié.

# Exemple d'utilisation :

python
Copy code
`days = Calendrier.get_days_of_month_formatted(2023, 10)`
`print(days)`
Cet exemple renverra une liste des jours de octobre 2023 formatée.
