# Arquitetura Backend — Sistema Educacional Pólya

## 1. Visão geral da arquitetura

O backend segue **Clean Architecture** com camadas bem definidas e **SOLID**. O sistema é orientado a **agentes** (LLM) e **judges** (avaliação de código), organizado em etapas conforme a metodologia de George Pólya.

### Princípios

- **Domain** não depende de nada externo (entidades, value objects, portas).
- **Application** orquestra fluxos e depende apenas de portas do domínio (use cases, orchestrator).
- **Infrastructure** implementa portas (LLM, Judge, persistência) e pode ser trocada sem alterar domínio/aplicação.
- **Interfaces** expõem a aplicação via HTTP (FastAPI); convertem DTOs em entidades e resultados em respostas.

### Fluxo de dependência

```
Interfaces (HTTP) → Application (use cases, orchestrator) → Domain (entities, ports)
                                                                    ↑
Infrastructure (agents, judges, repos) ─────────────────────────────┘
```

### Categorias do sistema

| Categoria | Responsabilidade | Exemplos |
|-----------|------------------|----------|
| **Agentes** | Interagir com LLM (Pólya: compreensão, planejamento, implementação, análise) | ComprehensionAgent, PlanningAgent, ImplementationAgent, AnalysisAgent |
| **Judges** | Executar e avaliar código (testes) | ExternalJudgeAdapter (HTTP para judge externo) |
| **Orchestrator** | Encadear etapas, persistir contexto, decidir próximo passo | PolyaOrchestrator |
| **Repositórios** | Persistir contexto por etapa, códigos, feedback | EtapaContextRepository, UserImplementationRepository |

---

## 2. Diagrama conceitual dos agentes

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                   PolyaOrchestrator                      │
                    │  (controla ordem das etapas, persiste contexto, decide   │
                    │   quando chamar agente vs judge)                          │
                    └───────────────────────────┬───────────────────────────────┘
                                                │
    ┌───────────────────────────────────────────┼───────────────────────────────────────────┐
    │                                           │                                           │
    ▼                                           ▼                                           ▼
┌───────────────┐  contexto    ┌───────────────┐  contexto    ┌───────────────┐  código    ┌───────────────┐
│ Comprehension │ ──────────►  │  Planning     │ ──────────►  │ Implementation │ ────────► │    Judge      │
│    Agent      │   (etapa 1)  │    Agent      │   (etapa 2)  │    Agent       │           │  (externo)    │
│  (Etapa 1)    │              │  (Etapa 2)    │              │  (Etapa 3)     │           └───────┬───────┘
└───────────────┘              └───────────────┘              └────────────────┘                   │
       │                              │                                │                          │
       │ respostas usuário             │ respostas usuário              │ código gerado             │ pass/fail
       ▼                              ▼                                ▼                          ▼
┌───────────────┐              ┌───────────────┐              ┌───────────────┐              ┌───────────────┐
│  Persistência │              │  Persistência │              │  Persistência │              │  Casos de     │
│  contexto E1  │              │  contexto E2  │              │  (libera E4)  │              │  erro → LLM   │
└───────────────┘              └───────────────┘              └───────────────┘              └───────────────┘

    Etapa 4 (Implementação do usuário):
┌───────────────┐     código user + código LLM      ┌───────────────┐     código     ┌───────────────┐
│   Analysis    │ ────────────────────────────────► │    Judge      │ ◄───────────── │  Persistência │
│    Agent      │ ◄── feedback sutil                 │  (externo)    │ ─────────────► │  E4 + E5      │
└───────────────┘                                   └───────────────┘   pass/fail    └───────────────┘
```

---

## 3. Estrutura de diretórios

```
problem_understanding_service/
├── app/
│   ├── config/
│   │   └── settings.py
│   ├── domain/
│   │   ├── entities/
│   │   │   ├── problem.py
│   │   │   ├── user_answer.py
│   │   │   ├── etapa_context.py
│   │   │   └── user_implementation.py
│   │   ├── ports/
│   │   │   ├── agents/
│   │   │   │   ├── base.py          # Interface base do agente
│   │   │   │   ├── comprehension.py
│   │   │   │   ├── planning.py
│   │   │   │   ├── implementation.py
│   │   │   │   └── analysis.py
│   │   │   ├── judges/
│   │   │   │   └── judge.py         # Porta do Judge
│   │   │   └── repositories/
│   │   │       ├── etapa_context_repository.py
│   │   │       └── user_implementation_repository.py
│   │   └── value_objects/
│   │       └── etapa.py            # Enum Etapa (1..5)
│   ├── application/
│   │   ├── use_cases/
│   │   │   ├── etapa1_comprehension.py
│   │   │   ├── etapa2_planning.py
│   │   │   ├── etapa3_implementation_llm.py
│   │   │   ├── etapa4_user_implementation.py
│   │   │   └── etapa5_user_tests.py
│   │   ├── orchestrator/
│   │   │   └── polya_orchestrator.py
│   │   └── dto/
│   │       └── (schemas de entrada/saída da aplicação)
│   ├── infrastructure/
│   │   ├── llm/
│   │   │   ├── pydantic_ai_agents/
│   │   │   │   ├── base.py
│   │   │   │   ├── comprehension_agent.py
│   │   │   │   ├── planning_agent.py
│   │   │   │   ├── implementation_agent.py
│   │   │   │   └── analysis_agent.py
│   │   │   └── langchain_pipelines/
│   │   │       └── comprehension_pipeline.py   # Exemplo pipeline LangChain
│   │   ├── judges/
│   │   │   └── external_judge_adapter.py
│   │   ├── persistence/
│   │   │   └── (implementações de repositórios, ex.: sqlalchemy)
│   │   └── prompts/
│   │       ├── versions.py         # Versionamento
│   │       └── v1/
│   │           ├── comprehension.txt
│   │           ├── planning.txt
│   │           └── ...
│   └── interfaces/
│       └── api/
│           ├── routes/
│           │   ├── health.py
│           │   ├── etapa1.py
│           │   ├── etapa2.py
│           │   └── ...
│           ├── schemas/
│           │   └── (Pydantic request/response)
│           └── dependencies.py     # DI: get_agent, get_judge, get_repos
├── docs/
│   └── ARCHITECTURE.md             # Este documento
├── main.py
├── pyproject.toml
└── uv.lock
```

---

## 4. Design das camadas

### 4.1 Domain

- **Entities**: `Problem`, `UserAnswer`, `EtapaContext`, `UserImplementation`. Imutáveis onde fizer sentido; sem referência a frameworks.
- **Value objects**: `Etapa` (enum 1..5), possivelmente `Language`, `JudgeVerdict`.
- **Ports (interfaces)**:
  - **Agents**: `ComprehensionAgentPort`, `PlanningAgentPort`, etc. — cada um com um método `run(contexto_entrada) -> resultado_estruturado`.
  - **Judge**: `JudgePort.submit(code, language, problem_id) -> JudgeResult` (passed/failed, feedback, casos de erro opcionais).
  - **Repositories**: `EtapaContextRepository.save/load`, `UserImplementationRepository.save/load`.

### 4.2 Application

- **Use cases**: um por etapa (Etapa1ComprehensionUseCase, Etapa2PlanningUseCase, …). Cada um recebe DTOs, chama portas (agente e/ou repositório, judge), retorna DTO de saída.
- **Orchestrator**: `PolyaOrchestrator` — recebe “ação do usuário” + estado atual (id_questao, id_usuario, etapa atual), carrega contexto das etapas anteriores quando necessário, chama o use case correto, persiste resultado, decide próximo passo (ex.: após E3 passar no judge → liberar E4).
- **DTOs**: objetos de transferência entre interfaces e aplicação; validados na borda (Pydantic nos routes).

### 4.3 Infrastructure

- **Agentes**: implementações das portas usando PydanticAI (e opcionalmente LangChain para pipelines). Cada agente lê prompts de `infrastructure/prompts` (versionado).
- **Judges**: `ExternalJudgeAdapter` implementa `JudgePort`, chamando API HTTP do judge externo.
- **Persistência**: implementações dos repositórios (ex.: SQLAlchemy para PostgreSQL); tabelas conforme especificação (etapa, id_questao, id_usuario, contexto/codigo/feedback).
- **Prompts**: arquivos por etapa e versão (`v1/comprehension.txt`); carregados por um `PromptProvider` que pode ser trocado para A/B ou versionamento.

### 4.4 Interfaces

- **Routes**: FastAPI routers por etapa ou por recurso; convertem request body em DTOs, chamam orchestrator ou use case direto, convertem resultado em response.
- **Dependencies**: funções que instanciam implementações concretas (agents, judge, repos) e injetam nos use cases/orchestrator — permitindo testes com mocks.

---

## 5. Interfaces principais

### 5.1 Agente (porta base)

```python
# domain/ports/agents/base.py
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")

class AgentPort(ABC, Generic[InputT, OutputT]):
    @abstractmethod
    def run(self, input_data: InputT) -> OutputT:
        """Executa o agente com o contexto fornecido."""
        ...
```

### 5.2 Compreensão (Etapa 1)

```python
# domain/ports/agents/comprehension.py
# Input: problema + respostas às 4 perguntas
# Output: JSON com questao (resumo), perguntas (status + feedback por pergunta)
```

### 5.3 Planejamento (Etapa 2)

```python
# domain/ports/agents/planning.py
# Input: contexto_etapa1 + respostas do usuário (similar, técnicas, parte menor, linguagem)
# Output: JSON com avaliação das respostas
```

### 5.4 Implementação LLM (Etapa 3)

```python
# domain/ports/agents/implementation.py
# Input: contexto_etapa1 + contexto_etapa2 + linguagem
# Output: código completo (string)
```

### 5.5 Análise do código do usuário (Etapa 4)

```python
# domain/ports/agents/analysis.py
# Input: codigo_llm + codigo_user
# Output: compatibilidade ok/erro, erros de sintaxe, inconsistências, feedback sutil
```

### 5.6 Judge

```python
# domain/ports/judges/judge.py
class JudgeResult:
    passed: bool
    feedback: str | None
    failed_cases: list[dict] | None  # para retorno à LLM (E3), sem revelar ao usuário (E5)

class JudgePort(ABC):
    @abstractmethod
    def submit(self, code: str, language: str, problem_id: str, *, reveal_inputs: bool = False) -> JudgeResult:
        ...
```

### 5.7 Repositórios

```python
# domain/ports/repositories/etapa_context_repository.py
class EtapaContextRepository(ABC):
    def save(self, etapa: Etapa, id_questao: str, id_usuario: str, contexto: dict) -> None: ...
    def load(self, etapa: Etapa, id_questao: str, id_usuario: str) -> dict | None: ...

# domain/ports/repositories/user_implementation_repository.py
class UserImplementationRepository(ABC):
    def save_etapa4(self, id_questao: str, id_usuario: str, codigo_llm: str, codigo_user: str, feedback: str) -> None: ...
    def save_etapa5(self, id_questao: str, id_usuario: str, status: str, feedback_inputs: str | None) -> None: ...
```

---

## 6. Fluxo do sistema

1. **Etapa 1 — Compreensão**  
   Usuário envia respostas às 4 perguntas. API chama `Etapa1ComprehensionUseCase` → `ComprehensionAgent.run(problema + respostas)` → LLM retorna JSON (resumo + avaliação por pergunta). Use case persiste em `EtapaContextRepository` (etapa=1) e retorna o JSON ao cliente.

2. **Etapa 2 — Planejamento**  
   Usuário envia respostas (similar, técnicas, parte menor, linguagem). Use case carrega contexto da etapa 1, chama `PlanningAgent.run(contexto_etapa1 + respostas)` → persiste contexto etapa 2 e retorna avaliação.

3. **Etapa 3 — Implementação automática (LLM)**  
   Orchestrator (ou use case) carrega contexto 1 e 2, chama `ImplementationAgent.run(contexto_etapa1 + contexto_etapa2 + linguagem)` → recebe código. Chama `Judge.submit(codigo, linguagem, problem_id)`. Se passou: marca “liberar E4” e retorna sucesso. Se falhou: retorna casos de erro para o agente corrigir (loop até passar ou limite).

4. **Etapa 4 — Implementação do usuário**  
   Usuário envia código. Use case carrega código LLM e contexto necessário, chama `AnalysisAgent.run(codigo_llm, codigo_user)` → se ok, chama Judge e persiste em `UserImplementation` (codigo_llm, codigo_user, feedback). Se erro, retorna feedback sutil.

5. **Etapa 5 — Testes do usuário**  
   Judge executa com `reveal_inputs=False`. Resultado (pass/fail, feedback sem inputs) é persistido e retornado. Se passou → problema concluído.

---

## 7. Estratégias

- **Escalabilidade**: Stateless por request; estado em PostgreSQL. Filas (Celery/RQ) podem ser adicionadas para E3 (re-tentativas de código LLM) sem mudar portas.
- **Novos agentes**: Criar nova porta em `domain/ports/agents/`, implementação em `infrastructure/llm/`, registrar no orchestrator ou novo use case.
- **Novos judges**: Nova implementação de `JudgePort` em `infrastructure/judges/` e configurar qual usar (env ou factory).
- **Versionamento de prompts**: `PromptProvider` recebe versão (ex.: v1); diretório `prompts/v1/`, `prompts/v2/`. Config ou feature flag escolhe a versão.

---

## 8. Código base inicial

O código base inicial está organizado conforme a estrutura acima, com:

- Domain: entidades, value object `Etapa`, portas de agentes (base + comprehension), Judge e repositórios.
- Application: use case da etapa 1 e esqueleto do orchestrator.
- Infrastructure: agente de compreensão com PydanticAI, pipeline LangChain de exemplo, adapter do Judge (HTTP), provider de prompts e repositório em memória para desenvolvimento.
- Interfaces: schemas Pydantic e rota `POST /etapa1/compreensao` com injeção de dependências.

Os exemplos de implementação de um agente, pipeline LangChain, PydanticAI, chamada ao Judge e endpoint FastAPI estão nos arquivos referenciados nas seções 9–12 abaixo.

---

## 9. Exemplo de implementação de um agente (Compreensão)

Existem **duas implementações** da porta `ComprehensionAgentPort`:

1. **PydanticAI** — `app/infrastructure/llm/pydantic_ai_agents/comprehension_agent.py`
   - `PydanticAIComprehensionAgent`: usa `Agent` do PydanticAI com `output_type=ComprehensionOutputModel`; carrega prompt de `prompts/v1/comprehension.txt`.
   - Saída estruturada garantida por Pydantic; conversão para `ComprehensionOutput` (TypedDict) via `_output_to_dict`.

2. **LangChain** — `app/infrastructure/llm/langchain_pipelines/comprehension_pipeline.py`
   - `LangChainComprehensionPipeline`: pipeline `ChatPromptTemplate | ChatOpenAI | JsonOutputParser`; mesmo prompt versionado.
   - Normalização do JSON em `_normalize_output` para o formato `ComprehensionOutput`.

A escolha é feita por configuração: `COMPREHENSION_AGENT=pydantic_ai` (padrão) ou `COMPREHENSION_AGENT=langchain`. Ver `app/infrastructure/llm/README.md`.

---

## 10. Exemplo de pipeline LangChain

Ver `app/infrastructure/llm/langchain_pipelines/comprehension_pipeline.py`: pipeline opcional que pode encadear prompt + LLM + parser, reutilizável como alternativa ao agente PydanticAI puro.

---

## 11. Exemplo de chamada ao Judge

- **Porta:** `app/domain/ports/judges/judge.py` — `JudgePort.submit(code, language, problem_id, reveal_inputs=...)` retorna `JudgeResult(passed, feedback, failed_cases)`.
- **Adapter:** `app/infrastructure/judges/external_judge_adapter.py` — `ExternalJudgeAdapter` faz POST para `{base_url}/submit` com JSON `code`, `language`, `problem_id`, `reveal_inputs` e interpreta a resposta.
- **Endpoint:** `POST /judge/submit` — body: `JudgeSubmitRequest` (code, language, problem_id, reveal_inputs); response: `JudgeSubmitResponse` (passed, feedback, failed_cases). A rota usa `get_judge()` de `dependencies` e chama `judge.submit(...)`.
- **Config:** `JUDGE_BASE_URL`, `JUDGE_TIMEOUT_SECONDS` em settings.

---

## 12. Exemplo de endpoint FastAPI

Ver `app/interfaces/api/routes/etapa1.py`: `POST /etapa1/compreensao` recebe problema + respostas, usa `get_comprehension_use_case()` (DI), chama use case, persiste contexto e retorna o JSON da etapa 1.

---

*Documento gerado como parte da refatoração da arquitetura backend do sistema educacional Pólya.*
