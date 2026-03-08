"""
Example LangChain pipeline for the Comprehension flow (Etapa 1).

This is an alternative to the PydanticAI-only agent: chains prompt + LLM + output parser.
Can be used when you need LangChain's tooling (e.g. chains, memory) or multiple steps.
"""

import json
import logging
from typing import Any

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.config.settings import get_settings
from app.domain.ports.agents.comprehension import (
    ComprehensionAgentPort,
    ComprehensionInput,
    ComprehensionOutput,
)
from app.infrastructure.prompts.versions import load_prompt

logger = logging.getLogger(__name__)


# Schema hint for the parser (optional; LLM must return valid JSON matching ComprehensionOutput)
COMPREHENSION_OUTPUT_SCHEMA = """
{
  "questao": {
    "descricao": "string",
    "entrada_problema": "string",
    "saida_problema": "string"
  },
  "perguntas": {
    "Pergunta literal": { "status": "correto|errado", "feedback": "string" }
  }
}
"""


class LangChainComprehensionPipeline(ComprehensionAgentPort):
    """
    Comprehension agent implemented as a LangChain pipeline.

    Pipeline: user message -> prompt template -> LLM -> JSON parser -> ComprehensionOutput.
    """

    def __init__(self, prompt_version: str = "v1") -> None:
        settings = get_settings()
        # LangChain OpenAI model name (e.g. gpt-4o-mini without prefix)
        model_name = settings.llm_model.split(":")[-1] if ":" in settings.llm_model else settings.llm_model
        self._llm = ChatOpenAI(model=model_name, temperature=0)
        self._system_prompt = load_prompt(prompt_version, "comprehension")
        self._parser = JsonOutputParser()

    def run(self, input_data: ComprehensionInput) -> ComprehensionOutput:
        """Run the pipeline and return structured output."""
        user_content = json.dumps(input_data, ensure_ascii=False, indent=2)
        prompt = ChatPromptTemplate.from_messages([
            ("system", self._system_prompt + "\n\nFormat output as JSON with keys: questao, perguntas."),
            ("human", "{input}"),
        ])
        chain = prompt | self._llm | self._parser
        try:
            result = chain.invoke({"input": user_content})
        except Exception as e:
            logger.exception("LangChain comprehension pipeline failed: %s", e)
            raise
        if not isinstance(result, dict):
            result = json.loads(result) if isinstance(result, str) else dict(result)
        return self._normalize_output(result)

    def _normalize_output(self, raw: dict[str, Any]) -> ComprehensionOutput:
        """Ensure output matches ComprehensionOutput shape."""
        questao = raw.get("questao") or {}
        perguntas = raw.get("perguntas") or {}
        return {
            "questao": {
                "descricao": str(questao.get("descricao", "")),
                "entrada_problema": str(questao.get("entrada_problema", "")),
                "saida_problema": str(questao.get("saida_problema", "")),
            },
            "perguntas": {
                k: {"status": str(v.get("status", "errado")), "feedback": str(v.get("feedback", ""))}
                for k, v in perguntas.items()
            },
        }
