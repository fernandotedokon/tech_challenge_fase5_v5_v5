# ==============================
# src/features/build_features.py
# ==============================

import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))


def build_features(df: pd.DataFrame):

    # Velocity (transações por usuário)
    df['tx_count_1h'] = df.groupby('user_id')['timestamp'].transform('count')

    # Valor relativo
    df['amount_mean_user'] = df.groupby('user_id')['amount'].transform('mean')
    df['amount_ratio'] = df['amount'] / (df['amount_mean_user'] + 1)

    # Geo distance
    df['geo_distance'] = df.apply(lambda x: haversine(
        x['lat'], x['lon'], x['merchant_lat'], x['merchant_lon']), axis=1)

    # Device fingerprint simples
    df['device_risk'] = df.groupby('device_id')['device_id'].transform('count')

    return df
