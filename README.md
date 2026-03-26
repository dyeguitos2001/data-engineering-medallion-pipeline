# Data Engineering Pipeline Project

Projeto de engenharia de dados desenvolvido para demonstrar a construção de pipelines completos, desde a ingestão até a disponibilização de dados para consumo analítico.

O projeto simula um fluxo de dados de pedidos, aplicando transformações, validações e organização em múltiplas camadas, seguindo boas práticas utilizadas em ambientes modernos de dados.

---

## 📌 Principais conceitos aplicados

- Ingestão e processamento de dados
- Transformação e padronização com Python
- Organização em camadas (Bronze, Silver e Gold)
- Validação de qualidade de dados
- Estruturação para consumo analítico
- Logging e organização modular do código
- Versionamento com Git

---

## 🏗️ Arquitetura

O pipeline segue o padrão de camadas:

- Raw: dados brutos de entrada  
- Bronze: dados ingeridos sem alterações estruturais  
- Silver: dados tratados, limpos e padronizados  
- Gold: dados agregados e prontos para análise  

---

## 📂 Estrutura do projeto
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
---

## ⚙️ Tecnologias utilizadas

- Python
- Pandas
- SQL (SQLite)
- Pytest
- Git

---

## ▶️ Como executar

python -m venv .venv  
.venv\Scripts\activate  
pip install -r requirements.txt  
python -m src.pipeline  

---

## 📊 Saída do pipeline

O pipeline gera datasets em diferentes estágios:

- bronze: dados brutos com controle de ingestão  
- silver: dados tratados e enriquecidos  
- gold: dados agregados para análise  

---

## 🧪 Testes

pytest

---

## 🔍 Observações

Este projeto foi estruturado com foco em clareza, organização e boas práticas, podendo ser facilmente evoluído para cenários mais complexos, como:

- integração com APIs  
- processamento distribuído  
- orquestração de pipelines  
- uso de data lakes  
- integração com ferramentas de BI  

---

## 👤 Autor

Dyego Simões Cabral Metelo
