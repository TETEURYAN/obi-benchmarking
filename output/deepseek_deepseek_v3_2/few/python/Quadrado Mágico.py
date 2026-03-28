import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = []
    zero_i = zero_j = -1
    for i in range(n):
        row = []
        for j in range(n):
            val = int(next(it))
            row.append(val)
            if val == 0:
                zero_i, zero_j = i, j
        grid.append(row)

    # Encontrar a soma mágica usando uma linha completa
    magic_sum = None
    for i in range(n):
        if 0 not in grid[i]:
            magic_sum = sum(grid[i])
            break
    if magic_sum is None:
        # Se todas as linhas têm zero, usa uma coluna completa
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            if 0 not in col:
                magic_sum = sum(col)
                break

    # Calcular o valor faltante
    row_sum = sum(grid[zero_i])
    missing_val = magic_sum - row_sum

    # Verificar se o valor é válido (não negativo)
    if missing_val < 0:
        # Se der negativo, tenta usar a coluna
        col_sum = sum(grid[i][zero_j] for i in range(n))
        missing_val = magic_sum - col_sum

    print(missing_val)
    print(zero_i + 1)
    print(zero_j + 1)

if __name__ == "__main__":
    main()