import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro e único número é a dimensão N
    n = int(input_data[0])
    
    # Lista para armazenar as linhas da saída
    output_lines = []
    
    # Itera sobre cada linha e coluna da matriz N x N
    for i in range(n):
        row_values = []
        for j in range(n):
            # O valor em cada posição (i, j) é a altura da pilha de cubos.
            # A altura é determinada pela distância até a borda mais próxima.
            # Se considerarmos índices 1-based (1 a N):
            # Distância ao topo: i + 1
            # Distância à base: n - i
            # Distância à esquerda: j + 1
            # Distância à direita: n - j
            # O valor é o mínimo dessas distâncias.
            val = min(i + 1, n - i, j + 1, n - j)
            row_values.append(str(val))
        
        # Junta os valores da linha com espaço
        output_lines.append(" ".join(row_values))
    
    # Imprime o resultado
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()