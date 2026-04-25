import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    N = int(data[0])
    M = int(data[1])
    grid = [list(data[i]) for i in range(2, 2 + N)]

    # Encontra o ponto de vazamento inicial (o único 'o' na primeira linha)
    leak_row = 0
    leak_col = -1
    for j in range(M):
        if grid[0][j] == 'o':
            leak_col = j
            break

    # Usamos uma pilha para simular o fluxo da água
    stack = [(leak_row, leak_col)]
    visited = set()
    visited.add((leak_row, leak_col))

    while stack:
        row, col = stack.pop()

        # Regra 1: água escorre verticalmente abaixo se não há prateleira
        # (prateleira é '#')
        if row + 1 < N and grid[row + 1][col] != '#':
            if (row + 1, col) not in visited:
                visited.add((row + 1, col))
                stack.append((row + 1, col))

        # Regra 2: água escorre horizontalmente para a esquerda se há prateleira abaixo-esquerda
        if col - 1 >= 0 and grid[row][col - 1] == '.':
            if row + 1 < N and grid[row + 1][col - 1] == '#':
                if (row, col - 1) not in visited:
                    visited.add((row, col - 1))
                    stack.append((row, col - 1))

        # Regra 3: água escorre horizontalmente para a direita se há prateleira abaixo-direita
        if col + 1 < M and grid[row][col + 1] == '.':
            if row + 1 < N and grid[row + 1][col + 1] == '#':
                if (row, col + 1) not in visited:
                    visited.add((row, col + 1))
                    stack.append((row, col + 1))

    # Atualiza a matriz com os pontos molhados
    for (r, c) in visited:
        if grid[r][c] == '.':
            grid[r][c] = 'o'

    # Imprime o resultado
    for row in grid:
        print(''.join(row))

if __name__ == '__main__':
    main()