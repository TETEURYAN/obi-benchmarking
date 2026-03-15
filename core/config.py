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
    # deepseek: ProviderConfig ...

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__", # Importante para o .env com dois underscores
        extra="ignore"
    )

    def list_providers(self) -> Dict[str, ProviderConfig]:
        """ Retorna um dicionário com o nome do provedor e seus dados """
        # Filtra apenas os atributos que são do tipo ProviderConfig
        return {
            name: getattr(self, name) 
            for name in self.model_fields 
            if isinstance(getattr(self, name), ProviderConfig)
        }

settings = _Config()