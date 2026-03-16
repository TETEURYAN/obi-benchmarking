# Polya Evaluation Script

This script evaluates LLM models based on the first two steps of Polya's method: Understanding and Planning.

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
   # Edit .env with your actual values
   ```
   Or set them in your environment:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   export OPENAI_BASE_URL='https://api.openai.com/v1' # Optional: for OpenAI-compatible APIs
   export MODEL_NAME='gpt-4o' # Optional: name of the model to use
   ```

## Usage

1. Add problems to `problems.json` following the specified format.
2. Run the script:
   ```bash
   uv run main.py
   ```
3. Check the results in `results.csv`.

## Files

- `main.py`: The execution script.
- `models.py`: Pydantic data models.
- `prompts.py`: Polya's method prompt template.
- `problems.json`: Dataset of problems to solve.
- `results.csv`: Generated output from the LLM.
