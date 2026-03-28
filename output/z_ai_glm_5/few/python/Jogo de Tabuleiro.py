import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Usando um iterador para processar os tokens sequencialmente
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    # Inicialização do tabuleiro
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            # Lê o valor (0, 1 ou 9 inicialmente)
            val = int(next(iterator))
            row.append(val)
        grid.append(row)

    # Preenchimento do tabuleiro
    # Começamos do índice 1 pois a linha 0 e coluna 0 são sementes
    for i in range(1, n):
        for j in range(1, n):
            # Somamos os valores dos 3 vizinhos relevantes
            # (i, j-1), (i-1, j-1), (i-1, j)
            s = grid[i][j-1] + grid[i-1][j-1] + grid[i-1][j]
            
            # Regra do problema:
            # Mais brancas (0s) que pretas (1s) -> preta (1)
            # Mais pretas (1s) que brancas (0s) -> branca (0)
            # s é a soma de 1s.
            # Se s <= 1, temos 0 ou 1 pedra preta. Logo, 2 ou 3 pedras brancas.
            # Brancas > Pretas. Resultado = 1.
            # Se s >= 2, temos 2 ou 3 pedras pretas. Logo, 1 ou 0 pedras brancas.
            # Pretas > Brancas. Resultado = 0.
            if s <= 1:
                grid[i][j] = 1
            else:
                grid[i][j] = 0

    # Imprime o resultado na célula (N, N), que é o índice (n-1, n-1)
    print(grid[n-1][n-1])

if __name__ == '__main__':
    main()