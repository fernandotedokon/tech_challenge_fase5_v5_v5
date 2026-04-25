from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
    "fraud_retraining",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    generate_data = BashOperator(
        task_id="generate_dataset",
        bash_command="python /opt/airflow/src/data/generate_dataset.py"
        
    )

    predict = BashOperator(
        task_id="run_predict",
        bash_command="""
        curl -X POST http://api:8000/predict \
        -H "Content-Type: application/json" \
        -d '{
            "amount": 1500,
            "user_id": 123,
            "device_id": "new_device",
            "lat": -23.5,
            "lon": -46.6,
            "merchant_lat": -23.4,
            "merchant_lon": -46.5
        }'
        """
    )

    #train_model = BashOperator(
    #    task_id="train_model",
    #    bash_command="python /opt/airflow/src/models/train.py"
    #)

#    generate_data >> predict >> train_model
generate_data >> predict

