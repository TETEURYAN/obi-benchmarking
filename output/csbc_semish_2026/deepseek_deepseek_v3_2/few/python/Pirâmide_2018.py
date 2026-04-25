import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    matrix = []
    idx = 1
    for i in range(N):
        row = list(map(int, data[idx:idx + N]))
        matrix.append(row)
        idx += N

    # dp[i][j] = mínimo peso de pirâmide que termina na coluna j da linha i
    dp = [[float('inf')] * N for _ in range(N)]

    # linha 1 (topo): apenas 1 caixa consecutiva
    for j in range(N):
        dp[0][j] = matrix[0][j]

    # linha i: precisa i caixas consecutivas, a coluna final j deve satisfazer j >= i-1 (pois precisa i caixas)
    for i in range(1, N):
        for j in range(i - 1, N):
            # última caixa da linha i é coluna j, então o bloco vai de j-(i-1) até j
            peso_bloco = sum(matrix[i][j-(i-1):j+1])
            # olha todas posições possíveis na linha anterior que podem sustentar esse bloco
            # a linha i-1 tem i-1 caixas consecutivas, terminando em coluna k
            # condição de compatibilidade: a coluna final da linha i-1 deve estar dentro do intervalo
            # [j-(i-1), j] pois a caixa abaixo de cada caixa da linha i deve estar na linha i-1
            # mais precisamente: o intervalo de caixas na linha i-1 deve ser [k-(i-2), k]
            # ele deve estar totalmente dentro de [j-(i-1), j]
            # isso é equivalente a k-(i-2) >= j-(i-1) e k <= j
            # simplificando: k >= j-1  e k <= j
            for k in range(max(j-1, i-2), min(j, N-1)+1):
                if k >= i-2:  # linha i-1 precisa ter i-1 caixas, então k >= i-2
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + peso_bloco)

    ans = min(dp[N-1])
    print(ans)

if __name__ == "__main__":
    solve()