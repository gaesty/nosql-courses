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