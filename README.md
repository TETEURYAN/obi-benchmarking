# Problem Understanding Service

Backend do sistema educacional baseado na **metodologia de George Pólya** (“How to Solve It”) para ensinar resolução de problemas de programação competitiva. O serviço expõe **agentes de IA** (LLM) e integração com **Judge** externo, organizado em **Clean Architecture** e **SOLID**.

## Visão geral

O sistema cobre as etapas de Pólya:

1. **Compreensão** — avaliar se o usuário entendeu entrada, saída e ideia do problema  
2. **Planejamento** — avaliar estratégia, técnicas e linguagem (estrutura pronta para expansão)  
3. **Implementação (LLM)** — gerar código e validar no Judge  
4. **Implementação do usuário** — análise do código do usuário e envio ao Judge  
5. **Testes do usuário** — executar testes sem revelar inputs  

**Tecnologias:** Python 3.11+, uv, FastAPI, PydanticAI, LangChain (opcional), Judge externo via HTTP.

---

## Arquitetura (Clean Architecture)

```
interfaces/api (FastAPI) → application (use cases, orchestrator) → domain (entities, ports)
                                                                         ↑
infrastructure (agents, judges, persistence, prompts) ────────────────────┘
```

| Camada | Conteúdo |
|--------|----------|
| **domain/** | Entidades (`Problem`, `UserAnswer`, `EtapaContext`, …), value objects (`Etapa`), **portas** (agentes, Judge, repositórios) |
| **application/** | Use cases por etapa (ex.: `Etapa1ComprehensionUseCase`), `PolyaOrchestrator` |
| **infrastructure/** | Implementações: agentes (PydanticAI, LangChain), `ExternalJudgeAdapter`, repositórios em memória, prompts versionados (`prompts/v1/`) |
| **interfaces/api/** | Rotas FastAPI, schemas Pydantic, `dependencies.py` (DI) |
| **config/** | Settings (pydantic-settings): LLM, Judge, ambiente, versão de prompts |

O domínio não depende de frameworks; agentes e Judge são **portas** implementadas na infraestrutura. Detalhes em `docs/ARCHITECTURE.md`.

---

## Requisitos

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (ambiente e dependências)

---

## Setup

```bash
cd problem_understanding_service
uv sync
cp .env.example .env
# Edite .env: OPENAI_API_KEY, LLM_MODEL, JUDGE_BASE_URL (se usar judge real)
```

---

## Executar

```bash
uv run python main.py
```

Ou com uvicorn:

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- API: `http://localhost:8000`  
- Docs: `http://localhost:8000/docs`

---

## Endpoints (rotas da API)

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/health` | Health check. Resposta: `{"status": "ok"}`. |
| POST | `/evaluate-understanding` | **(Legado)** Avalia compreensão (ideia + entrada + saída). Retorna `{"result": "CORRETO"}` ou `{"result": "ERRADO"}`. |
| POST | `/etapa1/compreensao` | **Etapa 1 — Compreensão.** Envia questão + respostas às 4 perguntas; retorna resumo da questão + avaliação por pergunta (status + feedback). Persiste contexto da etapa 1. |
| POST | `/judge/submit` | Submete código ao Judge externo. Body: `code`, `language`, `problem_id`, `reveal_inputs`. Retorna `passed`, `feedback`, `failed_cases`. |

### POST /etapa1/compreensao

Corpo da requisição:

```json
{
  "id_questao": "q1",
  "id_usuario": "u1",
  "descricao_questao": "Dados dois números inteiros, calcule a soma.",
  "formato_entrada": "Dois inteiros A e B em uma linha.",
  "formato_saida": "Um inteiro: A + B.",
  "exemplos": { "entrada": "2 3", "saida": "5" },
  "respostas_usuario": {
    "Quais são os dados de entrada (input)?": "Dois inteiros na mesma linha.",
    "Qual é a saída esperada (output)?": "Um inteiro com a soma.",
    "Existem condições especiais ou casos de borda?": "Não.",
    "Qual a ideia do problema?": "Ler dois números e imprimir a soma."
  }
}
```

Resposta (contexto da etapa 1 salvo no backend):

```json
{
  "questao": {
    "descricao": "...",
    "entrada_problema": "...",
    "saida_problema": "..."
  },
  "perguntas": {
    "Quais são os dados de entrada (input)?": { "status": "correto", "feedback": "..." },
    "Qual é a saída esperada (output)?": { "status": "correto", "feedback": "..." },
    "Existem condições especiais ou casos de borda?": { "status": "correto", "feedback": "..." },
    "Qual a ideia do problema?": { "status": "correto", "feedback": "..." }
  }
}
```

### POST /judge/submit

Corpo da requisição:

```json
{
  "code": "a, b = map(int, input().split())\nprint(a + b)",
  "language": "python3",
  "problem_id": "soma",
  "reveal_inputs": false
}
```

Resposta:

```json
{
  "passed": true,
  "feedback": null,
  "failed_cases": null
}
```

Quando `passed: false`, `feedback` e opcionalmente `failed_cases` trazem detalhes (com ou sem inputs conforme `reveal_inputs`).

### POST /evaluate-understanding (legado)

Mantido para compatibilidade. Corpo: `problema` (enunciado estruturado) + `resposta_usuario` (`ideia`, `interpretacao_entrada`, `interpretacao_saida`). Resposta: `{"result": "CORRETO"}` ou `{"result": "ERRADO"}`.

---

## Configuração (.env)

| Variável | Descrição | Default |
|----------|-----------|---------|
| `LLM_MODEL` | Modelo PydanticAI (ex.: openai:gpt-4o-mini) | openai:gpt-4o-mini |
| `COMPREHENSION_AGENT` | Agente da Etapa 1: `pydantic_ai` ou `langchain` | pydantic_ai |
| `PROMPT_VERSION` | Versão dos prompts (v1, v2, …) | v1 |
| `JUDGE_BASE_URL` | URL base do Judge externo | http://localhost:8080 |
| `JUDGE_TIMEOUT_SECONDS` | Timeout HTTP do Judge | 30 |
| `API_HOST` | Host do servidor | 0.0.0.0 |
| `API_PORT` | Porta do servidor | 8000 |
| `ENVIRONMENT` | development / staging / production | development |

Para modelos OpenAI, defina `OPENAI_API_KEY` no `.env`.

---

## Testes com Bruno

A pasta `bruno/` contém a coleção para testar a API no [Bruno](https://www.usebruno.com/):

1. Abra o Bruno → **Open Collection** → selecione a pasta `bruno`.
2. Selecione o environment **local** (`base_url: http://localhost:8000`).
3. Execute as requisições (Health, Evaluate Understanding legado, Etapa 1 Compreensão, Judge Submit).

Ver `bruno/README.md` para a lista completa de requisições.

---

## Docker

```bash
docker build -t problem-understanding-service .
docker run -p 8000:8000 --env-file .env problem-understanding-service
```

---

## Estrutura de pastas (resumo)

```
app/
├── config/           # settings (LLM, Judge, env, prompt version)
├── domain/            # entities, value_objects, ports (agents, judges, repositories)
├── application/       # use_cases (etapa1, ...), orchestrator
├── infrastructure/    # llm (pydantic_ai_agents, langchain_pipelines), judges, persistence, prompts
└── interfaces/api/   # routes, schemas, dependencies
docs/
└── ARCHITECTURE.md   # Design completo
bruno/                # Coleção de requisições
```

---

## Extensibilidade

- **Trocar agente de compreensão:** `COMPREHENSION_AGENT=langchain` ou implementar outra classe que satisfaça `ComprehensionAgentPort` e registrá-la em `dependencies.get_comprehension_agent()`.
- **Novos agentes (planejamento, implementação, análise):** criar porta em `domain/ports/agents/`, implementação em `infrastructure/llm/`, use case e rota em `application/` e `interfaces/api/routes/`.
- **Trocar Judge:** implementar `JudgePort` em `infrastructure/judges/` e configurar em `dependencies.get_judge()` (ex.: via `JUDGE_BASE_URL` ou factory).
- **Versionamento de prompts:** arquivos em `app/infrastructure/prompts/v1/`, `v2/`, …; `PROMPT_VERSION` escolhe a versão.

---

## Troubleshooting

- **503 “Serviço de compreensão temporariamente indisponível”:** falha na LLM (ex.: chave de API). Verifique `OPENAI_API_KEY` e logs.
- **503 “Judge temporariamente indisponível”:** Judge externo inacessível ou timeout. Verifique `JUDGE_BASE_URL` e rede; para desenvolvimento pode-se mockar o Judge.
