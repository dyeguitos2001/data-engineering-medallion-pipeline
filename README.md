# Projeto de Engenharia de Dados Júnior

Projeto de portfólio construído para demonstrar fundamentos de Engenharia de Dados alinhados a vagas de nível júnior, com foco em ingestão, transformação, qualidade e disponibilização de dados em arquitetura Medallion.

## O que este projeto demonstra
- Python para manipulação de dados
- SQL para consumo analítico
- pipeline em camadas Bronze / Silver / Gold
- validações simples de qualidade
- logging, organização e documentação
- estrutura pronta para GitHub

## Estrutura
```text
data-engineering-junior-project/
├── data/
│   ├── raw/orders.csv
│   ├── bronze/orders_bronze.csv
│   ├── silver/orders_silver.csv
│   └── gold/sales_summary_gold.csv
├── src/
│   ├── utils/logging_config.py
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── quality.py
│   ├── load.py
│   └── pipeline.py
├── tests/test_transform.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.pipeline
```

## Destaque para currículo
**Projeto de Pipeline de Dados com Python, SQL e arquitetura Medallion**
- Desenvolvi pipeline de ingestão, transformação e disponibilização de dados em camadas Bronze, Silver e Gold.
- Implementei tratamento, padronização e validações de qualidade de dados com Python.
- Estruturei saída analítica em CSV e consultas SQL para suporte a dashboards e análises.
- Organizei o projeto com logs, testes e documentação técnica para publicação em GitHub.

## Relação com a vaga
Mesmo rodando localmente com CSV, o projeto replica conceitos compatíveis com vagas de Engenharia de Dados Júnior:
- arquitetura Medallion
- troubleshooting básico
- SQL para analytics
- Python para dados
- documentação de pipeline
- base para Databricks / Spark / Delta
