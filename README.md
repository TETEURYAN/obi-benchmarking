# Polya Framework: LLM Evaluation for Competitive Programming

Este repositório contém dois projetos experimentais para avaliação de Large Language Models (LLMs) em tarefas de programação competitiva, especificamente problemas da Olimpíada Brasileira de Informática (OBI). Os projetos implementam metodologias baseadas no método de resolução de problemas de Polya.

## Projetos

### Experimento 1: Comprehensive Multi-Agent Polya Evaluator

Um framework completo para avaliação de LLMs em problemas OBI usando duas abordagens:
- **Método Completo de Polya**: Pipeline de três etapas (Compreensão → Planejamento → Implementação)
- **Zero-Shot**: Geração direta de código com um único prompt

**Características principais:**
- Avaliação sequencial de múltiplos modelos LLM
- Julgamento abrangente de código (AC/WA/CE/RE/TLE)
- Execução paralela de casos de teste
- Capacidade de reavaliação sem chamar LLM novamente
- Agregação automática de resultados em CSVs

**Tecnologias:** OpenAI API, Python (openai, pandas, pydantic, python-dotenv)

### Experimento 2: Polya's Understanding & Planning Evaluator

Focado nas primeiras duas etapas do método de Polya: Compreensão e Planejamento. Avalia a capacidade dos LLMs de entender e planejar soluções para problemas de programação.

**Características principais:**
- Organização por níveis de dificuldade (OBI 2023/2024, nível 2)
- Estratégias Zero-shot e Few-shot
- Suporte a múltiplas linguagens (Python e C++)
- Suporte a múltiplos provedores (OpenAI e Gemini)
- Métricas abrangentes com notebook Jupyter para análise
- Interface interativa orientada a menu

**Tecnologias:** OpenAI e Gemini APIs, Python (pydantic, openai, pandas, numpy, jupyter)

## Diferenças Principais

| Aspecto | Experimento 1 | Experimento 2 |
|---------|---------------|---------------|
| **Escopo** | Geração completa + julgamento | Análise de planejamento e compreensão |
| **Etapas de Polya** | Todas 3 etapas | Primeiras 2 etapas |
| **Provedores LLM** | Apenas OpenAI | OpenAI + Gemini |
| **Linguagens** | Apenas Python | Python e C++ |
| **Execução** | Batch automatizado | Menu interativo |
| **Julgamento** | Completo (compilar, executar, classificar) | Apenas resultados de avaliação |
| **Organização** | Pasta única test_cases | Hierárquica por ano/nível |
| **Saída** | CSVs + métricas detalhadas | CSVs por modelo/estratégia + notebook |

## Instalação e Execução

### Experimento 1

1. Entre no diretório:
   ```bash
   cd experimento_1
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Copie `.env.example` e edite para `.env`:
   ```bash
   cp .env.example .env
   ```

4. Adicione as informações no `.env`:
   ```
   OPENAI_API_KEY=sua-chave-api-aqui
   OPENAI_BASE_URL=https://api.openai.com/v1
   MODEL_NAME=gpt-4o
   ```

5. Execute a aplicação:
   ```bash
   python main.py
   ```

### Experimento 2

1. Entre no diretório:
   ```bash
   cd experimento_2
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Copie `.env.example` e edite para `.env`:
   ```bash
   cp .env.example .env
   ```

4. Adicione as informações no `.env`, substituindo `EXAMPLE` pelo nome do provedor (ex: `OPENAI`):
   ```
   OPENAI__API_KEY=sua-chave-api-aqui
   OPENAI__BASE_URL=https://api.openai.com/v1
   OPENAI__MODEL_NAME=gpt-4o
   ```

5. Execute a aplicação:
   ```bash
   python main.py
   ```

## Mais Informações

Para detalhes específicos sobre cada projeto, consulte os arquivos `README.md` dentro dos diretórios `experimento_1` e `experimento_2`.