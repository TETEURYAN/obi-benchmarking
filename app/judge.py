import os
import judge0
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class Judge:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("JUDGE0_API_KEY")
        self.client = judge0.Client(self.api_key) if self.api_key else None

    def evaluate(self, code: str, language_id: int, test_cases: List[Dict]) -> List[Dict]:
        """
        Evaluate code against a list of test cases.
        For now, this is a mock if no API key is provided.
        """
        if not self.client:
            # Mock implementation
            results = []
            for tc in test_cases:
                results.append({
                    "input": tc.get("input"),
                    "expected": tc.get("expected_output"),
                    "actual": "MOCKED",
                    "status": "Accepted" if "MOCKED" == tc.get("expected_output") else "Wrong Answer"
                })
            return results

        # Actual implementation with judge0 would go here
        # This is a placeholder for actual SDK usage
        return [{"status": "MOCKED_SUCCESS"}]
