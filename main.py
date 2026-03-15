import json
import os
import pandas as pd
from models.evaluation_result import EvaluationResult
from models.problem import Problem
from prompts import ZERO_SHOT_PROMPT_TEMPLATE, FEW_SHOT_PROMPT_TEMPLATE
from pathlib import Path


def load_problem(file_path: Path) -> Problem:
    data = json.loads(file_path.read_text(encoding="utf-8"))
    
    return Problem(**data)

def print_partition(text: str):
    print("="*70)
    print("text")
    print("="*70)

def main():
    
    try:
        print_partition("CRIANDO DATABASE")
        
        path_database = Path("database")
        questions_path = []
        
        for folder in path_database.glob("*/*/*/*/"):
            if folder.is_dir():
                questions_path.append(folder)
        
        problem_names = []            
        for path in questions_path:
            problem_names.append(path.name)
        
        problems = []
        for question_path in questions_path:
            problems.append(load_problem(Path(question_path / "problem.json")))
        
        print_partition("FIM DA CRIANÇÃO DATABASE")
        
    except Exception:    
        print("Erro na estrutura database. Verifique o diretorio!")
        exit(1)
    
    zero_shot_prompt = ZERO_SHOT_PROMPT_TEMPLATE.format(contexto=contexto)
    
    results = []
    total = 0
    total_acc = 0
    
    for problem in problems:
        print(f"Processing problem: {problem.title} (ID: {problem.id})...")
        
        contexto = f"Problema: \"{problem.title}\". {problem.statement}\nEntrada: {problem.input}\nSaída: {problem.output}\nRestrições: {problem.constraints}"
        
        if args.zero_shot:
            print("Running in zero-shot mode...")
            
            code_response = get_llm_response(client, model_name, zero_shot_prompt)
            code_text = extract_code(code_response)
            understanding = "N/A (Zero-shot)"
            plan = "N/A (Zero-shot)"
            
            if (code_text[0] == '`'):
                code_text = code_text[6: len(code_text) - 3]
                
            create_file(name = f"{problem.title}.cpp",
                    path = f"code_llm/zero-shot/{os.getenv("MODEL_NAME", "test")}",
                    content=code_text)
            
        else:
            # Step 1: Comprehension
            comp_prompt = COMPREHENSION_PROMPT_TEMPLATE.format(contexto=contexto)
            understanding = get_llm_response(client, model_name, comp_prompt)
            
            # Step 2: Planning
            plan_prompt = PLANNING_PROMPT_TEMPLATE.format(
                linguagem="C++",
                output_agente_compreensao=understanding,
                contexto=contexto
            )
            plan = get_llm_response(client, model_name, plan_prompt)
            
            # Step 3: Implementation
            impl_prompt = IMPLEMENTATION_PROMPT_TEMPLATE.format(
                linguagem="C++",
                output_agente_planejador=plan,
                contexto=contexto
            )
            
            code_response = get_llm_response(client, model_name, impl_prompt)
            code_text = extract_code(code_response)
            
            if (code_text[0] == '`'):
                code_text = code_text[6: len(code_text) - 3]
            
            create_file(name = f"{problem.title}.cpp",
                    path = f"code_llm/multiagentes/{os.getenv("MODEL_NAME", "test")}",
                    content=code_text)
        
        # Step 4: Evaluation
        test_cases = get_test_cases(problem.id, problem.examples)
        print(f"Found {len(test_cases)} test cases for {problem.id}")
        
        judge_correctness, judge_test_cases, total_test_cases = evaluate_code(code_text, test_cases)
        
        total += total_test_cases
        total_acc += judge_test_cases
        
        
        
        results.append(EvaluationResult(
            question_id=problem.id,
            model=model_name,
            understanding_text=understanding,
            plan_text=plan,
            code_text=code_text,
            judge_correctness=judge_correctness,
            judge_test_cases=judge_test_cases,
            total_test_cases=total_test_cases
        ))

    # Save to CSV
    df = pd.DataFrame([r.model_dump() for r in results])
    df.to_csv("results.csv", index=False)
    print("Evaluation complete. Results saved to results.csv")
    print(f"{total_acc}/{total}")

if __name__ == "__main__":
    main()
