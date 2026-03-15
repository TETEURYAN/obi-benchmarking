from pathlib import Path
from core import config
import os
import glob
from services import LLMService, JudgeService
from prompts import ZERO_SHOT_PROMPT_TEMPLATE, FEW_SHOT_PROMPT_TEMPLATE
from models.problem import Problem


class Orchestrator:

    def __init__(self, type: str, language: str):
        self.__type = type
        self.__language = language

        if language == "python":
            self.__format_file_code = "py"
        elif language == "cpp":
            self.__format_file_code = "cpp"

    def create_file(self,
                    name: str = "test.cpp",
                    base: str = "output",
                    model: str = "test",
                    content: str = "test") -> bool:
        try:
            Path(f"{base}/{model}/{self.__type}/{self.__language}/").mkdir(parents=True, exist_ok=True)
            Path(f"{base}/{model}/{self.__type}/{self.__language}/{name}").touch()
            file = Path(f"{base}/{model}/{self.__type}/{self.__language}/{name}")
            file.write_text(content)
            return True
        except Exception:
            print("Erro ao criar o código")
            return False
            
    def valid_code(self, code: str) -> str:

        if code is None:
            return code

        if code[0] == "`":
            if self.__language == "cpp":
                code = code[6:len(code) - 3]
            elif self.__language == "python":
                code = code[9:len(code) - 3]

        return code

    def get_test_cases(self,
                       path: str,
                       name: str,
                       default_examples: list) -> list[tuple[str, str]]:

        test_cases = []
        path_test_cases = f"{path}/{name}/"

        if os.path.exists(path_test_cases):
            in_files = glob.glob(os.path.join(
                path_test_cases, "**", "*.in"), recursive=True)
            for in_file in in_files:
                sol_file = in_file.replace(".in", ".sol")
                if os.path.exists(sol_file):
                    with open(in_file, 'r') as f:
                        in_content = f.read()
                    with open(sol_file, 'r') as f:
                        sol_content = f.read()
                    test_cases.append((in_content, sol_content))

        if not test_cases:
            test_cases = [(e.input, e.output) for e in default_examples]

        return test_cases

    def get_exemples_of_problem(self, examples: list[Problem]) -> str:
        output = "<test cases>\n"
        i = 1

        for example in examples:
            output += f"<test {i}>\n"
            output += "<input test>\n"
            output += f"{example.input}\n"
            output += "</input test>\n"

            output += "<output test>\n"
            output += f"{example.output}\n"
            output += "</output teste>\n"
            output += f"</test {i}>\n"

            i += 1

        output += "</test cases>\n"

        return output

    def format_problem(self, problem: Problem) -> str:
        output = "<title>\n"
        output += f"{problem.title}\n"
        output += "</title>\n"

        output += "<descrition>\n"
        output += f"{problem.statement}\n"
        output += "</descrition>\n"

        output += "<constraints>\n"
        output += f"{problem.constraints}\n"
        output += "\n</constraints>\n"

        output += "<input format>\n"
        output += f"{problem.input}\n"
        output += "</input format>\n"

        output += "<output format>\n"
        output += f"{problem.output}\n"
        output += "</output format>\n"

        output += f"\n{self.get_exemples_of_problem(problem.examples)}"

    def execute(self, problems: list, questions_path: list):

        model = config.GEMINI_MODEL_NAME
        llm_service = LLMService(model=config.GEMINI_MODEL_NAME,
                                 base_url=config.GEMINI_BASE_URL,
                                 api_key=config.GEMINI_API_KEY,
                                 temperature=0.0)

        judge_service = JudgeService(language=self.__language)

        problem_names = []
        for path in questions_path:
            problem_names.append(path.name)

        for problem in problems:
            print(f"Processando questão: {problem.title}")
            prompt = "test"

            if self.__type == "zero":
                prompt = ZERO_SHOT_PROMPT_TEMPLATE.format(
                    contexto=self.format_problem(problem))
            elif self.__type == "few":
                prompt = FEW_SHOT_PROMPT_TEMPLATE.format(
                    contexto=self.format_problem(problem))
            else:
                return False

            code_response = llm_service.create_code_llm(prompt=prompt)
            code = self.valid_code(code_response)
            
            if self.create_file(name=f"{problem}.{self.__format_file_code}",
                                base="output",
                                model=model,
                                content=code):
                print("Arquivo criado com sucesso!!")
            else:
                print("Próxima questão...")
                continue

            judge_service.execute(code=code)

            del prompt

        del llm_service, judge_service
        return True
