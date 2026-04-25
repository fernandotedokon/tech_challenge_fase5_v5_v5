# 📈 Projeto LSTM para Treinamento e Fraud Detection
**Powered by Group 9, 6MLET**

### Projeto de Machine Learning e MLOps para previsão de **Fraud Detection** usando **redes neurais LSTM**, incluindo Orquestração, implantação de API, monitoramento, detecção de desvio de dados, automação de retreinamento, visualização em painel e infraestrutura Dockerizada.



## 🚀 Visão Geral

O objetivo deste projeto é prever o **detecção de fraude** das operaçãoes dos clientes das empresas financeiras, utilizando dados históricos, treinamento, avaliação de score de risco dos dados obtidos automaticamente via dataset com simulador de risco.

Utilizando **Redes Neurais LSTM (Long Short-Term Memory)**, adequadas para séries temporais financeiras.
O projeto atende **toda a pipeline de Machine Learning**:

1. Coleta de dados históricos
2. Pré-processamento e feature engineering
3. Treinamento e avaliação do modelo
4. Salvamento e versionamento
5. Deploy via API REST
6. Monitoramento de performance
7. Detecção de Data Drift
8. Retraining automático
9. Visualização via Dashboard
10. Dockerização completa



## 📦 Requisitos

- Python 3.11+
- pip
- Docker
- WSL



## 🧠 Tecnologias Utilizadas

- **Pandas** - Biblioteca para análise e manipulação de dados estruturados (como planilhas, CSV, tabelas, Parquet).
- **TensorFlow** - Biblioteca open source criada pelo Google para Machine Learning e Deep Learning, serve para criar, treinar, avaliar e colocar modelos de ML em produção.
- **Keras** - Biblioteca de alto nível para Deep Learning, focada em simplicidade e produtividade, serve para criar, treinar e testar redes neurais de forma rápida.
- **NumPy** - Biblioteca base para computação numérica em python, operações matemáticas de alta performance.
- **Scikit-learn** - Biblioteca Python para Machine Learning “clássico”, focada em modelos estatísticos, simplicidade e produtividade, usada para treinar, avaliar e aplicar modelos de ML sem Deep Learning.
- **FastAPI** - Biblioteca Python para criar APIs REST modernas, com foco em performance, simplicidade e tipagem forte, usado para modelos de Machine Learning, microserviços e backends rápidos.
- **Streamlit** - Biblioteca Python para criar aplicações web interativas de forma rápida e simples, focado em visualização de dados e projetos de Data Science / ML.
- **matplotlib** - Biblioteca Python para criação de gráficos e visualizações de dados, transforma números e tabelas em gráficos visuais: linhas, barras, dispersão e histogramas.


### 🔹 Core
- **pandas, numpy** → base de dados e feature engineering

### 🔹 ML
- **scikit-learn** → modelos baseline + produção
- **torch** → MLP (mesmo que opcional, já deixei pronto)

### 🔹 MLflow
- tracking de experimento
- versionamento de modelo
- registry (Champion vs Challenger)

### 🔹 API
- **fastapi** → endpoint realtime
- **uvicorn** → servidor

### 🔹 Airflow
- orquestra pipeline (treino + retrain)

### 🔹 DVC
versionamento de dados (essencial pra datathon)

### 🔹 Monitoramento
- **evidently** → drift
- **prometheus-client** → métricas

### 🔹 LLM / RAG
- **langchain** → agente ReAct + RAG
- **openai** → modelo LLM
- **faiss-cpu** → vector DB
- **tiktoken** → tokenização

### 🔹 Segurança
 presidio → detecção de PII (LGPD compliance)

### 🔹 Testes
- **pytest**

### 🔹 Qualidade
- **ruff** → lint
- **pre-commit** → hooks





## 🧠 🔥 Arquitetura completa de Fraud Detection (nível produção) - 
🏗️ Visão geral

```bash
                ┌──────────────────────┐
                │  Airflow (orquestra) │
                └─────────┬────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
📊 Ingestão        🤖 Treinamento     🔁 Re-training
(pipelines)        (ML pipeline)      (schedule diário)
        │                 │
        ▼                 ▼
   Data Lake        MLflow Tracking
 (MinIO / S3)       (experimentos)
        │                 │
        └──────┬──────────┘
               ▼
        📦 Modelo versionado
               │
               ▼
        🚀 API de Previsão
           (FastAPI)
               │
               ▼
   📡 Monitoramento & Observabilidade
     ┌──────────────┬──────────────┐
     ▼              ▼              ▼
 Prometheus      Grafana       Alertmanager
(metrics)     (dashboards)     (alertas)


```
## 🧱 Arquitetura do Projeto

```bash
fraud-detection-platform/
│
├── docker/
│   ├── airflow/
│   ├── api/
│   ├── ml/
│
├── dags/
│   ├── ingestion_dag.py
│   ├── training_dag.py
│   ├── retrain_dag.py
│
├── src/
│   ├── ingestion/
│   │   ├── fetch_api.py
│   │   ├── load_data.py
│   │
│   ├── features/
│   │   ├── build_features.py
│   │
│   ├── models/
│   │   ├── train.py
│   │   ├── predict.py
│   │
│   ├── api/
│   │   ├── main.py
│   │   ├── schemas.py
│   │   ├── service.py
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── mlruns/  # MLflow
├── configure.env
├── docker-compose.yml
├── docker-compose-airflow.yml
├── docker-compose-api.yml
└── requirements-ml.txt

```


## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <https://github.com/fernandotedokon/tech_challenge_fase5_v5_v5.git>

cd tech_challenge_fase5_v5_v5
```



## 🐳 Como Executar o Projeto via docker

1. Dockerfile único (único para API e Streamlit)
2. docker-compose.yml 
3. Estrutura de pastas recomendada
4. Como subir tudo com um comando

#### 📦 Requisitos

- Ter Docker instalado e inicializado
- Docker estar integrado WSL

▶️ Como subir tudo, estando  na raiz do projeto:
```bash
docker-compose build
docker-compose up
```

Ou em modo background:
```bash
docker-compose up -d
```

🌐 Acessos depois de subir
| Serviço   | URL                                                      |
| --------- | -------------------------------------------------------- |
| FastAPI   | [http://localhost:8000/docs](http://localhost:8000/docs) |
| Streamlit | [http://localhost:8501](http://localhost:8501)           |



## ✅ Como testar e validar cada etapa do projeto

### ⚙️ 1. Orquestração — Airflow

Apache Airflow

Responsável por:
  - gerar dataset
  - treinar modelo
  - validar modelo
  - publicar versão

🔁 DAG ideal:
```bash
generate_data
    ↓
train_model
    ↓
evaluate_model
    ↓
register_model (MLflow)
    ↓
deploy_model
```


### 🤖 2. MLflow (coração do ML)

MLflow

📌 Tracking:
- accuracy
- precision
- recall
- AUC

📌 Registry:
- versiona modelos
- staging / production

📌 Experiments:
- compara runs

💡 Fluxo real:
```bash
Train → Log metrics → Register model → Promote to production
```




### 🚀 3. API de Fraude (serving)

FastAPI

Função:
Recebe transação e retorna risco de fraude

Exemplo
```bash
POST /predict
```

Request:
```bash
{
  "amount": 2500,
  "user_id": 123,
  "device_id": "dev_10",
  "lat": -23.5,
  "lon": -46.6
}
```

Response:
```bash
{
  "fraud_probability": 0.87,
  "is_fraud": 1
}
```



🔗 API carrega modelo do MLflow
```bash
model = mlflow.pyfunc.load_model("models:/fraud-model/Production")
```



### 📊 4. Monitoramento (Grafana + Prometheus)

Grafana
Prometheus

📈 O que monitorar:
API:
  - requests/sec
  - latency
  - error rate
ML:
  - drift de dados
  - drift de features
  - queda de performance


📊 Dashboard Grafana:
  - fraude por hora
  - taxa de fraude
  - latência da API
  - uso do modelo




### 🚨 5. Alertas (Alertmanager)

Alertmanager

Exemplos:
🔴 alerta crítico:
  - fraude subiu 300%

🟡 alerta médio:
  - latência > 500ms

🔴 alerta ML:
  - AUC caiu abaixo de 0.75





### 🔄 Fluxo completo (visão real de empresa)

```bash
1. Airflow gera dados
2. Salva no MinIO
3. Treina modelo
4. MLflow registra experimento
5. Se aprovado → promove modelo
6. API atualiza modelo automaticamente
7. Prometheus monitora API
8. Grafana mostra dashboards
9. Alertmanager dispara alertas
```





# Fraud Detection System

## Features
- ML Pipeline (MLflow)
- Realtime API
- Airflow orchestration
- RAG + Agent
- Drift detection
- LGPD ready

## Run

make train
make serve


# ==============================
# README.md
# ==============================
# Fraud Detection Platform

## Run

docker-compose up --build

## Endpoints

POST /predict

## Airflow

http://localhost:8080

## MLflow

http://localhost:5000

# ==============================
# END PROJECT
# ==============================



## 🧭 VISÃO GERAL (o que você vai fazer)

1. Criar estrutura de pastas
2. Colar os arquivos (Dockerfiles + código)
3. Subir serviços básicos
5. 4. Inicializar Airflow
6. Testar API
7. Ativar monitoramento (Prometheus + Grafana)



### 📁 1. Criar estrutura do projeto
No seu computador:

```bash
mkdir fraud-detection-platform
cd fraud-detection-platform
```
Agora crie as pastas:

```bash
mkdir -p docker/api docker/airflow src/api src/models src/features src/ingestion src/monitoring dags monitoring data/raw data/processed
```


### 🐳 3. Subir só infraestrutura primeiro (TESTE POR ETAPAS)
Antes de tudo, teste só banco + airflow:

```bash
docker-compose up postgres
```


### ⚙️ 4. Inicializar Airflow (ESSENCIAL)

```bash
docker-compose run airflow-webserver airflow db init
```

Criar usuario:

```bash
docker-compose run airflow-webserver airflow users create \
  --username admin \
  --password admin \
  --firstname admin \
  --lastname admin \
  --role Admin \
  --email admin@email.com

```



Gere a chave (dentro do container 👇)

```bash
docker compose run --rm airflow-webserver python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Subir todos os containers
```bash
docker compose up --build
```



### 🚀 5. Subir Airflow completo

```bash
docker-compose up airflow-webserver airflow-scheduler
```

👉 Acesse:

http://localhost:8080

✔ Verifique:

DAGs aparecem
scheduler ativo





🚀 Agora sobe tudo
```bash
docker compose up
```

🌐 Acessa no navegador

```bash
http://localhost:8080
```

```bash
user: admin
pass: admin
```



### 🤖 6. Subir API

```bash
docker-compose up api
```

👉 Testar:

http://localhost:8000/docs

✔ Se funcionar → API OK



### 🚀 PASSO A PASSO PRA LIMPAR TUDO

```bash
docker-compose down -v --remove-orphans
docker system prune -f
```

depois

```bash
docker-compose up --build api
```

### TRANSACAO NORMAL

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
  "amount": 50,
  "user_id": 1,
  "device_id": "abc",
  "lat": -23.5,
  "lon": -46.6,
  "merchant_lat": -23.5,
  "merchant_lon": -46.6
}'
```



### Simulação de FRAUDE

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
  "amount": 1000,
  "user_id": 1,
  "device_id": "abc",
  "lat": -23.5,
  "lon": -46.6,
  "merchant_lat": 40.7,
  "merchant_lon": -74.0
}'
```


## Forcar dados externos

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
  "amount": 100000,
  "user_id": 9999,
  "device_id": "unknown_device_999",
  "lat": -23.5,
  "lon": -46.6,
  "merchant_lat": 40.7,
  "merchant_lon": -74.0
}'

```


### COMO SUBIR (PASSO A PASSO)

```bash
docker-compose down --remove-orphans

docker-compose build --no-cache

docker-compose up
```

### 2. LIMPAR CACHE DE BUILD

```bash
docker builder prune -a
```


### 2. LIMPAR TUDO RELACIONADO

```bash
docker rm -f $(docker ps -aq)
```



## 🚀 COMO SUBIR (FORMA CORRETA)
### 1. Limpeza total

```bash
docker rm -f $(docker ps -aq)
docker volume prune -f
```

### 2. Subir ambiente

```bash
docker compose down -v

docker-compose build api

docker compose up --build

docker-compose up -d --build

```



### Sempre que mudar versão do Airflow:

```bash
docker compose down -v

docker compose up --build

```




### 🚀 ACESSOS

| Serviço    | URL                                                            |
| ---------- | -------------------------------------------------------------- |
| Airflow    | [http://localhost:8080](http://localhost:8080)                 | ok
| API        | [http://localhost:8000](http://localhost:8000)                 | ok
| Metrics    | [http://localhost:8000/metrics](http://localhost:8000/metrics) | ok
| Prometheus | [http://localhost:9090](http://localhost:9090)                 | ok
| Grafana    | [http://localhost:3000](http://localhost:3000)                 | ok
| MLflow     | [http://localhost:5000](http://localhost:5000)                 | ok




## 3. Grafana

```bash
http://localhost:3000

login: admin / admin
```

### Criar dashboard

1. Clique em "+" → Dashboard
2. Add new panel
3. Em Data source → selecione Prometheus



### Painel 1: fraude por minuto

```bash
rate(fraud_predictions_total[1m])
```


### Painel 2: taxa de fraude

```bash
rate(fraud_predictions_total[5m]) / rate(fraud_requests_total[5m])
```

### Painel 3: score médio

```bash
fraud_score_avg
```

⚠️ Antes disso: garantir Prometheus conectado

Se não aparecer nada:

Vá em Settings → Data Sources
Add → Prometheus
URL:



```bash
http://prometheus:9090
```



### 1. Airflow - Ver logs via terminal (Docker)

```bash
docker-compose logs -f airflow-scheduler

docker-compose exec airflow-scheduler airflow tasks logs ingestion_pipeline ingest_data 2026-04-20
```


### 1. Voltar pasta

```bash
cd /mnt/d/Tedokon/Projetos/FIAP/Projetos_Tech_Challenge_Fase5/v5_v2/datathon-grupo-05_v4
```




### 1. Docker - REBUILD

```bash
docker compose down -v

docker compose up -d --build
```







## ✅ SOLUÇÃO (direta e prática) 
### 1. Pare tudo

```bash
docker compose down -v
```

### 1. Pare tudo

```bash
docker compose down -v
```

### 2. Suba só o Postgres

```bash
docker compose up -d postgres
```

### 3. Rode o init do Airflow (ESSENCIAL)

```bash
docker compose up airflow-init

docker compose run airflow-webserver airflow users create \
  --username admin \
  --password admin \
  --firstname admin \
  --lastname admin \
  --role Admin \
  --email admin@email.com

```


# 4. Suba tudo

```bash
docker compose up -d
```

```bash
docker compose run airflow-webserver airflow db upgrade
```



# 1. Mata TUDO que está rodando
```bash
docker kill $(docker ps -q)
```

# 2. Remove TODOS containers
```bash
docker rm $(docker ps -aq)
```

# 3. Remove TODOS volumes
```bash
docker volume rm $(docker volume ls -q)
```

# 4. (IMPORTANTE) limpa imagens também
```bash
docker rmi $(docker images -q) -f
```

# 5. Suba novamente
```bash
docker compose up -d
```

# 6. Validação FINAL

```bash
docker logs datathon-grupo-05_v4-airflow-init-1
```




### Simulação de FRAUDE

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d ' {
 "amount": 1825,
  "user_id": 103,
  "device_id": "dev_271",
  "lat": -24.5,
  "lon": -49.6,
  "merchant_lat": -24.7,
  "merchant_lon": -49.0
} '
```


## Forcar dados externos

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '  {
 "amount": 1257,
  "user_id": 103,
  "device_id": "new_device",
  "lat": -24.5,
  "lon": -49.6,
  "merchant_lat": -24.7,
  "merchant_lon": -49.0
}

'