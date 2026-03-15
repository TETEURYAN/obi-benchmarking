import json
import os
import re
import glob
import argparse
import pandas as pd
from datetime import datetime
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
from src.models import Problem, EvaluationResult
from src.prompts import COMPREHENSION_PROMPT_TEMPLATE, PLANNING_PROMPT_TEMPLATE, IMPLEMENTATION_PROMPT_TEMPLATE, ZERO_SHOT_PROMPT_TEMPLATE
from src.evaluator import evaluate_code

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
    parser = argparse.ArgumentParser(description="Evaluate LLMs on OBI problems.")
    parser.add_argument("--zero-shot", action="store_true", help="Run with a single zero-shot prompt instead of multi-agent mode.")
    parser.add_argument("--models-file", type=str, help="Path to a .txt file with one model name per line.")
    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY", "sk-no-key-required")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    
    # Determine models to run
    if args.models_file and os.path.exists(args.models_file):
        with open(args.models_file, 'r') as f:
            model_names = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    else:
        model_names = [os.getenv("MODEL_NAME", "gpt-4o")]
    
    client = OpenAI(api_key=api_key, base_url=base_url)
    problems = load_problems("problems.json")
    
    all_summaries = []
    run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for model_name in model_names:
        print(f"\n" + "="*50)
        print(f"Starting evaluation for model: {model_name}")
        print("="*50 + "\n")
        
        results = []
        for problem in problems:
            print(f"Processing problem: {problem.title} (ID: {problem.id})...")
            
            contexto = f"Problema: \"{problem.title}\". {problem.statement}\nEntrada: {problem.input}\nSaída: {problem.output}\nRestrições: {problem.constraints}"
            
            if args.zero_shot:
                print("Running in zero-shot mode...")
                zero_shot_prompt = ZERO_SHOT_PROMPT_TEMPLATE.format(contexto=contexto)
                code_response = get_llm_response(client, model_name, zero_shot_prompt)
                code_text = extract_code(code_response)
                understanding = "N/A (Zero-shot)"
                plan = "N/A (Zero-shot)"
            else:
                # Step 1: Comprehension
                comp_prompt = COMPREHENSION_PROMPT_TEMPLATE.format(contexto=contexto)
                understanding = get_llm_response(client, model_name, comp_prompt)
                
                # Step 2: Planning
                plan_prompt = PLANNING_PROMPT_TEMPLATE.format(
                    linguagem="python",
                    output_agente_compreensao=understanding,
                    contexto=contexto
                )
                plan = get_llm_response(client, model_name, plan_prompt)
                
                # Step 3: Implementation
                impl_prompt = IMPLEMENTATION_PROMPT_TEMPLATE.format(
                    linguagem="python",
                    output_agente_planejador=plan,
                    contexto=contexto
                )
                
                code_response = get_llm_response(client, model_name, impl_prompt)
                code_text = extract_code(code_response)
            
            # Step 4: Evaluation
            test_cases = get_test_cases(problem.id, problem.examples)
            print(f"Found {len(test_cases)} test cases for {problem.id}")
            
            # Unpack evaluate_code result (now returns failures list as fourth element)
            judge_correctness, judge_test_cases, total_test_cases, failures = evaluate_code(code_text, test_cases)

            results.append(EvaluationResult(
                question_id=problem.id,
                model=model_name,
                understanding_text=understanding,
                plan_text=plan,
                code_text=code_text,
                judge_correctness=judge_correctness,
                judge_test_cases=judge_test_cases,
                total_test_cases=total_test_cases
                ,failures=failures
            ))

        # Save to CSV in structured format
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        shot_status = "zeroshot" if args.zero_shot else "agents"
        results_dir = os.path.join("resultados", model_name)
        os.makedirs(results_dir, exist_ok=True)
        
        model_name_safe = model_name.replace("/", "_")
        file_name = f"results_{model_name_safe}_{timestamp}_{shot_status}.csv"
        output_path = os.path.join(results_dir, file_name)
        
        df = pd.DataFrame([r.model_dump() for r in results])
        df.to_csv(output_path, index=False)
        print(f"Evaluation complete for {model_name}. Results saved to {output_path}")

        # Accumulate summary metrics
        total_problems = len(results)
        problems_passed = sum(1 for r in results if r.judge_correctness)
        total_cases = sum(r.total_test_cases for r in results)
        cases_passed = sum(r.judge_test_cases for r in results)
        success_rate_problems = problems_passed / total_problems if total_problems > 0 else 0
        success_rate_cases = cases_passed / total_cases if total_cases > 0 else 0

        all_summaries.append({
            "model": model_name,
            "shot_status": shot_status,
            "total_problems": total_problems,
            "problems_passed": problems_passed,
            "success_rate_problems": success_rate_problems,
            "total_cases": total_cases,
            "cases_passed": cases_passed,
            "success_rate_cases": success_rate_cases,
            "timestamp": timestamp
        })

    # Save summary results CSV
    if all_summaries:
        shot_status = "zeroshot" if args.zero_shot else "agents"
        summary_file_name = f"summary_results_{run_timestamp}_{shot_status}.csv"
        summary_path = os.path.join("resultados", summary_file_name)
        
        df_summary = pd.DataFrame(all_summaries)
        df_summary.to_csv(summary_path, index=False)
        print(f"\nAll evaluations complete. Summary saved to {summary_path}")

if __name__ == "__main__":
    main()
