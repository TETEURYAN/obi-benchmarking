import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    K = int(next(it))
    
    grid = []
    for _ in range(L):
        row = [int(next(it)) for _ in range(C)]
        grid.append(row)
    
    # BFS com estados (linha, coluna, tempo_mod_K)
    from collections import deque
    INF = 10**18
    dist = [[[INF] * K for _ in range(C)] for __ in range(L)]
    
    start_state = (0, 0, 0)
    dist[0][0][0] = 0
    dq = deque([start_state])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while dq:
        r, c, t_mod = dq.popleft()
        current_dist = dist[r][c][t_mod]
        
        # Chegou no destino?
        if r == L-1 and c == C-1:
            print(current_dist)
            return
        
        # Movimentos para salas vizinhas
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < L and 0 <= nc < C:
                next_time = current_dist + 1
                next_mod = next_time % K
                # Verifica se pode entrar na sala (nr, nc) no tempo next_time
                if grid[nr][nc] == -1:
                    # Relógio funcionando: sempre mostra hora certa
                    if dist[nr][nc][next_mod] > next_time:
                        dist[nr][nc][next_mod] = next_time
                        dq.append((nr, nc, next_mod))
                else:
                    # Relógio parado: só pode entrar se next_mod == grid[nr][nc]
                    if next_mod == grid[nr][nc] and dist[nr][nc][next_mod] > next_time:
                        dist[nr][nc][next_mod] = next_time
                        dq.append((nr, nc, next_mod))
        
        # Esperar na sala atual (apenas se o relógio estiver funcionando)
        if grid[r][c] == -1:
            next_time = current_dist + 1
            next_mod = next_time % K
            if dist[r][c][next_mod] > next_time:
                dist[r][c][next_mod] = next_time
                dq.append((r, c, next_mod))
    
    # Não encontrou caminho
    print(-1)

if __name__ == "__main__":
    solve()