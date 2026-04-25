from prometheus_client import Histogram, REGISTRY

if "request_latency_seconds" in REGISTRY._names_to_collectors:
    REQUEST_LATENCY = REGISTRY._names_to_collectors["request_latency_seconds"]
else:
    REQUEST_LATENCY = Histogram(
        "request_latency_seconds",
        "Request latency",
        ["method", "endpoint"]
    )
