from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
import pandas as pd
import mlflow
import joblib
import os

from src.api.service import build_features_df

def train():

    print("Iniciando treino...")
    df = pd.read_csv("/opt/airflow/data/processed/train_fraud.csv")

    print("Dataset:", df.shape)
    print("Colunas:", df.columns)

    X = build_features_df(df)
    y = df["target"]

    print("Treinando modelo...")

    model = XGBClassifier(
        n_estimators=500,
        max_depth=8,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=10,
        eval_metric="auc"
    )

    model.fit(X, y)

    preds = model.predict_proba(X)[:, 1]
    auc = roc_auc_score(y, preds)

    print("AUC:", auc)

    mlflow.set_tracking_uri("http://mlflow:5000")

    with mlflow.start_run():
        mlflow.log_metric("auc", auc)

    os.makedirs("/app/models", exist_ok=True)
    joblib.dump(model, "/opt/airflow/models/model.pkl")

    print("Modelo salvo! Treino finalizado")

if __name__ == "__main__":
    train()