# Projet de Traitement de Logs

Ce projet est conçu pour collecter, traiter et analyser différents types de logs à l'aide de Filebeat, Logstash, et potentiellement Elasticsearch et Kibana (stack ELK).

## Structure du Projet

```
.
├── data
│   ├── apache_logs.txt
│   ├── data.csv
│   └── data-json.log
├── docker-compose.yml
├── filebeat
│   ├── dockerfile
│   └── filebeat.yml
├── logs
│   └── python_logs.log
├── logstash
│   ├── config
│   │   ├── logstash.yml
│   │   └── pipelines.yml
│   └── pipeline
│       ├── logstash-apache.conf
│       ├── logstash-csv.conf
│       └── logstash-python-log.conf
├── README.md
└── send_logs.py
```

## Description des Composants

### Data
Contient les fichiers de logs sources :
- `apache_logs.txt` : Logs Apache
- `data.csv` : Données au format CSV
- `data-json.log` : Logs au format JSON

### Filebeat
Configuration de Filebeat pour la collecte de logs :
- `dockerfile` : Instructions pour construire l'image Docker de Filebeat
- `filebeat.yml` : Configuration de Filebeat

### Logs
Répertoire contenant les logs générés par l'application Python :
- `python_logs.log` : Logs Python

### Logstash
Configuration de Logstash pour le traitement des logs :
- `config/logstash.yml` : Configuration générale de Logstash
- `config/pipelines.yml` : Définition des pipelines Logstash
- `pipeline/` : Configurations spécifiques pour chaque type de log

### Autres Fichiers
- `docker-compose.yml` : Configuration Docker Compose pour orchestrer les services
- `send_logs.py` : Script Python pour générer ou envoyer des logs
- `README.md` : Ce fichier

## Démarrage Rapide

1. Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.
2. Clonez ce dépôt.
3. Lancez les services avec la commande :
   ```
   docker-compose up -d
   ```
4. Les logs seront collectés et traités automatiquement.

## Configuration

Pour modifier la configuration de Filebeat ou Logstash, ajustez les fichiers YAML correspondants dans les répertoires `filebeat/` et `logstash/config/`.

## Génération de Logs

Pour générer des logs de test, exécutez :

```
python send_logs.py
```

## Contribution

Les contributions à ce projet sont les bienvenues. Veuillez ouvrir une issue ou soumettre une pull request pour toute amélioration ou correction.


