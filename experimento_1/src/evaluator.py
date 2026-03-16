import json
import time
import subprocess
import tempfile
import os
import sys
from concurrent.futures import ThreadPoolExecutor
# from models import Problem

def execute_local(code: str, stdin: str, timeout: float = 2.0) -> dict:
    """Executes code locally using a subprocess."""
    # We use a unique temporary file per execution to avoid collisions in parallel runs
    fd, temp_file_path = tempfile.mkstemp(suffix='.py', text=True)
    with os.fdopen(fd, 'w') as f:
        f.write(code)
        
    try:
        start_time = time.time()
        process = subprocess.run(
            [sys.executable, temp_file_path],
            input=stdin,
            text=True,
            capture_output=True,
            timeout=timeout
        )
        execution_time = time.time() - start_time
        
        return {
            "run": {
                "stdout": process.stdout,
                "stderr": process.stderr,
                "code": process.returncode
            },
            "execution_time": execution_time
        }
    except subprocess.TimeoutExpired as e:
        return {
            "run": {
                "stdout": e.stdout.decode() if e.stdout else "",
                "stderr": "Execution timed out.",
                "code": 124
            },
            "execution_time": timeout
        }
    except Exception as e:
        return {
            "run": {
                "stdout": "",
                "stderr": str(e),
                "code": 1
            },
            "execution_time": 0.0
        }
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

def evaluate_code(code: str, test_cases: list[tuple[str, str]]) -> tuple[bool, int, int, list, str]:
    """
    Evaluates the python code against the provided test cases in parallel.
    Each test case is a tuple (input, output).
    Returns: (judge_correctness, test_cases_passed, total_cases, failures_list, classification)
    """
    if not code.strip():
        return False, 0, len(test_cases), [], "CE"
    
    # print("code:", code )
    total_cases = len(test_cases)
    test_cases_passed = 0
    failures: list[str] = []
    
    print(f"Starting evaluation of {total_cases} test cases...")
    
    def run_case(case_idx, input_str, expected_output):
        result = execute_local(code, input_str)
        run_data = result.get("run", {})
        stdout = run_data.get("stdout", "").strip()
        expected = expected_output.strip()
        retcode = run_data.get("code")
        stderr = run_data.get("stderr", "")
        
        passed = (stdout == expected and retcode == 0)
        classification = "AC"
        msg = None
        
        if not passed:
            if retcode == 124:
                classification = "TLE"
            elif "SyntaxError" in stderr or "IndentationError" in stderr:
                classification = "CE"
            elif retcode != 0:
                classification = "RE"
            else:
                classification = "WA"
            
            msg = f"Case {case_idx}: expected: {repr(expected)} got: {repr(stdout)} retcode: {retcode} stderr: {stderr}"
        return passed, msg, classification

    # Use ThreadPoolExecutor for parallel execution
    max_workers = min(32, (os.cpu_count() or 1) * 4)
    
    final_classification = "AC"
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(run_case, i, inp, out) 
            for i, (inp, out) in enumerate(test_cases)
        ]
        
        for i, future in enumerate(futures):
            passed, msg, classification = future.result()
            if passed:
                test_cases_passed += 1
            else:
                if final_classification == "AC":
                    final_classification = classification
                if msg:
                    failures.append(msg[-100:])
                    print(msg[-100:])
            
            # Progress logging every 10% or every 10 cases
            if (i + 1) % max(1, total_cases // 10) == 0 or (i + 1) == total_cases:
                print(f"Progress: {i+1}/{total_cases} cases evaluated...")

    judge_correctness = (test_cases_passed == total_cases) and total_cases > 0
    print(f"Evaluation complete: {test_cases_passed}/{total_cases} passed. Result: {final_classification}")
    
    return judge_correctness, test_cases_passed, total_cases, failures, final_classification
