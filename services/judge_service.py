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

    def __run_single_test(self, code: str, stdin: str, expected: str, timeout: float) -> Tuple[str, float]:
        """Retorna uma tupla (sigla_resultado, tempo_execucao)."""
        suffix = f".{self.__extension}"
        exec_time = 0.0
        
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
                        return "CE", 0.0
                    cmd = [str(executable)]
                else:
                    cmd = [self.__python_cmd, str(source_file)]

                # Medição de tempo precisa
                start_mark = time.perf_counter()
                process = subprocess.run(
                    cmd, 
                    input=stdin, 
                    capture_output=True, 
                    text=True, 
                    timeout=timeout
                )
                exec_time = time.perf_counter() - start_mark

                if process.returncode != 0:
                    return "RE", exec_time

                if process.stdout.strip() == expected.strip():
                    return "AC", exec_time
                else:
                    return "WA", exec_time

            except subprocess.TimeoutExpired:
                return "TLE", timeout
            except Exception:
                return "RE", exec_time

    def execute(self, code: str, test_cases: List[Tuple[str, str]], timeout: float = 15.0) -> Tuple[str, dict, int, float]:
        """
        Retorna: (status_final, contagem_dict, total_casos, maior_tempo_execucao)
        """
        clean_code = self.__clean_code(code)
        total_cases = len(test_cases)
        
        if not clean_code or not test_cases:
            return "CE", {}, total_cases, 0.0

        print(f"\n--- Iniciando Judge: {self.__language.upper()} ---")

        def worker(case):
            inp, exp = case
            return self.__run_single_test(clean_code, inp, exp, timeout)

        max_workers = min(32, (os.cpu_count() or 1) * 4)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results_with_time = list(executor.map(worker, test_cases))

        statuses = [r[0] for r in results_with_time]
        times = [r[1] for r in results_with_time]
        
        max_time = max(times) if times else 0.0

        counts = {
            "AC": statuses.count("AC"),
            "WA": statuses.count("WA"),
            "RE": statuses.count("RE"),
            "TLE": statuses.count("TLE"),
            "CE": statuses.count("CE")
        }

        if counts["CE"] > 0:
            status_final = "CE"
        elif counts["AC"] == total_cases:
            status_final = "AC"
        else:
            status_final = next(s for s in statuses if s != "AC")

        print("\n" + "="*30)
        print(f"RESUMO DOS TESTES ({total_cases} casos)")
        print("-" * 30)
        print(f"  Accepted (AC):      {counts['AC']}")
        print(f"  Wrong Answer (WA):  {counts['WA']}")
        print(f"  Runtime Error (RE): {counts['RE']}")
        print(f"  Time Limit (TLE):   {counts['TLE']}")
        print(f"  Comp. Error (CE):   {counts['CE']}")
        print("-" * 30)
        print(f"MAIOR TEMPO: {max_time:.3f}s")
        print(f"SITUAÇÃO: {status_final}")
        print("="*30)

        return status_final, counts, total_cases, max_time