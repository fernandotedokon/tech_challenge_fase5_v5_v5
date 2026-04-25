# ==============================
# INGESTÃO VIA API EXTERNA
# ==============================
import requests


def fetch_external_data():
    response = requests.get("https://api.mockfraud.com/transactions")
    data = response.json()
    return pd.DataFrame(data)

