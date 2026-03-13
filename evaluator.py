import json
import urllib.request
import urllib.error
import time
from models import Problem

PISTON_URL = "http://localhost:2000/api/v2/execute"

def execute_piston(code: str, stdin: str) -> dict:
    """Executes code using a local Piston instance."""
    payload = {
        "language": "python",
        "version": "3.10.0",
        "files": [{"content": code}],
        "stdin": stdin
    }
    
    req = urllib.request.Request(
        PISTON_URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        start_time = time.time()
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            result['execution_time'] = time.time() - start_time
            return result
    except urllib.error.URLError as e:
        print(f"Warning: Failed to connect to Piston API at {PISTON_URL}. Ensure it is running. Error: {e}")
        return {"run": {"stdout": "", "stderr": str(e), "code": 1}, "execution_time": 0.0}

def evaluate_code(code: str, test_cases: list[tuple[str, str]]) -> tuple[bool, int, str, str]:
    """
    Evaluates the python code against the provided test cases.
    Each test case is a tuple (input, output).
    Returns: (judge_correctness, judge_test_cases, judge_time_complexity, judge_space_complexity)
    """
    if not code.strip():
        return False, 0, "Fail", "Fail"
        
    test_cases_passed = 0
    total_cases = len(test_cases)
    
    # We will track execution time to estimate time complexity
    max_execution_time = 0.0
    
    for input_str, expected_output in test_cases:
        result = execute_piston(code, input_str)
        
        run_data = result.get("run", {})
        stdout = run_data.get("stdout", "").strip()
        expected = expected_output.strip()
        
        # execution time in seconds
        exec_time = result.get("execution_time", 0.0)
        max_execution_time = max(max_execution_time, exec_time)
        
        if stdout == expected and run_data.get("code") == 0:
            test_cases_passed += 1
            
    judge_correctness = (test_cases_passed == total_cases) and total_cases > 0
    
    # Simple heuristics for time and space complexity based on pure execution
    # Ideally, we would need actual memory limits and execution time limits per problem.
    judge_time_complexity = "Pass" if max_execution_time < 2.0 else "Fail"
    judge_space_complexity = "Pass" # Piston API does not easily expose peak memory without a custom engine
    
    return judge_correctness, test_cases_passed, judge_time_complexity, judge_space_complexity
