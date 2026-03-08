"""
Prompt versioning for agents.

Allows A/B testing and rollback by loading prompts from a versioned directory (v1, v2, ...).
"""

from pathlib import Path
from typing import Optional


def get_prompts_dir(version: str = "v1") -> Path:
    """Return the path to the prompts directory for the given version."""
    base = Path(__file__).resolve().parent
    return base / version


def load_prompt(version: str, name: str, encoding: str = "utf-8") -> str:
    """
    Load a prompt template by version and name.

    Args:
        version: e.g. "v1"
        name: filename without extension, e.g. "comprehension"
        encoding: file encoding

    Returns:
        Prompt text.
    """
    path = get_prompts_dir(version) / f"{name}.txt"
    return path.read_text(encoding=encoding)
