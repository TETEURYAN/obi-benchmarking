# Agentes LLM (Etapa 1 — Compreensão)

Esta pasta contém **duas implementações de exemplo** da porta de domínio `ComprehensionAgentPort`:

## 1. PydanticAI (`pydantic_ai_agents/comprehension_agent.py`)

- **Classe:** `PydanticAIComprehensionAgent`
- **Uso:** output estruturado via Pydantic; o modelo da LLM retorna um JSON que é validado e convertido em `ComprehensionOutput`.
- **Vantagens:** tipagem forte, retry e validação automáticos pelo PydanticAI.
- **Config:** `COMPREHENSION_AGENT=pydantic_ai` (padrão).

## 2. LangChain (`langchain_pipelines/comprehension_pipeline.py`)

- **Classe:** `LangChainComprehensionPipeline`
- **Uso:** pipeline `prompt -> LLM -> JsonOutputParser`; o prompt é carregado da mesma pasta versionada (`prompts/v1/comprehension.txt`).
- **Vantagens:** integração com ecossistema LangChain (chains, memory, tools no futuro).
- **Config:** `COMPREHENSION_AGENT=langchain`.

Ambas implementam a mesma porta (`ComprehensionAgentPort`) e são intercambiáveis via configuração. O use case `Etapa1ComprehensionUseCase` recebe a implementação por injeção de dependência em `dependencies.get_comprehension_agent()`.

### Trocar de implementação

No `.env`:

```env
COMPREHENSION_AGENT=pydantic_ai   # ou langchain
PROMPT_VERSION=v1
```
