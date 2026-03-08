import os
import httpx
import logging
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Judge:
    def __init__(self, base_url: str = None):
        # Default Piston endpoint (local or hosted)
        self.base_url = base_url or os.getenv("PISTON_BASE_URL", "http://localhost:2000")
        self.client = httpx.Client(base_url=self.base_url, timeout=30.0)
        logger.info(f"Initializing Judge with Piston endpoint: {self.base_url}")

    def evaluate(self, code: str, language: str, test_cases: List[Dict], version: str = "*", run_timeout: int = 3000, run_memory_limit: int = -1) -> List[Dict]:
        """
        Evaluate code against multiple test cases using Piston.
        run_timeout: max wall-time in milliseconds (default 3000).
        run_memory_limit: max memory in bytes (default -1, no limit).
        """
        results = []
        logger.info(f"Evaluating code (lang={language}) with {len(test_cases)} test cases.")

        for i, tc in enumerate(test_cases):
            try:
                payload = {
                    "language": language,
                    "version": version,
                    "files": [{"content": code}],
                    "stdin": tc.get("input", ""),
                    "run_timeout": run_timeout,
                    "run_memory_limit": run_memory_limit
                }
                
                response = self.client.post("/api/v2/execute", json=payload)
                response.raise_for_status()
                data = response.json()
                
                run_result = data.get("run", {})
                status_code = run_result.get("code")
                status_msg = run_result.get("status") # e.g., 'RE', 'TO', 'SG'
                stdout = run_result.get("stdout", "")
                expected = tc.get("expected_output", "")
                
                status = "Accepted" if status_code == 0 else "Runtime Error"
                if status_msg == "TO":
                    status = "Time Limit Exceeded"
                elif status_msg == "RE":
                    status = "Runtime Error"
                elif status_msg == "SG":
                    status = f"Terminated ({run_result.get('signal')})"
                
                # Compare output if the code ran successfully
                if status == "Accepted":
                    if stdout.strip() != expected.strip():
                        status = "Wrong Answer"

                results.append({
                    "input": tc.get("input"),
                    "expected": expected,
                    "actual": stdout,
                    "status": status,
                    "error": run_result.get("stderr"),
                    "time": run_result.get("cpu_time"), # In milliseconds
                    "memory": run_result.get("memory")  # In bytes
                })
                logger.info(f"Test case #{i+1} result: {status} (Time: {run_result.get('cpu_time')}ms, Memory: {run_result.get('memory')}B)")

            except Exception as e:
                logger.error(f"Error during Piston evaluation for TC #{i+1}: {str(e)}")
                results.append({
                    "input": tc.get("input"),
                    "expected": tc.get("expected_output"),
                    "actual": None,
                    "status": "Internal Error",
                    "error": str(e)
                })

        return results

    def close(self):
        self.client.close()
