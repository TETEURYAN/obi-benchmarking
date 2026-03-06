# Problem Understanding Service

Microsserviço (agente de compreensão) para avaliar se o usuário entendeu corretamente um problema de programação competitiva. Parte de uma plataforma educacional baseada em agentes de IA para maratonas de programação.

## Arquitetura (Clean Architecture)

- **domain/** – Entidades (`Problem`, `UserAnswer`) e interface do serviço de avaliação
- **application/** – Caso de uso `EvaluateUnderstandingUseCase`
- **infrastructure/** – Implementação com PydanticAI (dois agentes: avaliação + feedback pedagógico)
- **interfaces/api/** – FastAPI (rotas e schemas Pydantic)
- **config/** – Configuração via ambiente (pydantic-settings)

## Requisitos

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (gerenciador de ambiente e dependências)

## Setup com UV

```bash
cd problem_understanding_service
uv sync
cp .env.example .env
# Edite .env e configure OPENAI_API_KEY (ou outro provider) e LLM_MODEL
```

## Executar

```bash
uv run python main.py
```

Ou com uvicorn diretamente:

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API disponível em `http://localhost:8000`. Documentação interativa: `http://localhost:8000/docs`.

## Endpoint

### POST /evaluate-understanding

Avalia a compreensão do usuário. Corpo da requisição:

```json
{
  "problema": {
    "titulo": "...",
    "descricao": "...",
    "objetivo": { ... },
    "entrada": { ... },
    "saida": { ... },
    "restricoes": { ... },
    "conceitos_envolvidos": [ ... ],
    "exemplos": [ ... ]
  },
  "resposta_usuario": {
    "ideia": "Resumo da ideia do usuário",
    "interpretacao_entrada": "Como o usuário entende a entrada",
    "interpretacao_saida": "Como o usuário entende a saída"
  }
}
```

Resposta (apenas duas possibilidades):

- `{ "result": "CORRETO" }`
- `{ "result": "ERRADO" }`

Quando a resposta é **ERRADO**, o sistema gera internamente um feedback pedagógico estruturado (o que está incorreto, conceitos mal compreendidos, correção, dicas) e registra em log; esse feedback não é retornado na API e pode ser usado depois pelo agente de feedback.

## Exemplo com curl

```bash
curl -X POST http://localhost:8000/evaluate-understanding \
  -H "Content-Type: application/json" \
  -d '{
    "problema": {
      "titulo": "Soma de Dois Números",
      "descricao": "Dados dois números inteiros, calcule a soma.",
      "objetivo": {"descricao": "Retornar a soma de A e B"},
      "entrada": {"formato": "Dois inteiros A e B em uma linha", "exemplo": "2 3"},
      "saida": {"formato": "Um inteiro: A + B", "exemplo": "5"},
      "restricoes": {},
      "conceitos_envolvidos": ["aritmética básica"],
      "exemplos": [{"entrada": "2 3", "saida": "5"}]
    },
    "resposta_usuario": {
      "ideia": "O problema pede a soma de dois números lidos da entrada.",
      "interpretacao_entrada": "Dois inteiros na mesma linha, separados por espaço.",
      "interpretacao_saida": "Um único inteiro: a soma dos dois números."
    }
  }'
```

## Docker

```bash
docker build -t problem-understanding-service .
docker run -p 8000:8000 --env-file .env problem-understanding-service
```

## Testes com Bruno

A pasta `bruno/` contém uma coleção para testar a API no [Bruno](https://www.usebruno.com/). Abra a pasta como coleção e execute as requisições **Health Check** e **Evaluate Understanding**. Veja `bruno/README.md`.

## Configuração (.env)

| Variável       | Descrição                          | Default              |
|----------------|------------------------------------|----------------------|
| `LLM_MODEL`    | Modelo PydanticAI (ex.: openai:gpt-4o-mini) | openai:gpt-4o-mini |
| `API_HOST`     | Host do servidor                   | 0.0.0.0              |
| `API_PORT`     | Porta do servidor                  | 8000                 |
| `ENVIRONMENT`  | development / staging / production | development          |

Para modelos OpenAI, defina `OPENAI_API_KEY` no ambiente ou no `.env`.

## Troubleshooting — "Serviço de avaliação temporariamente indisponível"

## Extensibilidade

- **Troca de LLM:** implemente `EvaluationService` em outra classe (ex.: outro provider) e injete no use case; o modelo padrão é definido em `LLM_MODEL` / `get_settings().llm_model`.
- **Reuso por outros agentes:** a pasta `infrastructure/llm` e os schemas em `interfaces/api/schemas.py` podem ser referência para os demais agentes (planejamento, implementação, testes).
