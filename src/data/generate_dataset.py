import numpy as np
import pandas as pd

np.random.seed(42)

def generate(n=5):

    data = []

    for i in range(n):

        user_id = np.random.randint(1, 500)
        device_id = np.random.choice(
            [f"dev_{np.random.randint(1, 300)}", "new_device"],
            p=[0.95, 0.05]
        )

        amount = np.random.exponential(2000)
        lat = np.random.uniform(-25, -20)
        lon = np.random.uniform(-50, -45)

        merchant_lat = lat + np.random.normal(0, 0.1)
        merchant_lon = lon + np.random.normal(0, 0.1)

        # =========================
        # FRAUD RULES (SINAL REAL)
        # =========================
        fraud_score = 0

        if amount > 200:
            fraud_score += 0.4

        if device_id == "new_device":
            fraud_score += 0.3

        distance = ((lat - merchant_lat)**2 + (lon - merchant_lon)**2) ** 0.5
        if distance > 1.0:
            fraud_score += 0.4

        is_fraud = 1 if fraud_score > 0.6 else 0

        data.append([
            amount,
            user_id,
            device_id,
            lat,
            lon,
            merchant_lat,
            merchant_lon,
            is_fraud
        ])

    df = pd.DataFrame(data, columns=[
        "amount", "user_id", "device_id",
        "lat", "lon",
        "merchant_lat", "merchant_lon",
        "target"
    ])

    df.to_csv("/opt/airflow/data/processed/train_fraud.csv", index=False)
    print("Dataset gerado com fraude realista!")

if __name__ == "__main__":
    generate()
