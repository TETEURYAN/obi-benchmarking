"""
Dependency injection for the API layer.

Provides use cases and repositories with concrete implementations
(agents, judges, persistence). Swap implementations here for tests or different envs.
"""

from app.application.use_cases.etapa1_comprehension import Etapa1ComprehensionUseCase
from app.config.settings import get_settings
from app.domain.ports.agents.comprehension import ComprehensionAgentPort
from app.infrastructure.judges.external_judge_adapter import ExternalJudgeAdapter
from app.infrastructure.llm.pydantic_ai_agents.comprehension_agent import (
    PydanticAIComprehensionAgent,
)
from app.infrastructure.llm.langchain_pipelines.comprehension_pipeline import (
    LangChainComprehensionPipeline,
)
from app.infrastructure.persistence.in_memory_etapa_context_repository import (
    InMemoryEtapaContextRepository,
)
from app.infrastructure.persistence.in_memory_user_implementation_repository import (
    InMemoryUserImplementationRepository,
)


# Singletons for lazy init (optional: replace with proper DI container)
_etapa_context_repo: InMemoryEtapaContextRepository | None = None
_user_impl_repo: InMemoryUserImplementationRepository | None = None
_comprehension_agent: ComprehensionAgentPort | None = None
_judge: ExternalJudgeAdapter | None = None


def get_etapa_context_repository() -> InMemoryEtapaContextRepository:
    """Return the etapa context repository (in-memory for dev)."""
    global _etapa_context_repo
    if _etapa_context_repo is None:
        _etapa_context_repo = InMemoryEtapaContextRepository()
    return _etapa_context_repo


def get_user_implementation_repository() -> InMemoryUserImplementationRepository:
    """Return the user implementation repository (in-memory for dev)."""
    global _user_impl_repo
    if _user_impl_repo is None:
        _user_impl_repo = InMemoryUserImplementationRepository()
    return _user_impl_repo


def get_comprehension_agent() -> ComprehensionAgentPort:
    """
    Return the comprehension agent (Etapa 1).

    Uses COMPREHENSION_AGENT env: "pydantic_ai" (default) or "langchain".
    Both are example implementations of ComprehensionAgentPort.
    """
    global _comprehension_agent
    if _comprehension_agent is None:
        settings = get_settings()
        if settings.comprehension_agent == "langchain":
            _comprehension_agent = LangChainComprehensionPipeline(
                prompt_version=settings.prompt_version,
            )
        else:
            _comprehension_agent = PydanticAIComprehensionAgent(
                prompt_version=settings.prompt_version,
            )
    return _comprehension_agent


def get_judge() -> ExternalJudgeAdapter:
    """Return the Judge port implementation (external HTTP API)."""
    global _judge
    if _judge is None:
        settings = get_settings()
        _judge = ExternalJudgeAdapter(
            base_url=settings.judge_base_url,
            timeout_seconds=settings.judge_timeout_seconds,
        )
    return _judge


def get_etapa1_comprehension_use_case() -> Etapa1ComprehensionUseCase:
    """Build Etapa 1 use case with injected dependencies."""
    return Etapa1ComprehensionUseCase(
        comprehension_agent=get_comprehension_agent(),
        etapa_context_repository=get_etapa_context_repository(),
    )
