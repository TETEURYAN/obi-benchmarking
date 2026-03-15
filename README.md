# Polya Evaluation Script

This script evaluates LLM models using two distinct approaches for solving OBI (Olimpíada Brasileira de Informática) problems:
1. **Multi-Agent (Polya's method):** A multi-step pipeline (Comprehension, Planning, Implementation).
2. **Zero-Shot:** A direct, single-prompt code generation.


> [!IMPORTANT]
> The results currently in the `resultados` folder were obtained using the **Zero-Shot** approach.

## Features

- **Multi-Model Support:** Evaluate several models sequentially from a configuration file.
- **Granular Judging:** Classifies solutions into AC (Accepted), WA (Wrong Answer), CE (Compilation Error), RE (Runtime Error), and TLE (Time Limit Exceeded).
- **Result Re-evaluation:** Capability to re-run the judge on existing generated code without calling the LLM again.
- **Parallel Testing:** Uses multi-threading to speed up test case execution.
- **Consolidated Metrics:** Automatically aggregates results into a summary CSV.

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

### Re-evaluate Existing Results
To re-run the judge on results already stored in the `resultados` directory:
```bash
uv run main.py --re-evaluate-results
```

## Judging Classifications

The evaluator classifies each problem execution based on standard competitive programming outcomes:

| Code | Meaning | Description |
| :--- | :--- | :--- |
| **AC** | Accepted | The code passed all test cases correctly within the time limit. |
| **WA** | Wrong Answer | The code produced an output different from the expected one. |
| **CE** | Compilation Error | The generated code failed to run (e.g., syntax errors). |
| **RE** | Runtime Error | The code crashed during execution. |
| **TLE** | Time Limit Exceeded | The code took longer than the allowed time per case (default 2s). |

## Results Structure

Evaluation results are saved in the `resultados` directory:

- `resultados/`: Base results folder.
    - `<model_name>/`: Model-specific folder.
        - `results_<model_name_safe>_<timestamp>_<shot_status>.csv`: Detailed results per test case.
    - `summary_results_<run_timestamp>_<shot_status>.csv`: Consolidated performance metrics for all models in a run.

## Project Structure

- `main.py`: CLI entry point and orchestration using Clean Architecture services.
- `src/`: Core logic.
    - `models.py`: Pydantic definitions for Problems and EvaluationResults.
    - `prompts.py`: Prompt templates (Comprehension, Planning, Implementation, Zero-Shot).
    - `evaluator.py`: Logic for parallel code execution and OBI-style judging.
- `test_cases/`: Input (`.in`) and expected solution (`.sol`) files.
- `problems.json`: Dataset containing problem statements, constraints, and base examples.
