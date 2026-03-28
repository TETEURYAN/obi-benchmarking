import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    E = int(next(it))
    S = int(next(it))
    M = int(next(it))
    
    # Grafo: adj[u] = lista de (v, tipo)
    adj = [[] for _ in range(N)]
    for _ in range(M):
        A = int(next(it))
        B = int(next(it))
        T = int(next(it))
        adj[A].append((B, T))
    
    # dist[u][t] = menor tempo para chegar em u no tempo t mod 3
    INF = 10**18
    dist = [[INF] * 3 for _ in range(N)]
    dist[E][0] = 0  # começa em E no tempo 0 (meio-dia)
    
    # Dijkstra modificado: estado = (tempo_total, u, tempo_mod)
    pq = [(0, E, 0)]
    while pq:
        d, u, mod = heapq.heappop(pq)
        if d > dist[u][mod]:
            continue
        if u == S:
            print(d)
            return
        
        # Para cada aresta (u -> v) com tipo T
        for v, tipo in adj[u]:
            # Verifica se pode passar no tempo atual
            # tipo 1: abre nos múltiplos de 3 -> pode passar se mod == 0
            # tipo 0: fecha nos múltiplos de 3 -> pode passar se mod != 0
            if (tipo == 1 and mod == 0) or (tipo == 0 and mod != 0):
                nd = d + 1
                nmod = (mod + 1) % 3
                if nd < dist[v][nmod]:
                    dist[v][nmod] = nd
                    heapq.heappush(pq, (nd, v, nmod))
            else:
                # Espera até poder passar
                # Encontra o menor k >= 0 tal que no tempo d+k o semáforo permite passagem
                # mod(d+k) = (mod + k) % 3
                # Queremos (tipo==1 e (mod+k)%3==0) ou (tipo==0 e (mod+k)%3!=0)
                for k in range(3):
                    nd = d + k
                    nmod = (mod + k) % 3
                    if (tipo == 1 and nmod == 0) or (tipo == 0 and nmod != 0):
                        nd += 1  # mais um minuto para atravessar
                        nmod = (nmod + 1) % 3
                        if nd < dist[v][nmod]:
                            dist[v][nmod] = nd
                            heapq.heappush(pq, (nd, v, nmod))
                        break
    
    print('*')

if __name__ == "__main__":
    main()