def _fraud_rule_engine(amount, device_id, lat, lon, merchant_lat, merchant_lon):

    fraud_score = 0

    if amount > 200:
        fraud_score += 0.4

    if device_id == "new_device":
        fraud_score += 0.3

    distance = ((lat - merchant_lat)**2 + (lon - merchant_lon)**2) ** 0.5

    if distance > 1.0:
        fraud_score += 0.4

    is_fraud = fraud_score > 0.6

    return fraud_score, is_fraud