from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Dict

class ProviderConfig(BaseModel):
    api_key: str
    model_name: str
    base_url: str

class _Config(BaseSettings):
    openai: ProviderConfig
    gemini: ProviderConfig

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        extra="ignore"
    )

    def list_providers(self) -> Dict[str, ProviderConfig]:
        """ Retorna um dicionário com o nome do provedor e seus dados """
        return {
            name: getattr(self, name) 
            for name in self.model_fields 
            if isinstance(getattr(self, name), ProviderConfig)
        }

config = _Config()