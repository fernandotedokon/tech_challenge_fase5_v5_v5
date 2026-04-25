# ==============================
# DRIFT DETECTION
# ==============================
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset


def detect_drift(ref, curr):
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=curr)
    report.save_html("drift_report.html")
    