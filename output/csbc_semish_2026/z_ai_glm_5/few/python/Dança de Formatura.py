import sys

# Aumentar o limite de recursão, embora não seja estritamente necessário para esta solução iterativa.
sys.setrecursionlimit(200000)

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para consumir os tokens de entrada sequencialmente
    iterator = iter(input_data)
    
    try:
        # Leitura de N, M e P
        N = int(next(iterator))
        M = int(next(iterator))
        P = int(next(iterator))
    except StopIteration:
        return

    # Inicialização dos vetores de mapeamento de permutação.
    # row_map[i] armazena o índice da linha original que está atualmente na linha i.
    # col_map[j] armazena o índice da coluna original que está atualmente na coluna j.
    # Inicialmente, a linha i contém a linha i, e a coluna j contém a coluna j.
    row_map = list(range(N))
    col_map = list(range(M))

    # Processamento dos P passos da dança
    for _ in range(P):
        # Leitura do tipo de operação e índices
        op = next(iterator)
        a = int(next(iterator)) - 1 # Converter para 0-based
        b = int(next(iterator)) - 1 # Converter para 0-based
        
        if op == 'L':
            # Troca de linhas: atualizamos o mapa de linhas
            row_map[a], row_map[b] = row_map[b], row_map[a]
        elif op == 'C':
            # Troca de colunas: atualizamos o mapa de colunas
            col_map[a], col_map[b] = col_map[b], col_map[a]

    # Construção da saída
    output_lines = []
    
    # Iteramos sobre a grade final (N linhas)
    for i in range(N):
        # A linha atual 'i' contém originalmente a linha 'row_map[i]'
        r_orig = row_map[i]
        
        # Calculamos o valor base para esta linha original: (r_orig) * M
        # Isso evita multiplicar repetidamente dentro do loop interno
        base_val = r_orig * M
        
        # Geramos os valores para a linha atual
        # O valor na coluna j é (r_orig * M) + col_map[j] + 1
        # Usamos um gerador dentro do join para eficiência de memória
        row_str = " ".join(str(base_val + col_map[j] + 1) for j in range(M))
        output_lines.append(row_str)
    
    # Imprimimos o resultado de uma vez para minimizar o overhead de I/O
    sys.stdout.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()