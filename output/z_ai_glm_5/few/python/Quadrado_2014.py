import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    # Leitura da grade
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(next(iterator)))
        grid.append(row)

    # Cálculo das somas das linhas
    row_sums = [sum(row) for row in grid]
    
    # Cálculo das somas das colunas
    col_sums = []
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += grid[i][j]
        col_sums.append(col_sum)

    # Função para encontrar o índice do elemento único (diferente da maioria)
    # Como N >= 3, a maioria é sempre definida pelos dois primeiros elementos se forem iguais,
    # ou pelo terceiro se os dois primeiros forem diferentes.
    def find_unique_index(sums):
        if sums[0] != sums[1]:
            # sums[0] ou sums[1] é o único diferente. 
            # Se sums[0] == sums[2], então sums[1] é o único. Caso contrário, sums[0] é o único.
            if sums[0] == sums[2]:
                return 1
            else:
                return 0
        else:
            # sums[0] == sums[1], então a maioria é sums[0].
            majority_val = sums[0]
            for i in range(2, len(sums)):
                if sums[i] != majority_val:
                    return i
        return -1 # Caso não encontre (não deve acontecer pelo enunciado)

    r_idx = find_unique_index(row_sums)
    c_idx = find_unique_index(col_sums)

    # Determinar o valor M (soma correta)
    # M é a soma de qualquer linha/coluna que não seja a alterada
    if r_idx == 0:
        M = row_sums[1]
    else:
        M = row_sums[0]
        
    # Calcular a diferença
    # S_alterada = M + (y - x) => diff = y - x
    diff = row_sums[r_idx] - M
    
    # y é o valor atual na posição alterada
    y = grid[r_idx][c_idx]
    
    # x é o valor original
    x = y - diff
    
    print(x, y)

if __name__ == '__main__':
    solve()