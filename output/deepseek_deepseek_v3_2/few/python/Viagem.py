import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    V = int(next(it))
    N = int(next(it))
    M = int(next(it))
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        a = int(next(it))
        b = int(next(it))
        t = int(next(it))
        p = int(next(it))
        adj[a].append((b, t, p))
        adj[b].append((a, t, p))
    
    X = int(next(it))
    Y = int(next(it))
    
    INF = 10**18
    dist = [[INF] * (V + 1) for _ in range(N + 1)]
    dist[X][0] = 0
    
    import heapq
    heap = []
    heapq.heappush(heap, (0, X, 0))  # (tempo, ilha, custo_acumulado)
    
    while heap:
        tempo_atual, ilha, custo_atual = heapq.heappop(heap)
        if tempo_atual > dist[ilha][custo_atual]:
            continue
        if ilha == Y:
            print(tempo_atual)
            return
        
        for viz, t, p in adj[ilha]:
            novo_custo = custo_atual + p
            if novo_custo > V:
                continue
            novo_tempo = tempo_atual + t
            if novo_tempo < dist[viz][novo_custo]:
                for c in range(novo_custo, V + 1):
                    if dist[viz][c] <= novo_tempo:
                        break
                    dist[viz][c] = novo_tempo
                heapq.heappush(heap, (novo_tempo, viz, novo_custo))
    
    print(-1)

if __name__ == "__main__":
    solve()