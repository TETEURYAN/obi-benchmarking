import sys

def main():
    # Lê toda a entrada de uma vez para eficiência
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é N
    n = int(input_data[0])
    
    # Os próximos N elementos são a ordem de chegada
    # input_data[1] é o 1º colocado, input_data[2] é o 2º, etc.
    
    # Array para armazenar a posição de cada atleta (índice 1 a N)
    # Inicializa com 0 ou qualquer valor, será sobrescrito
    posicoes = [0] * (n + 1)
    
    # Itera sobre os atletas na ordem de chegada
    # O índice 'i' no loop representa a posição de chegada (0 a N-1)
    # O valor 'atleta' é o número do atleta
    arrival_list = input_data[1:]
    
    for i in range(n):
        atleta_id = int(arrival_list[i])
        # A posição no ranking é i + 1 (1-based)
        posicoes[atleta_id] = i + 1
        
    # Gera a saída
    # Imprime a posição do atleta 1, depois do 2, ..., até N
    output = []
    for i in range(1, n + 1):
        output.append(str(posicoes[i]))
        
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    main()