import json
import os
import re
import glob
import argparse
import pandas as pd
from datetime import datetime
from typing import List, Tuple, Dict, Any, Optional
from abc import ABC, abstractmethod
from openai import OpenAI
from dotenv import load_dotenv
from src.models import Problem, EvaluationResult
from src.prompts import (
    COMPREHENSION_PROMPT_TEMPLATE, 
    PLANNING_PROMPT_TEMPLATE, 
    IMPLEMENTATION_PROMPT_TEMPLATE, 
    ZERO_SHOT_PROMPT_TEMPLATE
)
from src.evaluator import evaluate_code

class ProblemRepository:
    """
    Handles the persistence and retrieval of problem definitions.
    """
    def __init__(self, file_path: str):
        """
        Initializes the repository with a path to the problems JSON file.
        """
        self.file_path = file_path

    def load_all(self) -> List[Problem]:
        """
        Loads all problems from the JSON file and returns a list of Problem objects.
        """
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Problem(**p) for p in data]


class TestCaseProvider:
    """
    Handles the discovery and loading of test cases for OBI problems.
    """
    def get_test_cases(self, problem_id: str, default_examples: List) -> List[Tuple[str, str]]:
        """
        Discovers test cases in the 'test_cases' directory or falls back to default examples.
        
        Args:
            problem_id: The unique identifier of the problem.
            default_examples: A list of default input/output examples from the problem statement.
            
        Returns:
            A list of tuples containing (input_string, expected_output_string).
        """
        test_cases = []
        problem_path = os.path.join("test_cases", problem_id)
        
        if os.path.exists(problem_path):
            in_files = glob.glob(os.path.join(problem_path, "**", "*.in"), recursive=True)
            for in_file in in_files:
                sol_file = in_file.replace(".in", ".sol")
                if os.path.exists(sol_file):
                    with open(in_file, 'r', encoding='utf-8') as f:
                        in_content = f.read()
                    with open(sol_file, 'r', encoding='utf-8') as f:
                        sol_content = f.read()
                    test_cases.append((in_content, sol_content))
        
        if not test_cases:
            test_cases = [(e.input, e.output) for e in default_examples]
        
        return test_cases


class ResultRepository:
    """
    Handles the storage of evaluation results and summary metrics in CSV format.
    """
    def __init__(self, base_dir: str = "resultados"):
        """
        Initializes the repository with a base directory for storing results.
        """
        self.base_dir = base_dir

    def save_model_results(self, model_name: str, results: List[EvaluationResult], shot_status: str, timestamp: str) -> str:
        """
        Saves individual model execution results to a CSV file.
        
        Returns:
            The absolute path to the saved CSV file.
        """
        results_dir = os.path.join(self.base_dir, model_name)
        os.makedirs(results_dir, exist_ok=True)
        
        model_name_safe = model_name.replace("/", "_")
        file_name = f"results_{model_name_safe}_{timestamp}_{shot_status}.csv"
        output_path = os.path.join(results_dir, file_name)
        
        df = pd.DataFrame([r.model_dump() for r in results])
        df.to_csv(output_path, index=False)
        return output_path

    def save_summary(self, summaries: List[Dict[str, Any]], shot_status: str, timestamp: str) -> str:
        """
        Saves the aggregated performance summary of multiple models to a CSV file.
        
        Returns:
            The absolute path to the saved summary CSV file.
        """
        summary_file_name = f"summary_results_{timestamp}_{shot_status}.csv"
        summary_path = os.path.join(self.base_dir, summary_file_name)
        
        df_summary = pd.DataFrame(summaries)
        df_summary.to_csv(summary_path, index=False)
        return summary_path

    def find_result_files(self) -> List[str]:
        """
        Crawls the results directory to find all CSV files starting with 'results_'.
        """
        return glob.glob(os.path.join(self.base_dir, "**", "results_*.csv"), recursive=True)



class LLMClientAdapter:
    """
    Adapter for interacting with the OpenAI-compatible LLM APIs.
    """
    def __init__(self, api_key: str, base_url: str):
        """
        Initializes the adapter with API credentials and base URL.
        """
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def get_response(self, model: str, prompt: str) -> str:
        """
        Sends a single prompt to the specified model and returns the response content.
        """
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        return response.choices[0].message.content


class CodeExtractor:
    """
    Utility class to extract code snippets from LLM responses.
    """
    @staticmethod
    def extract(response_text: str) -> str:
        """
        Extracts python code from markdown blocks (```python ... ``` or ``` ... ```).
        If no blocks are found, returns the original text stripped of whitespace.
        """
        match = re.search(r'```python\n(.*?)\n```', response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        # Fallback: check generic code block
        match = re.search(r'```\n(.*?)\n```', response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
            
        return response_text.strip()



class EvaluationStrategy(ABC):
    """
    Abstract base class for different evaluation methodologies (e.g., Zero-shot, Multi-agent).
    """
    @abstractmethod
    def evaluate(self, client: LLMClientAdapter, model: str, problem: Problem) -> Tuple[str, str, str]:
        """
        Executes the evaluation logic for a single problem.
        
        Returns:
            A tuple of (understanding_text, plan_text, code_text).
        """
        raise NotImplementedError

    def _get_context(self, problem: Problem) -> str:
        """
        Formats the problem statement and constraints into a context string for prompts.
        """
        return (f"Problema: \"{problem.title}\". {problem.statement}\n"
                f"Entrada: {problem.input}\n"
                f"Saída: {problem.output}\n"
                f"Restrições: {problem.constraints}")


class ZeroShotStrategy(EvaluationStrategy):
    """
    Strategy that uses a single Zero-shot prompt to generate code directly.
    """
    def evaluate(self, client: LLMClientAdapter, model: str, problem: Problem) -> Tuple[str, str, str]:
        """
        Sends a single prompt to the LLM and extracts the generated code.
        """
        contexto = self._get_context(problem)
        zero_shot_prompt = ZERO_SHOT_PROMPT_TEMPLATE.format(contexto=contexto)
        code_response = client.get_response(model, zero_shot_prompt)
        code_text = CodeExtractor.extract(code_response)
        return "N/A (Zero-shot)", "N/A (Zero-shot)", code_text


class MultiAgentStrategy(EvaluationStrategy):
    """
    Strategy that breaks down problem solving into Comprehension, Planning, and Implementation phases.
    """
    def evaluate(self, client: LLMClientAdapter, model: str, problem: Problem) -> Tuple[str, str, str]:
        """
        Executes a three-step pipeline to generate code.
        """
        contexto = self._get_context(problem)
        
        # Step 1: Comprehension
        comp_prompt = COMPREHENSION_PROMPT_TEMPLATE.format(contexto=contexto)
        understanding = client.get_response(model, comp_prompt)
        
        # Step 2: Planning
        plan_prompt = PLANNING_PROMPT_TEMPLATE.format(
            linguagem="python",
            output_agente_compreensao=understanding,
            contexto=contexto
        )
        plan = client.get_response(model, plan_prompt)
        
        # Step 3: Implementation
        impl_prompt = IMPLEMENTATION_PROMPT_TEMPLATE.format(
            linguagem="python",
            output_agente_planejador=plan,
            contexto=contexto
        )
        
        code_response = client.get_response(model, impl_prompt)
        code_text = CodeExtractor.extract(code_response)
        
        return understanding, plan, code_text



class EvaluationService:
    """
    Application service that orchestrates the overall evaluation flow for multiple models and problems.
    """
    def __init__(self, 
                 client: LLMClientAdapter, 
                 problem_repo: ProblemRepository, 
                 result_repo: ResultRepository,
                 test_case_provider: TestCaseProvider):
        """
        Initializes the service with necessary adapters and repositories (Dependency Injection).
        """
        self.client = client
        self.problem_repo = problem_repo
        self.result_repo = result_repo
        self.test_case_provider = test_case_provider

    def run_evaluation(self, model_names: List[str], strategy: EvaluationStrategy, shot_status: str):
        """
        Main loop to evaluate listed models against all available problems using the chosen strategy.
        """
        problems = self.problem_repo.load_all()
        run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        all_summaries = []

        for model_name in model_names:
            print(f"\n{'='*50}\nStarting evaluation for model: {model_name}\n{'='*50}\n")
            
            results = []
            for problem in problems:
                print(f"Processing problem: {problem.title} (ID: {problem.id})...")
                
                understanding, plan, code_text = strategy.evaluate(self.client, model_name, problem)
                
                test_cases = self.test_case_provider.get_test_cases(problem.id, problem.examples)
                print(f"Found {len(test_cases)} test cases for {problem.id}")
                
                correctness, passed, total, failures, classification = evaluate_code(code_text, test_cases)

                results.append(EvaluationResult(
                    question_id=problem.id,
                    model=model_name,
                    understanding_text=understanding,
                    plan_text=plan,
                    code_text=code_text,
                    judge_correctness=correctness,
                    judge_test_cases=passed,
                    total_test_cases=total,
                    failures=failures,
                    classification=classification
                ))

            output_path = self.result_repo.save_model_results(model_name, results, shot_status, run_timestamp)
            print(f"Evaluation complete for {model_name}. Results saved to {output_path}")

            all_summaries.append(self._calculate_summary(model_name, shot_status, results, run_timestamp))

        if all_summaries:
            summary_path = self.result_repo.save_summary(all_summaries, shot_status, run_timestamp)
            print(f"\nAll evaluations complete. Summary saved to {summary_path}")

    def _calculate_summary(self, model_name: str, shot_status: str, results: List[EvaluationResult], timestamp: str) -> Dict[str, Any]:
        """
        Helper method to aggregate metrics for a specific model evaluation run.
        """
        total_problems = len(results)
        problems_passed = sum(1 for r in results if r.judge_correctness)
        total_cases = sum(r.total_test_cases for r in results)
        cases_passed = sum(r.judge_test_cases for r in results)
        
        return {
            "model": model_name,
            "shot_status": shot_status,
            "total_problems": total_problems,
            "problems_passed": problems_passed,
            "success_rate_problems": problems_passed / total_problems if total_problems > 0 else 0,
            "total_cases": total_cases,
            "cases_passed": cases_passed,
            "success_rate_cases": cases_passed / total_cases if total_cases > 0 else 0,
            "timestamp": timestamp
        }


class ReEvaluationService:
    """
    Application service specialized in re-running evaluations for existing results in CSV files.
    """
    def __init__(self, problem_repo: ProblemRepository, result_repo: ResultRepository, test_case_provider: TestCaseProvider):
        """
        Initializes the service with necessary repositories.
        """
        self.problem_repo = problem_repo
        self.result_repo = result_repo
        self.test_case_provider = test_case_provider

    def re_evaluate_all(self):
        """
        Iterates over all result files and re-runs the judge against original code snippets.
        """
        print("Re-evaluating existing results...")
        problems = {p.id: p for p in self.problem_repo.load_all()}
        result_files = self.result_repo.find_result_files()
        
        for file_path in result_files:
            print(f"Processing {file_path}...")
            df = pd.read_csv(file_path)
            if df.empty:
                continue
                
            new_rows = []
            for _, row in df.iterrows():
                p_id = row['question_id']
                code = str(row['code_text'])
                
                if p_id in problems:
                    problem = problems[p_id]
                    test_cases = self.test_case_provider.get_test_cases(problem.id, problem.examples)
                    
                    print(f"  Re-evaluating {p_id} ({len(test_cases)} cases)...")
                    correctness, passed, total, failures, classification = evaluate_code(code, test_cases)
                    
                    row['judge_correctness'] = correctness
                    row['judge_test_cases'] = passed
                    row['total_test_cases'] = total
                    row['failures'] = json.dumps(failures)
                    row['classification'] = classification
                else:
                    print(f"  Warning: Problem ID {p_id} not found in repository")
                
                new_rows.append(row)
            
            pd.DataFrame(new_rows).to_csv(file_path, index=False)
            print(f"Finished updating {file_path}")
            
        print("\nRe-evaluation complete.")


# --- Main Application ---

def load_models_from_file(file_path: str) -> List[str]:
    """
    Loads model names from a text file, ignoring empty lines and comments.
    """
    if not os.path.exists(file_path):
        return [os.getenv("MODEL_NAME", "gpt-4o")]
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


def main():
    """
    Main entry point for the CLI application.
    Orchestrates dependency injection and initializes the appropriate service based on user input.
    """
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="Evaluate LLMs on OBI problems.")
    parser.add_argument("--zero-shot", action="store_true", help="Run with a single zero-shot prompt.")
    parser.add_argument("--models-file", type=str, help="Path to a .txt file with model names.")
    parser.add_argument("--re-evaluate-results", action="store_true", help="Re-evaluate already generated code.")
    args = parser.parse_args()

    problem_repo = ProblemRepository("problems.json")
    result_repo = ResultRepository()
    test_case_provider = TestCaseProvider()
    
    if args.re_evaluate_results:
        reeval_service = ReEvaluationService(problem_repo, result_repo, test_case_provider)
        reeval_service.re_evaluate_all()
        return

    api_key = os.getenv("OPENAI_API_KEY", "sk-no-key-required")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    client = LLMClientAdapter(api_key, base_url)
    
    # Strategy Selection
    strategy = ZeroShotStrategy() if args.zero_shot else MultiAgentStrategy()
    shot_status = "zeroshot" if args.zero_shot else "agents"
    
    # Model Loading
    model_names = load_models_from_file(args.models_file) if args.models_file else [os.getenv("MODEL_NAME", "gpt-4o")]
    
    # Execution
    eval_service = EvaluationService(client, problem_repo, result_repo, test_case_provider)
    eval_service.run_evaluation(model_names, strategy, shot_status)


if __name__ == "__main__":
    main()
