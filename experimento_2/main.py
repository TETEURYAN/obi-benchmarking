import json
from models.problem import Problem
from pathlib import Path
from core import Orchestrator

def load_problem(file_path: Path) -> Problem:
    data = json.loads(file_path.read_text(encoding="utf-8"))
    print("Carregando file: ", file_path)
    
    return Problem(**data)

def print_partition(text: str):
    print("="*70)
    print(text)
    print("="*70)

def get_int_input(text : str = "test") -> int:
    try:
        number = int(input(text))
        return number
    except Exception:
        return 0

def main():
    
    try:
        print_partition("CRIANDO DATABASE")
        
        path_database = Path("database")
        questions_path = []
        
        for folder in list(path_database.iterdir()):
            if folder.is_dir():
                questions_path.append(folder)
        
        
        problem_names = []            
        for path in questions_path:
            problem_names.append(path.name)
        
        problems = []
        for question_path in questions_path:
            problems.append(load_problem(Path(question_path / "problem.json")))
        
        print_partition("FIM DA CRIANÇÃO DATABASE")
    except Exception as e:    
        print("Erro na estrutura database. Verifique o diretorio!")
        print("Erro: ", e)
        exit(1)
    
    while True:
        print_partition(text="MENU")
        print("1. Zero shot prompt;")
        print("2. Few shot prompt.")
        print("Se digitar qualquer outra coisa; termina a execução!")
        op = get_int_input("Digite uma opção para prompt: ")
        
        type_prompt = "" 
        
        if op == 1:
            type_prompt = "zero"
        elif op == 2:
            type_prompt = "few"
        else:
            exit(0)

        print_partition(text="MENU")
        print("1. Python;")
        print("2. C++.")
        print("Se digitar qualquer outra coisa; termina a execução!")
        op = get_int_input("Escolha uma opção de linguagem: ")
        
        if op == 1:
            language = "python"
        elif op == 2:
            language = "cpp"
        else:
            exit(0)
        
        orchestrador = Orchestrator(type=type_prompt, language=language)
        if orchestrador.execute(problems=problems):
            print("Resultado está em output/results/")
            print_partition("REINICIANDO")
        else:
            exit(1)
        
if __name__ == "__main__":
    main()
