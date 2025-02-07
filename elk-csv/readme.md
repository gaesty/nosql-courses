# Projet ELK pour Traitement de Logs CSV et Web Server

Ce projet utilise la stack ELK (Elasticsearch, Logstash, Kibana) pour collecter, traiter et analyser des logs CSV et des logs de serveur web.

## Structure du Projet

```
.
├── data
├── docker-compose.yml
├── elasticsearch
│   └── elasticsearch.yml
├── logstash
│   ├── logstash.conf
│   ├── logstash-json.conf
│   └── logstash.yml
└── web_server_logs
    └── logstash-apache.conf
```

## Description des Composants

### Data
Répertoire destiné à stocker les fichiers de données d'entrée.

### Elasticsearch
Configuration d'Elasticsearch :
- `elasticsearch.yml` : Fichier de configuration pour Elasticsearch

### Logstash
Configuration de Logstash pour le traitement des logs :
- `logstash.conf` : Configuration principale de Logstash
- `logstash-json.conf` : Configuration pour le traitement des logs au format JSON
- `logstash.yml` : Configuration générale de Logstash

### Web Server Logs
Configuration spécifique pour les logs de serveur web :
- `logstash-apache.conf` : Configuration Logstash pour les logs Apache

### Autres Fichiers
- `docker-compose.yml` : Configuration Docker Compose pour orchestrer les services ELK

## Démarrage Rapide

1. Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.
2. Clonez ce dépôt.
3. Placez vos fichiers de logs dans le répertoire `data/`.
4. Lancez les services avec la commande :
   ```
   docker-compose up -d
   ```
5. Accédez à Kibana via votre navigateur (généralement sur `http://localhost:5601`).

## Configuration

- Pour modifier la configuration d'Elasticsearch, éditez le fichier `elasticsearch/elasticsearch.yml`.
- Pour ajuster le traitement des logs, modifiez les fichiers de configuration Logstash dans le répertoire `logstash/`.
- Pour configurer le traitement des logs de serveur web, éditez `web_server_logs/logstash-apache.conf`.

## Utilisation

1. Assurez-vous que vos fichiers de logs sont placés dans le répertoire `data/`.
2. Logstash traitera automatiquement les logs selon les configurations définies.
3. Utilisez Kibana pour visualiser et analyser les données traitées.

## Dépannage

Si vous rencontrez des problèmes :
1. Vérifiez les logs Docker avec `docker-compose logs`.
2. Assurez-vous que tous les services sont en cours d'exécution avec `docker-compose ps`.
3. Vérifiez que les fichiers de configuration sont correctement formatés.
