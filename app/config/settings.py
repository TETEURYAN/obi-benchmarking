"""
Application configuration loaded from environment variables.

Centralizes all settings so that the LLM provider and other infrastructure
can be swapped without changing domain or application code.
"""

import os
from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings. Prefer env vars; .env is loaded automatically.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # LLM: model string compatible with PydanticAI (e.g. openai:gpt-4o-mini, openai:gpt-4o)
    llm_model: str = Field(
        default="openai:gpt-4o-mini",
        description="PydanticAI model string for the agent (e.g. openai:gpt-4o-mini)",
    )

    # Environment
    environment: Literal["development", "staging", "production"] = Field(
        default="development",
        description="Runtime environment",
    )

    # API
    api_host: str = Field(default="0.0.0.0", description="Host to bind the API server")
    api_port: int = Field(default=8000, description="Port for the API server")


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()
