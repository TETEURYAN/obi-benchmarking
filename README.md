# Polya Evaluation Script

This script evaluates LLM models based on Polya's method (multi-agent approach) or a standard Zero-Shot approach. It is primarily designed for solving OBI (Olimpíada Brasileira de Informática) problems.

> [!IMPORTANT]
> Os resultados contidos na pasta `resultados` foram obtidos utilizando **apenas a abordagem Zero-Shot**.

## Setup

1. Install `uv` if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Set your API configuration:
   Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   # Edit .env with your actual values (OPENAI_API_KEY, OPENAI_BASE_URL, etc.)
   ```

## Usage

### Single Model Execution
To run a single model defined in your `.env` or using the default:
```bash
uv run main.py
```

### Multi-Model Execution
To run multiple models sequentially from a text file:
```bash
uv run main.py --models-file models/models.txt
```

### Zero-Shot Mode
To run using a single zero-shot prompt instead of the multi-agent Polya approach:
```bash
uv run main.py --zero-shot
```

## Results Structure

Evaluation results are saved in the `resultados` directory with the following structure:

- `resultados/`: Base results folder.
    - `<model_name>/`: Model-specific folder.
        - `results_<model_name_safe>_<timestamp>_<shot_status>.csv`: Detailed execution results for each test case.
    - `summary_results_<run_timestamp>_<shot_status>.csv`: Consolidated metrics for all models evaluated in a single run.

## Project Structure

- `main.py`: Main entry point and orchestration script.
- `src/`: Core logic and configurations.
    - `models.py`: Pydantic data models for problems and evaluation results.
    - `prompts.py`: Prompt templates for Polya steps and zero-shot mode.
    - `evaluator.py`: Logic for code execution and correctness verification.
- `test_cases/`: Directory containing input and solution files for the problems.
- `problems.json`: Dataset of problem statements and examples.
