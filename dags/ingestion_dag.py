from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os


def ingest():
    input_path = "/opt/airflow/data/raw/transactions.csv"
    output_dir = "/opt/airflow/data/processed"
    output_path = f"{output_dir}/train.csv"

    print("Verificando arquivo:", input_path)

    if not os.path.exists(input_path):
        raise Exception(f"Arquivo não encontrado: {input_path}")

    print("Lendo CSV...")
    df = pd.read_csv(input_path)

    print("Shape:", df.shape)

    os.makedirs(output_dir, exist_ok=True)

    print("Salvando arquivo...")
    df.to_csv(output_path, index=False)

    print("Sucesso! Arquivo criado:", output_path)


def create_dag():
    with DAG(
        dag_id="ingestion_pipeline",
        start_date=datetime(2024, 1, 1),
        schedule_interval="@daily",
        catchup=False,
    ) as dag:

        ingest_task = PythonOperator(
            task_id="ingest_data",
            python_callable=ingest
        )

        return dag


dag = create_dag()

