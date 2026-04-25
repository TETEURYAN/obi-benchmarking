import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    C = int(input_data[0])
    A = int(input_data[1])

    # A capacidade útil por viagem é C - 1 (reservando 1 vaga para o monitor).
    # O número mínimo de viagens é o teto da divisão de A por (C - 1).
    # Fórmula do teto da divisão inteira: (numerador + denominador - 1) // denominador
    
    capacidade_alunos = C - 1
    viagens = (A + capacidade_alunos - 1) // capacidade_alunos

    print(viagens)

if __name__ == "__main__":
    main()