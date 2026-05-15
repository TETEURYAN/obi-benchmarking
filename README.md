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
GEMINI__API_KEY=seu-api-key-aqui
GEMINI__BASE_URL=https://openrouter.ai/api/v1 #Utilizando openrouter
GEMINI__MODEL_NAME=google/gemini-3.1-pro-preview
GEMINI__INPUT_PRICE=0.000002 # Entrada: 2U$ por 1M tokens
GEMINI__OUTPUT_PRICE=0.000012 # Saída: 12U$ por 1M tokens
```

## Banco de questões

- Antes de executar o sistema, extraia as questões compactadas em `database/file.zip` para a pasta `database/` para que o `core/orchestrator.py` consiga localizar os problemas.

Exemplo:

```bash
unzip database/file.zip -d database/
```

## Uso

1. Execute o programa interativo:
   ```bash
   uv run main.py
   ```

2. Crie ou escolha um ambiente de saída (número):
   - `0` = Criar um ambiente
   - `1` = Ambiente 1 (diretório de output)
   - `2` = Ambiente 2 (diretório de output)

3. Informar para executar apenas 1 ano:
   - Informe um ano entre 1999 a 2025

4. Selecione a estratégia de prompting:
   - `1` = Zero-shot (sem exemplos)
   - `2` = Few-shot (com exemplos)

5. Selecione a linguagem de programação:
   - `1` = Python
   - `2` = C++

6. O sistema irá:
   - Carregar problemas do database
   - Gerar soluções usando os modelos LLM configurados
   - Executar testes com casos de teste
   - Gerar relatórios em CSV

7. Verifique os resultados em `output/results/`

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
- `output/[ambiente criado pelo usuário]/[modelo]/[tipo]/[linguagem]/`: Código-fonte gerado e artefatos
- `output/[ambiente criado pelo usuário]/results/`: Arquivos CSV com métricas
   - `results_[modelo]_[linguagem]_[tipo].csv`: Desempenho por problema

## Estrutura do Projeto Geral

```
├── core/                      # Configuração e orquestração
│   ├── config.py              # Carregamento de credenciais
│   └── orchestrator.py        # Lógica principal de execução
├── database/                  # Problemas da OBI (extrair database/file.zip)
│   ├── [questao_1]/
│   │   └── problem.json
│   ├── [questao_2]/
│   │   └── problem.json
│   └── ...
├── models/                    # Modelos de dados Pydantic
├── prompts/                   # Templates de prompts (zero-shot, few-shot)
├── services/                  # Serviços de LLM e avaliação
├── output/                    # Resultados gerados
│   └── [ambiente]/
│       ├── [modelo]/
│       │   ├── [tipo]/
│       │   │   └── [linguagem]/
│       │   └── ...
│       └── results/           # CSVs com métricas
└── metrics/                   # Notebooks para análise
```

## Notebook de Análise

Execute análises detalhadas em `metrics/model_metrics.ipynb`, isso foi adicionado de forma manual. Será implementado de forma que fique automático os valores.
