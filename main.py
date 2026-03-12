import json
import os
import pandas as pd
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
from models import Problem, EvaluationResult
from prompts import POLYA_PROMPT_TEMPLATE

# Load environment variables from .env file
load_dotenv()

def load_problems(file_path: str) -> List[Problem]:
    with open(file_path, 'r') as f:
        data = json.load(f)
    return [Problem(**p) for p in data]

def get_llm_response(client: OpenAI, model: str, prompt: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    return response.choices[0].message.content

def split_response(response: str):
    # Basic split based on likely headers. A more robust parser might be needed.
    understanding = ""
    plan = ""
    
    if "Understanding" in response and "Plan" in response:
        parts = response.split("Plan", 1)
        understanding = parts[0].replace("Understanding", "").strip("# ").strip()
        plan = parts[1].strip("# ").strip()
    else:
        # Fallback if headers are not found
        understanding = response
        plan = "Failed to parse plan from response."
        
    return understanding, plan

def main():
    api_key = os.getenv("OPENAI_API_KEY", "sk-no-key-required")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    model_name = os.getenv("MODEL_NAME", "gpt-4o")
    
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    problems = load_problems("problems.json")
    results = []

    for problem in problems:
        print(f"Processing problem: {problem.title} (ID: {problem.id})...")
        
        examples_text = "\n".join([f"Input: {e.input}\nOutput: {e.output}" for e in problem.examples])
        
        prompt = POLYA_PROMPT_TEMPLATE.format(
            title=problem.title,
            statement=problem.statement,
            input_description=problem.input,
            output_description=problem.output,
            constraints=problem.constraints,
            examples_text=examples_text
        )
        
        response_text = get_llm_response(client, model_name, prompt)
        understanding, plan = split_response(response_text)
        
        results.append(EvaluationResult(
            question_id=problem.id,
            model=model_name,
            understanding_text=understanding,
            plan_text=plan
        ))

    # Save to CSV
    df = pd.DataFrame([r.model_dump() for r in results])
    df.to_csv("results.csv", index=False)
    print("Evaluation complete. Results saved to results.csv")

if __name__ == "__main__":
    main()
