
from collections import deque

def main():
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # BFS com prioridade (0-1 BFS) para encontrar caminho com mínimo de blocos
    # dist[i][j] = número mínimo de blocos passados para chegar em (i,j)
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = grid[0][0]  # Começa no (0,0), mas o problema diz que nunca está bloqueado
    
    # Usando deque para 0-1 BFS: se mover para célula livre (0) -> adiciona no início
    # se mover para célula bloqueada (1) -> adiciona no final
    dq = deque()
    dq.append((0, 0))
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while dq:
        x, y = dq.popleft()
        
        # Se chegamos no destino, podemos parar (BFS garante menor número de blocos)
        if x == n-1 and y == n-1:
            break
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                # Custo para chegar ao vizinho: custo atual + valor da célula vizinha
                novo_custo = dist[x][y] + grid[nx][ny]
                if novo_custo < dist[nx][ny]:
                    dist[nx][ny] = novo_custo
                    if grid[nx][ny] == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))
    
    # O problema diz que o quadrado inicial e final nunca estão bloqueados
    # então dist[n-1][n-1] já tem o número mínimo de blocos passados
    print(dist[n-1][n-1])

if __name__ == "__main__":
    main()
