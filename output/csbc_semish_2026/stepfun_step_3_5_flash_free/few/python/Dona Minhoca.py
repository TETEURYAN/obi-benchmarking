import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a = int(next(it)); b = int(next(it))
        adj[a].append(b)
        adj[b].append(a)
    
    # BFS para obter pais e ordem
    pai = [0] * (N+1)
    ordem = []
    q = deque([1])
    pai[1] = 0
    while q:
        v = q.popleft()
        ordem.append(v)
        for u in adj[v]:
            if u == pai[v]:
                continue
            pai[u] = v
            q.append(u)
    ordem_rev = ordem[::-1]
    
    INF = 10**9
    
    def can_cover(R):
        min_dist = [INF] * (N+1)
        max_need = [-1] * (N+1)
        contador = 0
        for v in ordem_rev:
            # Calcular min_dist a partir dos filhos
            for u in adj[v]:
                if u == pai[v]:
                    continue
                if min_dist[u] + 1 < min_dist[v]:
                    min_dist[v] = min_dist[u] + 1
            # Determinar estado de cobertura de v
            if min_dist[v] <= R:
                max_need_temp = -1
            else:
                max_need_temp = 0
            # Incorporar max_need dos filhos
            for u in adj[v]:
                if u == pai[v]:
                    continue
                if max_need[u] != -1:
                    cand = max_need[u] + 1
                    if max_need_temp == -1:
                        max_need_temp = cand
                    elif cand > max_need_temp:
                        max_need_temp = cand
            max_need[v] = max_need_temp
            # Verificar condições
            if max_need[v] > R:
                return False
            if max_need[v] == R:
                contador += 1
                min_dist[v] = 0
                max_need[v] = -1
        if max_need[1] >= 0:
            contador += 1
        return contador <= K
    
    low, high = 0, N
    while low < high:
        mid = (low + high) // 2
        if can_cover(mid):
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    main()