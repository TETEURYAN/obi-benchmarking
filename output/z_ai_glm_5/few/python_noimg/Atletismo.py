import sys

def main():
    # Lê toda a entrada de uma vez para maior performance
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro valor é N
    n = int(input_data[0])
    
    # Array para armazenar a posição de cada atleta (índice 1 a N)
    # Inicializado com 0
    positions = [0] * (n + 1)
    
    # Os próximos N valores são os atletas na ordem de chegada
    # input_data[1] é o 1º colocado, input_data[i] é o i-ésimo colocado
    # Iteramos de 1 a N para definir as posições
    for i in range(1, n + 1):
        athlete = int(input_data[i])
        positions[athlete] = i
        
    # Prepara a saída para impressão rápida
    output = []
    for i in range(1, n + 1):
        output.append(str(positions[i]))
    
    # Imprime o resultado
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    main()