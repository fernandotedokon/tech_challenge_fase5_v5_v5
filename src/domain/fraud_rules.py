import os
#from dotenv import load_dotenv


def fraud_rule_engine(amount, device_id, lat, lon, merchant_lat, merchant_lon):

    #load_dotenv("configure.env")
    
    # =========================
    # LOAD CONFIG
    # =========================
    AMOUNT_THRESHOLD = float(os.getenv("AMOUNT_THRESHOLD", 200))
    AMOUNT_WEIGHT = float(os.getenv("AMOUNT_WEIGHT", 0.4))

    NEW_DEVICE_VALUE = os.getenv("NEW_DEVICE_VALUE", "new_device")
    DEVICE_WEIGHT = float(os.getenv("DEVICE_WEIGHT", 0.3))

    DISTANCE_THRESHOLD = float(os.getenv("DISTANCE_THRESHOLD", 1.0))
    DISTANCE_WEIGHT = float(os.getenv("DISTANCE_WEIGHT", 0.4))

    FRAUD_SCORE_THRESHOLD = float(os.getenv("FRAUD_SCORE_THRESHOLD", 0.6))

    # =========================
    # RULE ENGINE
    # =========================
    fraud_score = 0

    if amount > AMOUNT_THRESHOLD:
        fraud_score += AMOUNT_WEIGHT

    if device_id == NEW_DEVICE_VALUE:
        fraud_score += DEVICE_WEIGHT

    distance = ((lat - merchant_lat)**2 + (lon - merchant_lon)**2) ** 0.5

    if distance > DISTANCE_THRESHOLD:
        fraud_score += DISTANCE_WEIGHT

    is_fraud = fraud_score > FRAUD_SCORE_THRESHOLD

    return fraud_score, is_fraud

