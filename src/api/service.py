import pandas as pd

# =========================
# CORE FEATURE ENGINEERING (REUTILIZÁVEL)
# =========================
def build_features_df(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["device_hash"] = df["device_id"].apply(lambda x: hash(x) % 1000)

    df["geo_distance"] = (
        (df["lat"] - df["merchant_lat"])**2 +
        (df["lon"] - df["merchant_lon"])**2
    ) ** 0.5

    return df[[
        "amount",
        "user_id",
        "device_hash",
        "geo_distance"
    ]]

# =========================
# API WRAPPER (1 registro)
# =========================
def build_features(transaction):

    df = pd.DataFrame([transaction.dict()])

    return build_features_df(df)
