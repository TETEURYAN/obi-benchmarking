import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    # Leitura da matriz de pesos
    matrix = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(next(iterator)))
        matrix.append(row)

    # Pré-cálculo de soma de prefixos para cada linha
    # prefix_sums[r][i] armazena a soma de matrix[r][0] até matrix[r][i-1]
    prefix_sums = [[0] * (N + 1) for _ in range(N)]
    for r in range(N):
        current_sum = 0
        for c in range(N):
            current_sum += matrix[r][c]
            prefix_sums[r][c+1] = current_sum

    # Função auxiliar para obter a soma de um intervalo [l, r] na linha 'row'
    def get_row_sum(row, l, r):
        return prefix_sums[row][r+1] - prefix_sums[row][l]

    # Tabela de Programação Dinâmica
    # dp[r][c] representa o peso mínimo de uma pirâmide válida
    # que termina na linha 'r' (0-indexado), onde o intervalo na linha 'r'
    # começa na coluna 'c'.
    # O intervalo na linha 'r' terá comprimento 'r+1'.
    
    INF = float('inf')
    dp = [[INF] * N for _ in range(N)]

    # Caso base: Primeira linha (índice 0)
    # O intervalo tem tamanho 1. Pode começar em qualquer coluna 'c'.
    for c in range(N):
        dp[0][c] = matrix[0][c]

    # Transição para as linhas subsequentes
    for r in range(1, N):
        # Na linha 'r', o intervalo tem tamanho 'r+1'.
        # O início do intervalo 'c' pode variar de 0 a N - (r+1).
        # Ex: se N=3, r=1 (tam 2), c pode ser 0 ou 1.
        
        for c in range(N - r):
            # O intervalo atual é [c, c+r]
            current_weight = get_row_sum(r, c, c + r)
            
            # O intervalo da linha anterior (r-1) deve estar contido no atual.
            # A linha anterior tem tamanho 'r'.
            # Opção 1: Intervalo anterior começa em 'c' (alinhado à esquerda).
            #          Intervalo: [c, c+r-1].
            prev_weight_left = dp[r-1][c]
            
            # Opção 2: Intervalo anterior começa em 'c+1' (alinhado à direita).
            #          Intervalo: [c+1, c+r].
            prev_weight_right = dp[r-1][c+1]
            
            # Escolhemos a opção de menor peso total
            dp[r][c] = current_weight + min(prev_weight_left, prev_weight_right)

    # O resultado final é o peso mínimo para a última linha (N-1),
    # onde o intervalo deve ter tamanho N.
    # O único início possível é c=0.
    print(dp[N-1][0])

if __name__ == '__main__':
    solve()