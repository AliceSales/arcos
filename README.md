# ARCOS – Orquestrador Multi-Cloud

Este projeto implementa um orquestrador simples para execução de funções em múltiplas nuvens (AWS e Azure),
com decisão baseada em contexto (localização do usuário) e cache de decisões.

O objetivo é avaliar estratégias adaptativas em ambientes multi-cloud, analisando métricas como latência,
uso de cache e seleção do provedor.

## Estrutura do Projeto

- arcos/
  - orchestrator/ (lógica de decisão)
  - cache/ (cache de decisões com TTL)
  - clients/ (clientes de chamada AWS e Azure)
- clouds/
  - azure/ (função Azure (worker))
  - aws/ (função AWS (worker))
- dashboard/
  - index.html (visualização dos dados)
  - data.json (métricas coletadas)
- tests/ (testes locais)

## Executar o Orquestrador Localmente

```bash
python tests/test_orchestrator.py
```

O orquestrador decide a nuvem, executa a função correspondente e registra métricas.

## Exibir o Dashboard

Entrar em dashboard e executar:

```bash
python -m http.server 8000
```
- Navegador:
    http://localhost:8000

O dashboard consome os dados do arquivo data.json(que estão mockados no momento :D).