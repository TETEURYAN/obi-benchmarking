from openai import OpenAI


class LLMService:

    def __init__(self,
                 model: str = "None",
                 base_url: str = "www.test.com",
                 api_key: str = "no-api-key",
                 temperature: float = 0.0):

        self.__client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        self.__model = model
        self.__temperature = temperature

    def level_question(self, prompt: str) -> str:
        try:
            level = self.__send_prompt(prompt=prompt)
            
            if level[0] == "`":
                level = level.split('\n')[1]
            
            if level in ['FACIL', 'MEDIO', 'DIFICIL']:
                return level
            
            return "NÃO CONSEGUIU CLASSIFICAR"
            
        except Exception:
            print("Erro ao criar o código!")
            return None
    
    def create_code_llm(self, prompt: str) -> str:
        try:
            return self.__send_prompt(prompt=prompt)
        except Exception:
            print("Erro ao criar o código!")
            return None

    def __send_prompt(self, prompt: str):
        response = self.__client.chat.completions.create(
            model=self.__model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.__temperature
        )
        
        return response.choices[0].message.content
