"""
External Judge adapter (HTTP).

Calls an external judge API to submit code and retrieve test results.
Implements JudgePort so the application layer remains agnostic of the judge implementation.
"""

import logging

import httpx

from app.domain.ports.judges.judge import JudgePort, JudgeResult

logger = logging.getLogger(__name__)


class ExternalJudgeAdapter(JudgePort):
    """
    Judge implementation that submits code to an external HTTP API.

    Expects the judge API to accept POST with JSON body:
    { "code": "...", "language": "...", "problem_id": "...", "reveal_inputs": bool }
    and return JSON: { "passed": bool, "feedback": str | null, "failed_cases": [...] }.
    """

    def __init__(self, base_url: str, timeout_seconds: float = 30.0) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout_seconds

    def submit(
        self,
        code: str,
        language: str,
        problem_id: str,
        *,
        reveal_inputs: bool = False,
    ) -> JudgeResult:
        """Submit code to the external judge and return result."""
        url = f"{self._base_url}/submit"
        payload = {
            "code": code,
            "language": language,
            "problem_id": problem_id,
            "reveal_inputs": reveal_inputs,
        }
        try:
            with httpx.Client(timeout=self._timeout) as client:
                response = client.post(url, json=payload)
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPError as e:
            logger.exception("Judge request failed: %s", e)
            return JudgeResult(
                passed=False,
                feedback=f"Judge indisponível: {e!s}",
                failed_cases=None,
            )
        passed = data.get("passed", False)
        feedback = data.get("feedback")
        failed_cases = data.get("failed_cases")
        if failed_cases is not None and not isinstance(failed_cases, list):
            failed_cases = [failed_cases]
        return JudgeResult(
            passed=passed,
            feedback=feedback,
            failed_cases=failed_cases,
        )
