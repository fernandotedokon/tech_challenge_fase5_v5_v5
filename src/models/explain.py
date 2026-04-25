# ==============================
# SHAP
# ==============================
import shap


def explain_prediction(model, X_sample):
    explainer = shap.Explainer(model)
    shap_values = explainer(X_sample)
    return shap_values.values.tolist()
