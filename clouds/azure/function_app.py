
import azure.functions as func
import time, json, datetime

app = func.FunctionApp()

@app.route(route="worker_azure", auth_level=func.AuthLevel.ANONYMOUS)
def worker(req: func.HttpRequest):
    start = time.time()
    location = req.params.get("location", "UNKNOWN")

    simulated_latency = random.uniform(80, 120)
    time.sleep(simulated_latency / 1000)

    latency = (time.time() - start) * 1000

    return func.HttpResponse(
        json.dumps({
            "provider": "azure",
            "region": "brazilsouth",
            "location": location,
            "latency_ms": round(latency, 2),
            "success": True,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }),
        mimetype="application/json"
    )
