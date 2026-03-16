# OBI LLM Evaluation Framework

Sistema de avaliação de modelos LLM (Large Language Models) em problemas da Olimpíada Brasileira de Informática (OBI). O framework testa diferentes estratégias de prompting (zero-shot e few-shot) e linguagens de programação (Python e C++) para gerar soluções automaticamente.

## Setup

### 1. Instalar `uv` (se ainda não instalado)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Instalar dependências
```bash
uv sync
```

### 3. Configurar credenciais de API

Crie um arquivo `.env` baseado em `.env.example`:
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais:
```
OPENAI__API_KEY=seu-api-key-aqui
OPENAI__BASE_URL=https://api.openai.com/v1
OPENAI__MODEL_NAME=gpt-4o

GEMINI__API_KEY=seu-api-key-aqui
GEMINI__BASE_URL=https://api.google.com/v1
GEMINI__MODEL_NAME=gemini-pro
```

## Estrutura do Projeto

```
experimento_2/
├── core/                   # Configuração e orquestração
│   ├── config.py          # Carregamento de credenciais
│   └── orchestrator.py    # Lógica principal de execução
├── database/              # Problemas da OBI
│   ├── obi_2023/
│   └── obi_2024/          # Anos 2023-2024 organizados por fase
├── models/                # Modelos de dados Pydantic
├── prompts/               # Templates de prompts (zero-shot, few-shot)
├── services/              # Serviços de LLM e avaliação
├── output/                # Resultados gerados
│   ├── [modelo]/          # Saída organizada por modelo
│   └── results/           # CSVs com métricas
└── metrics/               # Notebooks para análise
```

## Uso

1. Execute o programa interativo:
   ```bash
   uv run main.py
   ```

2. Selecione a estratégia de prompting:
   - `1` = Zero-shot (sem exemplos)
   - `2` = Few-shot (com exemplos)

3. Selecione a linguagem de programação:
   - `1` = Python
   - `2` = C++

4. O sistema irá:
   - Carregar problemas do database
   - Gerar soluções usando os modelos LLM configurados
   - Executar testes com casos de teste
   - Gerar relatórios em CSV

5. Verifique os resultados em `output/results/`

## Arquivos Principais

- `main.py`: Script de entrada com menu interativo
- `core/config.py`: Carregamento de configurações via `.env`
- `core/orchestrator.py`: Orquestração de execução
- `models/`: Modelos de dados (Problem, EvaluationResult, Level)
- `prompts/`: Templates de prompts para diferentes estratégias
- `services/llm_service.py`: Integração com APIs de LLM
- `services/judge_service.py`: Avaliação de soluções geradas

## Saídas Geradas

Os resultados são organizados em:
- `output/[modelo]/[tipo]/[linguagem]/`: Código-fonte gerado
- `output/results/`: Arquivos CSV com métricas
  - `results_[modelo]_[linguagem]_[tipo].csv`: Desempenho por problema
  - `level_to_questions_[modelo].csv`: Estatísticas por fase

## Notebook de Análise

Execute análises detalhadas em `metrics/model_metrics.ipynb`
