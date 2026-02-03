import json
import time
import random
from datetime import datetime

def handler(event, context):
    start = time.time()
    location = req.params.get("location", "UNKNOWN")

    simulated_latency = random.uniform(80, 120)
    time.sleep(simulated_latency / 1000)

    latency_ms = round((time.time() - start) * 1000, 2)

    response = {
        "provider": "aws",
        "region": "sa-east-1",
        "location": location,
        "latency_ms": latency_ms,
        "cost_per_request_usd": 0.0000002,
        "success": True,
        "timestamp": datetime.utcnow().isoformat(),
        "request_id": f"aws_{random.randint(1000,9999)}",
        "simulated": True
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
