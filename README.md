# nosql-courses

# Projet NoSQL et ELK Stack avec Docker

Ce projet illustre l'utilisation des bases de données NoSQL, en particulier Elasticsearch, en combinaison avec la stack ELK (Elasticsearch, Logstash, Kibana) dans un environnement conteneurisé Docker. Il s'inspire des concepts et exemples présentés dans les ressources suivantes :

*   [Introduction ELK Stack](lien vers le document 1, si disponible)
*   [What are NoSQL databases?](lien vers le document 2, si disponible)

## Contexte

Ce projet a pour but de démontrer comment les bases de données NoSQL, et Elasticsearch en particulier, peuvent être utilisées pour des cas d'usage spécifiques tels que l'analyse de logs, la recherche full-text et le monitoring en temps réel. Le projet met en avant les avantages de la stack ELK pour l'ingestion, le traitement, le stockage et la visualisation de données non structurées.

## Technologies

*   **Docker et Docker Compose:** Pour la conteneurisation et l'orchestration des services.
*   **Elasticsearch:** Moteur de recherche et d'analyse NoSQL basé sur Lucene.
*   **Logstash:** Outil d'ingestion et de transformation des données.
*   **Kibana:** Interface de visualisation et d'exploration des données.
*   **(Optionnel) Autres bases NoSQL:**  Si le projet le nécessite, d'autres bases NoSQL comme MongoDB, Redis ou Neo4j peuvent être incluses pour comparer et illustrer différents modèles de données.

## Concepts Clés Illustrés

*   **Bases de données NoSQL:**
    *   Types de bases NoSQL : Document-based, Key-Value, Column-Family, Graph-Based (avec exemples de MongoDB, Redis, Cassandra, Neo4j).
    *   Avantages des bases NoSQL : Flexibilité du schéma, scalabilité horizontale, haute disponibilité, performance.
    *   Cas d'usage typiques : Analyse en temps réel, traitement de transactions à haut volume, diffusion de contenu rapide.
*   **Elasticsearch:**
    *   Basé sur Apache Lucene : Indexation inversée pour une recherche full-text rapide.
    *   Architecture distribuée : Shards et replicas pour la scalabilité et la haute disponibilité.
    *   Flexibilité : Capacité à gérer des données non structurées (JSON, CSV, XML).
    *   Cas d'usage : Analyse de logs, monitoring, recherche web.
*   **Stack ELK:**
    *   Ingestion des données avec Logstash.
    *   Stockage et indexation des données dans Elasticsearch.
    *   Visualisation et exploration des données avec Kibana.


## Prérequis

*   Docker et Docker Compose installés sur votre système.

## Installation et Démarrage

1.  Clonez ce dépôt GitHub.
2.  Placez vos exemples de données (logs, JSON, CSV) dans le répertoire `data/`.
3.  Modifiez les fichiers de configuration Logstash (`logstash/logstash.conf`) pour correspondre à la structure de vos données. C'est l'étape la plus importante !
4.  Démarrez les services avec Docker Compose:

    ```
    docker-compose up -d
    ```

5.  Accédez à Kibana dans votre navigateur à l'adresse `http://localhost:5601`. Configurez un index pattern correspondant aux données indexées par Logstash.

## Configuration

*   **Elasticsearch:**  Ajustez les paramètres dans `elasticsearch/elasticsearch.yml` si nécessaire (mémoire, cluster name, etc.).
*   **Logstash:** Configurez les inputs, filters et outputs dans `logstash/logstash.conf` pour traiter vos données correctement. La documentation de Logstash est essentielle pour cette étape.
*   **Kibana:**  Créez des visualisations et des tableaux de bord dans Kibana pour explorer et analyser vos données.

## Utilisation

1.  Une fois les services démarrés, Logstash collectera, transformera et indexera les données dans Elasticsearch.
2.  Utilisez Kibana pour visualiser et explorer les données.  Créez des index patterns, des visualisations et des tableaux de bord pour analyser vos logs.

## Concepts Avancés (Potentiel)

*   **Intégration de Beats:** Utilisation de Filebeat ou Metricbeat pour collecter des données directement depuis des serveurs ou applications.
*   **Sécurité avec X-Pack (Elastic Cloud):** Configuration de l'authentification, l'autorisation et le chiffrement.
*   **Monitoring des performances du cluster ELK:** Utilisation des métriques Elasticsearch et Logstash pour optimiser les performances.

## Troubleshooting

*   **Vérifiez les logs Docker:** Utilisez `docker-compose logs` pour consulter les logs de chaque service et identifier d'éventuelles erreurs.
*   **Erreurs de configuration Logstash:** Logstash peut générer des erreurs si les fichiers de configuration sont incorrects.  Consultez les logs Logstash pour identifier et corriger ces erreurs.
*   **Problèmes de connexion:** Assurez-vous que les services ELK peuvent communiquer entre eux.


