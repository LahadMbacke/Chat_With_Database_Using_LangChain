# Chat_With_Database_Using_LangChain
![chat-with-mysql-chain-langchain](https://github.com/user-attachments/assets/e2cbc37b-d9ee-46ed-a9c4-153125e094f1)

https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/

# README du Projet

## Aperçu

Ce projet intègre divers composants pour traiter des requêtes en langage naturel concernant le contenu d'une base de données, les traduire en requêtes SQL, exécuter ces requêtes, puis traduire les résultats en langage naturel. Il utilise l'API OpenAI pour le traitement et la compréhension du langage naturel, ainsi qu'une base de données PostgreSQL pour le stockage et la récupération des données.

## Fonctionnalités

- **Traitement du Langage Naturel** : Utilise l'API OpenAI pour interpréter les requêtes en langage naturel et générer des requêtes SQL.
- **Interaction avec la Base de Données** : Se connecte à une base de données PostgreSQL pour récupérer les informations des tables et exécuter les requêtes SQL.
- **Génération Dynamique de Réponses** : Traduit les résultats des requêtes SQL en langage naturel pour une interprétation facile par l'utilisateur.

## Prérequis

- Python 3.x
- PostgreSQL
- Clé API OpenAI
- Packages Python : `dotenv`, `psycopg2`, `langchain_openai`, `langchain`, `langchain_community`, `langchain_core`

## Variables d'Environnement

Créez un fichier .env dans le répertoire racine du projet et ajoutez les variables suivantes :
- OPENAI_API_KEY= `<votre_clé_api_openai>`
- host= `<hôte_de_la_base_de_données>`
- port= `<port_de_la_base_de_données>`
- dbname= `<nom_de_la_base_de_données>`
- username= `<nom_d'utilisateur_de_la_base_de_données>`
- password= `<mot_de_passe_de_la_base_de_données>`

## Architecture
Le projet est structuré autour d'une série d'étapes qui :

- Récupération de la Requête SQL : Convertit une question en langage naturel en une requête SQL à l'aide de l'API OpenAI.
- Exécution de la Requête : Exécute la requête SQL sur la base de données PostgreSQL et récupère les résultats.
- Traduction des Résultats : Convertit les résultats de la requête SQL en langage naturel pour présentation à l'utilisateur.

## Contribution
Les contributions sont les bienvenues ! Veuillez forker le dépôt et soumettre une pull request avec vos modifications proposées.
## Next Step 
utiliser Streamlit pour avoir un interface graphique pour chater sur la base de donnees