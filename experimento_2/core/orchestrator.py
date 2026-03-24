from pathlib import Path
from .config import config
from services import LLMService, JudgeService
from models.problem import Problem
from models.evaluation_result import EvaluationResult
from models.level import Level
from prompts import ZERO_SHOT_PROMPT_TEMPLATE, FEW_SHOT_PROMPT_TEMPLATE, LEVEL_PROMPT_TEMPLATE, EXAMPLES_BY_LANGUAGE
import pandas as pd
import os
import glob


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
            target_dir = Path(base) / model / self.__type / self.__language

            target_dir.mkdir(parents=True, exist_ok=True)
            file_path = target_dir / name
            file_path.write_text(content, encoding="utf-8")

            print(f"Arquivo criado com sucesso em: {file_path}")
            return True

        except Exception as e:
            print(f"Erro ao criar o arquivo {name}: {e}")
            return False

    def create_csv(self, base: str = "output", model: str = "test", results: list = None) -> bool:
        try:
            target_dir = Path(base) / "results"
            target_dir.mkdir(parents=True, exist_ok=True)

            if not results:
                print("Aviso: Lista de resultados vazia. CSV não será gerado.")
                return False

            file_name = f"results_{model}_{self.__language}_{self.__type}.csv"
            file_path = target_dir / file_name

            df = pd.DataFrame([r.model_dump() for r in results])

            df.to_csv(file_path, index=False, encoding="utf-8")

            print(f"Relatório CSV gerado com sucesso em: {file_path}")
            return True

        except Exception as e:
            print(f"Erro ao gerar o CSV de resultados: {e}")
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
        path_test_cases = f"{path}{name}/test_cases/"
        print(path_test_cases)

        if os.path.exists(path_test_cases):
            in_files = glob.glob(os.path.join(path_test_cases, "**", "*.in"), recursive=True)
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

    def get_examples_of_problem(self, examples: list[Problem]) -> str:
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

        output += f"\n{self.get_examples_of_problem(problem.examples)}"

        return output

    def get_exemplos(self):

        examples_list = EXAMPLES_BY_LANGUAGE.get(self.__language, [])

        output = "<exemplos>\n"
        for example in examples_list:
            output += f"{example}"
        output += "<exemplos>\n"

        return output

    def execute(self, problems: list):

        for _, provider in config.list_providers().items():

            model = provider.model_name
            base_url = provider.base_url
            api_key = provider.api_key

            print("[CODIFICADOR]: Modelo LMM: ", model)

            llm_service = LLMService(model=model,
                                     base_url=base_url,
                                     api_key=api_key,
                                     temperature=0.0)

            judge_service = JudgeService(language=self.__language)

            results = []

            path_results = Path(
                f"output/results/results_{model}_{self.__language}_{self.__type}.csv")

            if path_results.exists():
                df = pd.read_csv(path_results)

                registros = df.to_dict('records')

                for row in registros:
                    results.append(EvaluationResult(**row))

            questoes_concluidas = {
                resultado.question_name for resultado in results}

            for problem in problems:

                if problem.title in questoes_concluidas:
                    print(f"Pulando '{problem.title}' (já avaliado).")
                    continue

                test_cases = self.get_test_cases(
                    "database/", problem.title, [])
                
                print(f"Processando questão: {problem.title}")
                
                if self.__type == "zero":
                    prompt = ZERO_SHOT_PROMPT_TEMPLATE.format(linguagem=self.__language,
                                                              contexto=self.format_problem(problem))
                elif self.__type == "few":
                    prompt = FEW_SHOT_PROMPT_TEMPLATE.format(linguagem=self.__language,
                                                             contexto=self.format_problem(
                                                                 problem),
                                                             exemplos=self.get_exemplos())
                else:
                    return False

                code_response, total_tokens, cost_prompt, duration_create_code = llm_service.create_code_llm(
                    prompt=prompt)

                code = self.valid_code(code_response)

                if self.create_file(name=f"{problem.title}.{self.__format_file_code}",
                                    base="output",
                                    model=model,
                                    content=code):
                    print("Arquivo criado com sucesso!!")
                else:
                    print("Próxima questão...")

                    results.append(EvaluationResult(
                        question_name=problem.title,
                        difficulty=problem.difficulty,
                        llm_code_creation_time=duration_create_code,
                        total_tokens=total_tokens,
                        cost_prompt=cost_prompt,
                        judge_predict="NO CODE",
                        execution_time=0.0,
                        AC=0,
                        WA=0,
                        RE=0,
                        TLE=0,
                        CE=0,
                        total_test_cases=len(test_cases)
                    ))

                    continue

                judge_predict, counts, total_cases, max_time = judge_service.execute(code=code,
                                                                                     test_cases=test_cases)

                print(counts)
                
                results.append(EvaluationResult(
                    question_name=problem.title,
                    difficulty=problem.difficulty,
                    llm_code_creation_time=duration_create_code,
                    total_tokens=total_tokens,
                    cost_prompt=cost_prompt,
                    judge_predict=judge_predict,
                    execution_time=max_time,
                    AC=counts["AC"],
                    WA=counts["WA"],
                    RE=counts["RE"],
                    TLE=counts["TLE"],
                    CE=counts["CE"],
                    total_test_cases=total_cases
                ))
                
                if self.create_csv(results=results, model=model):
                    print("Resultado criado com sucesso!")
                else:
                    print("Erro ao criar o resultado")
                    
                del prompt

            del llm_service, judge_service

        return True
