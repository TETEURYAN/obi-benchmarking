import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    grid = []
    for _ in range(N):
        row = [int(next(it)) for _ in range(N)]
        grid.append(row)
    
    # Verifica se todos os números de 1 a N² estão presentes (condição do quadrado mágico clássico)
    # Mas como os valores podem ser até 1e9 e N até 1000, N² pode ser 1e6, então podemos usar um set
    # No entanto, o problema não exige explicitamente que os números sejam de 1 a N², apenas que a soma das linhas/colunas/diagonais seja igual.
    # Pelos exemplos, o primeiro teste tem todos 1 e deve retornar 0, então a verificação de unicidade e intervalo não é necessária.
    # Vamos apenas verificar as somas.
    
    # Calcula a soma da primeira linha como referência
    target = sum(grid[0])
    
    # Verifica todas as linhas
    for i in range(N):
        if sum(grid[i]) != target:
            print(0)
            return
    
    # Verifica todas as colunas
    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += grid[i][j]
        if col_sum != target:
            print(0)
            return
    
    # Verifica diagonal principal
    diag_sum = 0
    for i in range(N):
        diag_sum += grid[i][i]
    if diag_sum != target:
        print(0)
        return
    
    # Verifica diagonal secundária
    diag2_sum = 0
    for i in range(N):
        diag2_sum += grid[i][N-1-i]
    if diag2_sum != target:
        print(0)
        return
    
    print(target)

if __name__ == "__main__":
    main()