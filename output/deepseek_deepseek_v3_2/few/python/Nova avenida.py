import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    
    grid = []
    for _ in range(N):
        row = [int(next(it)) for _ in range(M)]
        grid.append(row)
    
    # Calcula soma de cada coluna
    col_sums = [0] * M
    for c in range(M):
        s = 0
        for r in range(N):
            s += grid[r][c]
        col_sums[c] = s
    
    # Para cada possível rua Norte-Sul entre as colunas j-1 e j,
    # o custo é a soma das colunas à esquerda OU à direita.
    # Queremos o mínimo entre todas as possibilidades.
    # A rua pode ser entre qualquer par de colunas adjacentes,
    # ou seja, há M-1 posições possíveis para a rua.
    # Para cada posição k (entre coluna k e k+1, 0-indexado),
    # custo_esquerda = soma das colunas 0..k
    # custo_direita  = soma das colunas k+1..M-1
    # Queremos min(custo_esquerda, custo_direita) para cada k,
    # e depois o mínimo global.
    
    total = sum(col_sums)
    best = total  # pior caso: desapropriar tudo
    left_sum = 0
    for k in range(M - 1):
        left_sum += col_sums[k]
        right_sum = total - left_sum
        current_best = min(left_sum, right_sum)
        if current_best < best:
            best = current_best
    
    print(best)

if __name__ == "__main__":
    main()