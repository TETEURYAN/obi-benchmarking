import sys

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    # Verificação básica para garantir que a entrada não está vazia
    if not input_data:
        return

    # Parse dos valores conforme descrição
    # P: 0 se Alice gritou "par", 1 se Bob gritou "par"
    # D1: dedos de Alice
    # D2: dedos de Bob
    p = int(input_data[0])
    d1 = int(input_data[1])
    d2 = int(input_data[2])

    # Cálculo da soma dos dedos
    soma = d1 + d2

    # Determinação do vencedor
    # Se a soma é par, quem gritou "par" ganha.
    # Se a soma é ímpar, quem gritou "ímpar" ganha.
    
    if soma % 2 == 0:
        # Soma par: vence quem gritou "par".
        # Se P=0 (Alice par), vence Alice (0).
        # Se P=1 (Bob par), vence Bob (1).
        print(p)
    else:
        # Soma ímpar: vence quem gritou "ímpar".
        # Se P=0 (Alice par -> Bob ímpar), vence Bob (1).
        # Se P=1 (Bob par -> Alice ímpar), vence Alice (0).
        print(1 - p)

if __name__ == "__main__":
    main()