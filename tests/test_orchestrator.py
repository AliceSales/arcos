import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from arcos.orchestrator.orchestrator import handle_request
print(handle_request("BR"))
print(handle_request("US"))
