import sys

def main():
    # Lê toda a entrada de uma vez para garantir performance
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro número é o número sorteado (X)
    target = int(input_data[0])
    
    output_lines = []
    
    # Processa as tentativas subsequentes
    # Começa do índice 1 até o fim dos dados lidos
    for i in range(1, len(input_data)):
        guess = int(input_data[i])
        
        if guess == target:
            output_lines.append("correto")
            break # O jogo termina ao acertar
        elif guess > target:
            output_lines.append("menor")
        else:
            output_lines.append("maior")
            
    # Imprime todas as respostas de uma vez
    sys.stdout.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()