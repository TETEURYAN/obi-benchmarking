from pydantic_settings import BaseSettings, SettingsConfigDict

class _Config(BaseSettings):
    
    """
        Atributos:
            GEMINI_API_KEY: Chave da API do Gemini
            GEMINI_MODEL_NAME: Modelo do Gemini
            GEMINI_BASE_URL: Base do link para OPENAI
             
            GPT_API_KEY - Chave para API do GPT
    """
    
    #GEMINI config
    GEMINI_API_KEY: str
    GEMINI_MODEL_NAME: str
    GEMINI_BASE_URL: str
    
    #GPT config
    GPT_API_KEY: str
    GPT_MODEL_NAME: str
    GPT_BASE_URL: str
    
    #DEEPSEEK config
    DEEPSEEK_API_KEY: str
    DEEPSEEK_MODEL_NAME: str
    DEEPSEEK_BASE_URL: str
    
    #GPT-OSS config
    GPT_OSS_API_KEY: str
    GPT_OSS_MODEL_NAME: str
    GPT_OSS_BASE_URL: str
    
    #LLAMA config
    LLAMA_OSS_API_KEY: str
    LLAMA_OSS_MODEL_NAME: str
    LLAMA_OSS_BASE_URL: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    
    
config = _Config()