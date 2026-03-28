import sys
sys.setrecursionlimit(2000000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    M = int(next(it))
    grid = []
    for _ in range(M):
        grid.append(list(next(it)))
    A = int(next(it))
    B = int(next(it))
    
    # Encontrar a posição do tesouro
    treasure = None
    for i in range(M):
        for j in range(M):
            if grid[i][j] == 'X':
                treasure = (i, j)
                break
        if treasure:
            break
    
    # Mapear direções para deslocamentos (linha, coluna)
    dir_map = {
        'N': (-1, 0),
        'S': (1, 0),
        'L': (0, 1),  # Leste é direita (coluna +1)
        'O': (0, -1)  # Oeste é esquerda (coluna -1)
    }
    
    # Inicializar estruturas para DFS/BFS
    visited = [[-1] * M for _ in range(M)]  # -1 = não visitado, >=0 = tempo de chegada
    in_stack = [[False] * M for _ in range(M)]
    
    # Converter para índices 0-based
    start = (A-1, B-1)
    tr_i, tr_j = treasure
    
    # Função DFS para detectar ciclos e calcular tempos
    def dfs(i, j, time):
        # Se sair da grade
        if i < 0 or i >= M or j < 0 or j >= M:
            return -1
        
        # Se chegou ao tesouro
        if (i, j) == (tr_i, tr_j):
            visited[i][j] = time
            return time
        
        # Se já visitado e sabemos o resultado
        if visited[i][j] != -1:
            return visited[i][j]
        
        # Se detectamos um ciclo (já está na pilha de recursão)
        if in_stack[i][j]:
            # Estamos em um ciclo que não leva ao tesouro
            return 0
        
        in_stack[i][j] = True
        
        # Obter próxima posição
        cell = grid[i][j]
        di, dj = dir_map[cell]
        ni, nj = i + di, j + dj
        
        result = dfs(ni, nj, time + 1)
        
        # Armazenar resultado
        if result > 0:
            visited[i][j] = result - (time + 1) + time
        else:
            visited[i][j] = result
        
        in_stack[i][j] = False
        return visited[i][j]
    
    # Executar DFS a partir do ponto inicial
    answer = dfs(start[0], start[1], 0)
    
    # Ajustar resposta conforme especificação
    if answer > 0:
        print(answer)
    else:
        print(answer)

if __name__ == "__main__":
    main()