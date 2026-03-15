import tempfile
import os
import time
import subprocess
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple, Dict

class JudgeService:
    def __init__(self, language: str = "python"):
        self.__language = language.lower()
        if self.__language == "python":
            self.__extension = "py"
            self.__python_cmd = sys.executable 
        else:
            self.__extension = "cpp"

    def __clean_code(self, code: str) -> str:
        code = code.strip()
        if code.startswith("```"):
            lines = code.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            code = "\n".join(lines)
        return code.strip()

    def __run_single_test(self, code: str, stdin: str, expected: str, timeout: float) -> str:
        suffix = f".{self.__extension}"
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            source_file = tmp_path / f"code{suffix}"
            source_file.write_text(code, encoding="utf-8")
            
            try:
                if self.__language == "cpp":
                    executable = tmp_path / "program.out"
                    compile_res = subprocess.run(
                        ['g++', str(source_file), '-o', str(executable)],
                        capture_output=True, text=True, timeout=15.0
                    )
                    if compile_res.returncode != 0:
                        return "CE"
                    cmd = [str(executable)]
                else:
                    cmd = [self.__python_cmd, str(source_file)]

                process = subprocess.run(
                    cmd, 
                    input=stdin, 
                    capture_output=True, 
                    text=True, 
                    timeout=timeout
                )

                if process.returncode != 0:
                    return "RE"

                if process.stdout.strip() == expected.strip():
                    return "AC"
                else:
                    return "WA"

            except subprocess.TimeoutExpired:
                return "TLE"
            except Exception:
                return "RE"

    def execute(self, code: str, test_cases: List[Tuple[str, str]], timeout: float = 2.0) -> Tuple[str, int, int]:
        clean_code = self.__clean_code(code)
        total_cases = len(test_cases)
        
        if not clean_code or not test_cases:
            return "CE", 0, total_cases

        print(f"\n--- Iniciando Judge: {self.__language.upper()} ---")

        def worker(case):
            inp, exp = case
            return self.__run_single_test(clean_code, inp, exp, timeout)

        max_workers = min(32, (os.cpu_count() or 1) * 4)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(worker, test_cases))

        counts = {
            "AC": results.count("AC"),
            "WA": results.count("WA"),
            "RE": results.count("RE"),
            "TLE": results.count("TLE"),
            "CE": results.count("CE")
        }

        # Lógica de Situação Final:
        # 1. Se houve erro de compilação em qualquer lugar -> CE
        # 2. Se todos são AC -> AC
        # 3. Caso contrário, retorna o primeiro erro que não seja AC encontrado na lista
        if counts["CE"] > 0:
            status_final = "CE"
        elif counts["AC"] == total_cases:
            status_final = "AC"
        else:
            # Pega o primeiro erro que apareceu na ordem dos testes
            status_final = next(r for r in results if r != "AC")

        # --- RELATÓRIO FINAL ---
        print("\n" + "="*30)
        print(f"RESUMO DOS TESTES ({total_cases} casos)")
        print("-" * 30)
        print(f"  Accepted (AC):      {counts['AC']}")
        print(f"  Wrong Answer (WA):  {counts['WA']}")
        print(f"  Runtime Error (RE): {counts['RE']}")
        print(f"  Time Limit (TLE):   {counts['TLE']}")
        print(f"  Comp. Error (CE):   {counts['CE']}")
        print("-" * 30)
        print(f"SITUAÇÃO: {status_final}")
        print("="*30)

        return status_final, counts["AC"], total_cases