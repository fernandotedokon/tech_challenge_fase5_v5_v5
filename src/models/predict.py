# ==============================
# src/models/predict.py
# ==============================
def predict(model, features):
    return model.predict_proba([features])[0][1]
