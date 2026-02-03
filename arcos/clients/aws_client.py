import os
import requests
from dotenv import load_dotenv

load_dotenv()

AWS_ENDPOINT = os.getenv("AWS_WORKER_URL")

def call_aws(location):
    r = requests.get(AWS_ENDPOINT, params={"location": location}, timeout=5)
    return r.json()
