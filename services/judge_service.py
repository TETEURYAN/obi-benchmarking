import tempfile
import os
import time
import subprocess
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple, Dict

class JudgeService:
    def __init__(self, language: str = "python"):
        self.__language = language.lower()
        # Define a extensão com base na linguagem
        self.__extension = "py" if self.__language == "python" else "cpp"

    def __clean_code(self, code: str) -> str:
        """Remove markdown wrappers (```python ... ```) e espaços inúteis."""
        code = code.strip()
        if code.startswith("```"):
            # Remove a primeira linha (ex: ```python) e a última (```)
            lines = code.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            code = "\n".join(lines)
        return code.strip()

    def __run_single_test(self, code: str, stdin: str, timeout: float) -> Dict:
        """Lógica interna para executar um único caso de teste."""
        suffix = f".{self.__extension}"
        # Criamos arquivos temporários para o código e para o executável (se for C++)
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            source_file = tmp_path / f"code{suffix}"
            source_file.write_text(code, encoding="utf-8")
            
            executable = source_file # Para Python, o 'executável' é o próprio script
            
            try:
                # --- FASE DE COMPILAÇÃO (Apenas C++) ---
                if self.__language == "cpp":
                    executable = tmp_path / "program.out"
                    compile_res = subprocess.run(
                        ['g++', str(source_file), '-o', str(executable)],
                        capture_output=True, text=True, timeout=15.0
                    )
                    if compile_res.returncode != 0:
                        return {"stdout": "", "stderr": f"C++ Compilation Error: {compile_res.stderr}", "code": 1}

                # --- FASE DE EXECUÇÃO ---
                cmd = ["python", str(executable)] if self.__language == "python" else [str(executable)]
                
                start_time = time.time()
                process = subprocess.run(
                    cmd, input=stdin, capture_output=True, text=True, timeout=timeout
                )
                exec_time = time.time() - start_time

                return {
                    "stdout": process.stdout,
                    "stderr": process.stderr,
                    "code": process.returncode,
                    "time": exec_time
                }

            except subprocess.TimeoutExpired:
                return {"stdout": "", "stderr": "TLE (Time Limit Exceeded)", "code": 124, "time": timeout}
            except Exception as e:
                return {"stdout": "", "stderr": str(e), "code": 1, "time": 0.0}

    def execute(self, code: str, test_cases: List[Tuple[str, str]], timeout: float = 2.0) -> Tuple[bool, int, int]:
        """
        Ponto de entrada único para o Judge.
        Retorna: (sucesso_total, casos_passados, total_de_casos)
        """
        clean_code = self.__clean_code(code)
        if not clean_code or not test_cases:
            return False, 0, len(test_cases)

        total_cases = len(test_cases)
        passed_count = 0
        
        print(f"Iniciando Judge para {self.__language.upper()} ({total_cases} casos)...")

        def worker(case):
            inp, expected = case
            result = self.__run_single_test(clean_code, inp, timeout)
            
            # Validação: stdout limpo deve ser igual ao esperado limpo
            is_correct = (
                result["code"] == 0 and 
                result["stdout"].strip() == expected.strip()
            )
            return is_correct

        # Execução paralela
        max_workers = min(32, (os.cpu_count() or 1) * 4)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(worker, test_cases))

        passed_count = sum(results)
        all_passed = passed_count == total_cases
        
        print(f"Resultado: {passed_count}/{total_cases} passados.")
        return all_passed, passed_count, total_cases