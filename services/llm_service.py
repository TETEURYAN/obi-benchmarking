from openai import OpenAI

class LLMService:
    
    def __init__(self,
                 model: str = "None",
                 base_url: str ="www.test",
                 api_key:str ="no-api-key",
                 temperature: float = 0.0):
        
        self.__client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
        self.__model = model
        self.__temperature = temperature