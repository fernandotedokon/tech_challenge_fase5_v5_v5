from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

from src.api.schemas import Transaction
from src.api.service import build_features
from src.domain.fraud_rules import fraud_rule_engine
from src.db.repository import save_prediction

import joblib
import os
import time
import traceback

from prometheus_client import Counter, Histogram, Gauge, generate_latest

# =========================
# INIT
# =========================

app = FastAPI(title="Fraud Detection API")

MODEL_PATH = "/app/models/model.pkl"
model = None

# =========================
# METRICS
# =========================

REQUEST_COUNT = Counter(
    "fraud_requests_total",
    "Total de requisições"
)

FRAUD_PREDICTIONS = Counter(
    "fraud_predictions_total",
    "Total de fraudes detectadas"
)

LATENCY = Histogram(
    "request_latency_seconds",
    "Latência da API"
)

AVG_SCORE = Gauge(
    "fraud_score_avg",
    "Score médio de fraude"
)

# =========================
# LOAD MODEL
# =========================

@app.on_event("startup")
def load_model():
    global model

    try:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Modelo não encontrado em {MODEL_PATH}")

        model = joblib.load(MODEL_PATH)

        print(f"Modelo carregado com sucesso: {type(model)}")

    except Exception:
        print("ERRO AO CARREGAR MODELO:")
        traceback.print_exc()
        model = None


# =========================
# HEALTHCHECK
# =========================

@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": model is not None
    }


# =========================
# PREDICT
# =========================
#load_dotenv("configure.env")

@app.post("/predict")
def predict(transaction: Transaction):

    global model

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo indisponível (não carregado)"
        )

    start_time = time.time()

    try:
        REQUEST_COUNT.inc()

        # =========================
        # RULE ENGINE (MESMA DO GENERATE)
        # =========================
        #rule_score, rule_fraud = fraud_rule_engine(transaction)
        rule_score, rule_fraud = fraud_rule_engine(
            transaction.amount,
            transaction.device_id,
            transaction.lat,
            transaction.lon,
            transaction.merchant_lat,
            transaction.merchant_lon
        )

        # =========================
        # BUILD FEATURES
        # =========================
        features = build_features(transaction)
        model_score  = model.predict_proba(features)[0][1]

        # =========================
        # COMBINACAO (hibrida)
        # =========================
        final_score = (model_score * 0.7) + (rule_score * 0.3)
        is_fraud = final_score > 0.5

        # =========================
        # METRICS
        # =========================
        if is_fraud:
            FRAUD_PREDICTIONS.inc()

        LATENCY.observe(time.time() - start_time)
        AVG_SCORE.set(model_score)

        # =========================
        # SAVE DATABASE
        # =========================
        try:
            save_prediction(transaction, model_score, is_fraud)
        except Exception as db_error:
            print("Erro ao salvar no banco:", db_error)

        # =========================
        # RESPONSE
        # =========================
        return {
            "fraud_score": float(final_score),
            "rule_score": float(rule_score),
            "model_score": float(model_score),
            "is_fraud": bool(is_fraud)
        }

    except Exception:
        print("ERRO COMPLETO:")
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail="Erro interno na predição"
        )

"""
def fraud_rule_engine(transaction):

    fraud_score = 0

    if transaction.amount > 200:
        fraud_score += 0.4

    if transaction.device_id == "new_device":
        fraud_score += 0.3

    distance = (
        (transaction.lat - transaction.merchant_lat)**2 +
        (transaction.lon - transaction.merchant_lon)**2
    ) ** 0.5

    if distance > 1.0:
        fraud_score += 0.4

    is_fraud = fraud_score > 0.6

    return fraud_score, is_fraud

"""


# =========================
# METRICS (PROMETHEUS)
# =========================

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")