# DOCUMENTATION API CALENDRIER

## Introduction

Cette API vous permet d'obtenir une liste formatée des jours d'un mois spécifique d'une année donnée.

### Pré-requis

Assurez-vous d'avoir pip d'installé et à jour avant de procéder à l'installation.

### Installation

Pour installer cette API, utilisez la commande pip suivante :  
``pip install chemin/acces/mon_calendrier-0.1.tar.gz``

## Comment utiliser l'API dans votre projet

Après avoir installé l'API via pip, vous pouvez simplement l'importer dans votre projet et commencer à l'utiliser.  
``from calendrier.calendrier import Calendrier``

## Fonctionnalité
### Fonction get_days_of_month_formatted
Cette méthode statique vous permet d'obtenir une liste formatée des jours d'un mois spécifique d'une année donnée.  
``def get_days_of_month_formatted(year: int, month: int) -> list:  
  ...``
### Paramètres
year : L'année pour laquelle vous souhaitez obtenir les jours. (Type : int)  
month : Le mois pour lequel vous souhaitez obtenir les jours. (Type : int)

### Retour
La fonction renvoie une liste de chaînes de caractères formatées représentant chaque jour du mois spécifié.

### Exemple d'utilisation
``days = Calendrier.get_days_of_month_formatted(2023, 10)  
  print(days)``
Cette exemple renverra une liste des jours de octobre 2023 dans ce format :  
``Sunday 01 October 2023  
  ...``

## Versions
**Version :** 1.0

## Auteur
* **Adrien Berard**

