from openai import OpenAI
import time

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
    
    def cal_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        
        output_price = 0.0
        input_price = 0.0
        
        if self.__model == "gemini-3.1-pro-preview":
            if prompt_tokens < 200000:
                output_price = float(12.0/1000000.0)
                input_price = float(2.0/1000000.0)
            else:
                output_price = float(18.0/1000000.0)
                input_price = float(4.0/1000000.0)
        elif self.__model == "gpt-5.4-2026-03-05":
            output_price = float(15.0/1000000.0)
            input_price = float(2.5/1000000.0)
            
        return prompt_tokens * input_price + completion_tokens * output_price
    
    def create_code_llm(self, prompt: str) -> tuple[str, int, float, float]:
        try:
            result = self.__send_prompt(prompt=prompt)
            total = result["prompt_tokens"] + result["completion_tokens"]
            cost = self.cal_cost(result["prompt_tokens"], result["completion_tokens"])
            
            return result["content"], total, cost, result["duration_prompt"]
        except Exception:
            print("Erro ao criar o código!")
            return None

    def __send_prompt(self, prompt: str):
        
        try:
            start_time = time.perf_counter()
            response = self.__client.chat.completions.create(
                model=self.__model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.__temperature
            )
            end_time = time.perf_counter()
                
            content = response.choices[0].message.content
            usage = response.usage
            
            return {
                "content": content,
                "prompt_tokens": usage.prompt_tokens,
                "completion_tokens": usage.completion_tokens,
                "total_tokens": usage.total_tokens,
                "duration_prompt": end_time - start_time
            }
        except Exception as e:
            print(f"Erro na chamada da API OpenAI: {e}")
            raise
