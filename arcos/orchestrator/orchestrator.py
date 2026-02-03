import os
import time
from datetime import datetime

from arcos.cache.decision_cache import DecisionCache
from arcos.clients.azure_client import call_azure
from arcos.clients.aws_client import call_aws

cache = DecisionCache() # (1h TTL)


def handle_request(user_location: str):
    """
        1. Mede tempo de decisão
        2. Consulta cache
        3. Executa função na nuvem escolhida
        4. Mede latência real (tempo do orquestrador -> processamento na nuvem -> obter e processar a resposta)
    """

    request_start = time.time()

    # Decisão
    decision_start = time.time()
    cached_provider = cache.get(user_location)

    if cached_provider:
        provider = cached_provider
        cache_used = True
    else:
        provider = "azure" if user_location == "BR" else "aws"
        cache.set(user_location, provider)
        cache_used = False


    decision_time_ms = (time.time() - decision_start) * 1000

    # Execução
    execution_start = time.time()

    if provider == "azure":
        cloud_response = call_azure(user_location)
    elif provider == "aws":
        cloud_response = call_aws(user_location)
    else:
        raise ValueError("Provider inválido")

    execution_time_ms = (time.time() - execution_start) * 1000

    total_time_ms = (time.time() - request_start) * 1000

    # Resultado
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "provider": provider,
        "cache_used": cache_used,
        "user_location": user_location,
        "decision_time_ms": round(decision_time_ms, 2),
        "execution_time_ms": round(execution_time_ms, 2),
        "total_latency_ms": round(total_time_ms, 2),
        "cloud_response": cloud_response
    }


def decide_provider(user_location: str) -> str:
    """
        Estratégia de decisão baseada em localização
    """

    # BR → Azure (Brazil South)
    # Outros → AWS (us-east-1)

    if user_location.upper() == "BR":
        return "azure"
    return "aws"
