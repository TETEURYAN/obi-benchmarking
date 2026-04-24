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


def execute_problems_by_year(problems: list, year: int):
    
    print_partition(text="ZERO-SHOT vs FEW-SHOT")
    problems_year = []
    
    for name, problem in problems:
        if int(problem.year) == year:
            print("Nome da questão: ", name)
            problems_year.append((name, problem))
    
    types = ['zero', 'few']
    languages = ['python', 'cpp']
    image_modes = [False, True]
    
    for t in types:
        for lan in languages:
            for use_img in image_modes:
                img_label = "COM imagens" if use_img else "SEM imagens"
                print_partition(f"Executando: {t} | {lan} | {img_label}")
                orch = Orchestrator(type=t, language=lan, use_images=use_img)
                if orch.execute(problems=problems_year):
                    print("Resultado está em output/results/")
                    print_partition("REINICIANDO")
                else:
                    exit(1)
    
    print_partition(text="FIM ZERO-SHOT vs FEW-SHOT")
    
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
            problems.append((question_path.name, load_problem(Path(question_path / "problem.json"))))
        
        print_partition("FIM DA CRIAÇÃO DATABASE")
    except Exception as e:    
        print("Erro na estrutura database. Verifique o diretorio!")
        print("Erro: ", e)
        exit(1)
    
    while True:
        print_partition(text="MENU")
        
        op = input("Quer executar um ano específico (y/n): ")
        if op == 'y':
            year = get_int_input("Digite um ano entre 1999 a 2026: ")
            execute_problems_by_year(problems, year)
        else:
            print_partition(text="MENU")
            break
    
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

        print_partition(text="MENU")
        print("1. Sem imagens (text-only);")
        print("2. Com imagens (multimodal).")
        print("Se digitar qualquer outra coisa; termina a execução!")
        op = get_int_input("Escolha uma opção de imagem: ")
        
        if op == 1:
            use_images = False
        elif op == 2:
            use_images = True
        else:
            exit(0)
        
        orchestrador = Orchestrator(type=type_prompt, language=language, use_images=use_images)
        if orchestrador.execute(problems=problems):
            print("Resultado está em output/results/")
            print_partition("REINICIANDO")
        else:
            exit(1)
        
if __name__ == "__main__":
    main()

