import json
import os
import re
import glob
import pandas as pd
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
from models import Problem, EvaluationResult
from prompts import COMPREHENSION_PROMPT_TEMPLATE, PLANNING_PROMPT_TEMPLATE, IMPLEMENTATION_PROMPT_TEMPLATE
from evaluator import evaluate_code

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

def extract_code(response_text: str) -> str:
    """Extracts python code from markdown block."""
    match = re.search(r'```python\n(.*?)\n```', response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Fallback: check generic code block
    match = re.search(r'```\n(.*?)\n```', response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
        
    return response_text.strip()

def get_test_cases(problem_id: str, default_examples: List) -> List[tuple[str, str]]:
    """Discovers test cases in the test_cases directory."""
    test_cases = []
    problem_path = os.path.join("test_cases", problem_id)
    
    if os.path.exists(problem_path):
        in_files = glob.glob(os.path.join(problem_path, "**", "*.in"), recursive=True)
        for in_file in in_files:
            sol_file = in_file.replace(".in", ".sol")
            if os.path.exists(sol_file):
                with open(in_file, 'r') as f:
                    in_content = f.read()
                with open(sol_file, 'r') as f:
                    sol_content = f.read()
                test_cases.append((in_content, sol_content))
    
    if not test_cases:
        test_cases = [(e.input, e.output) for e in default_examples]
    
    return test_cases

def main():
    api_key = os.getenv("OPENAI_API_KEY", "sk-no-key-required")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    model_name = os.getenv("MODEL_NAME", "gpt-4o")
    
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    problems = load_problems("problems.json")
    results = []

    for problem in problems:
        print(f"Processing problem: {problem.title} (ID: {problem.id})...")
        
        # Step 1: Comprehension
        contexto = f"Problema: \"{problem.title}\". {problem.statement}\nEntrada: {problem.input}\nSaída: {problem.output}\nRestrições: {problem.constraints}"
        comp_prompt = COMPREHENSION_PROMPT_TEMPLATE.format(contexto=contexto)
        understanding = get_llm_response(client, model_name, comp_prompt)
        
        # Step 2: Planning
        plan_prompt = PLANNING_PROMPT_TEMPLATE.format(
            linguagem="Python",
            output_agente_compreensao=understanding
        )
        plan = get_llm_response(client, model_name, plan_prompt)
        
        # Step 3: Implementation
        impl_prompt = IMPLEMENTATION_PROMPT_TEMPLATE.format(
            linguagem="Python",
            output_agente_planejador=plan
        )
        
        code_response = get_llm_response(client, model_name, impl_prompt)
        code_text = extract_code(code_response)
        
        # Step 4: Evaluation
        test_cases = get_test_cases(problem.id, problem.examples)
        print(f"Found {len(test_cases)} test cases for {problem.id}")
        
        judge_correctness, judge_test_cases, judge_time_complexity, judge_space_complexity = evaluate_code(code_text, test_cases)
        
        results.append(EvaluationResult(
            question_id=problem.id,
            model=model_name,
            understanding_text=understanding,
            plan_text=plan,
            code_text=code_text,
            judge_correctness=judge_correctness,
            judge_test_cases=judge_test_cases,
            judge_time_complexity=judge_time_complexity,
            judge_space_complexity=judge_space_complexity
        ))

    # Save to CSV
    df = pd.DataFrame([r.model_dump() for r in results])
    df.to_csv("results.csv", index=False)
    print("Evaluation complete. Results saved to results.csv")

if __name__ == "__main__":
    main()
