import json
import time
import subprocess
import tempfile
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from models import Problem

def execute_local(code: str, stdin: str, timeout: float = 2.0) -> dict:
    """Executes C++ code locally using a subprocess."""
    # We use a unique temporary file per execution to avoid collisions in parallel runs
    fd, temp_file_path = tempfile.mkstemp(suffix='.cpp', text=True)
    with os.fdopen(fd, 'w') as f:
        f.write(code)
    
    exe_path = temp_file_path.replace('.cpp', '.out')
    
    try:
        # Compile the C++ code
        compile_process = subprocess.run(
            ['g++', temp_file_path, '-o', exe_path],
            capture_output=True,
            text=True,
            timeout=10.0  # Compilation timeout
        )
        
        if compile_process.returncode != 0:
            return {
                "run": {
                    "stdout": "",
                    "stderr": f"Compilation error: {compile_process.stderr}",
                    "code": compile_process.returncode
                },
                "execution_time": 0.0
            }
        
        # Execute the compiled binary
        start_time = time.time()
        process = subprocess.run(
            [exe_path],
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
        if os.path.exists(exe_path):
            os.remove(exe_path)

def evaluate_code(code: str, test_cases: list[tuple[str, str]]) -> tuple[bool, int, int]:
    """
    Evaluates the C++ code against the provided test cases in parallel.
    Each test case is a tuple (input, output).
    Returns: (judge_correctness, test_cases_passed, total_cases)
    """
    
    
    if (code[0] == '`'):
        code = code[6: len(code) - 3]
    
    if not code.strip():
        return False, 0, len(test_cases)
        
    total_cases = len(test_cases)
    test_cases_passed = 0
    
    print(f"Starting evaluation of {total_cases} test cases...")
    
    def run_case(case_idx, input_str, expected_output):
        result = execute_local(code, input_str)
        run_data = result.get("run", {})
        stdout = run_data.get("stdout", "").strip()
        expected = expected_output.strip()
        passed = (stdout == expected and run_data.get("code") == 0)
        return passed

    # Use ThreadPoolExecutor for parallel execution
    # Using more workers than CPU cores since it's mostly waiting for subprocesses
    max_workers = min(32, (os.cpu_count() or 1) * 4)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(run_case, i, inp, out) 
            for i, (inp, out) in enumerate(test_cases)
        ]
        
        for i, future in enumerate(futures):
            if future.result():
                test_cases_passed += 1
            
            # Progress logging every 10% or every 10 cases
            if (i + 1) % max(1, total_cases // 10) == 0 or (i + 1) == total_cases:
                print(f"Progress: {i+1}/{total_cases} cases evaluated...")

    judge_correctness = (test_cases_passed == total_cases) and total_cases > 0
    print(f"Evaluation complete: {test_cases_passed}/{total_cases} passed.")
    
    return judge_correctness, test_cases_passed, total_cases
