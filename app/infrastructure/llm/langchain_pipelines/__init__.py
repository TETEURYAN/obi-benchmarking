"""LangChain pipelines (optional alternative to PydanticAI agents)."""

from app.infrastructure.llm.langchain_pipelines.comprehension_pipeline import (
    LangChainComprehensionPipeline,
)

__all__ = ["LangChainComprehensionPipeline"]
