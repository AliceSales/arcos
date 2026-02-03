import os
import requests
from dotenv import load_dotenv

load_dotenv()
AZURE_ENDPOINT = os.getenv("AZURE_WORKER_URL")
print(AZURE_ENDPOINT)
def call_azure(location):
    r = requests.get(AZURE_ENDPOINT, params={"location": location}, timeout=5)
    return r.json()
