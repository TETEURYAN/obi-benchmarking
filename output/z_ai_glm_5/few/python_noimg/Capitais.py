import sys
from collections import deque

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

    # Grafo e grau dos vértices
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)

    # Leitura das arestas
    for _ in range(n - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Identificar capitais (folhas)
    capitals = []
    for i in range(1, n + 1):
        if degree[i] == 1:
            capitals.append(i)

    # Caso especial: N=2, ambas são capitais, distância é 1
    if n == 2:
        print(1)
        return

    # BFS Multisource para encontrar a menor distância entre pares de capitais
    # Queue armazena (vértice, fonte)
    q = deque()
    dist = [-1] * (n + 1)
    source = [-1] * (n + 1)

    for c in capitals:
        q.append(c)
        dist[c] = 0
        source[c] = c

    while q:
        u = q.popleft()
        
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                source[v] = source[u]
                q.append(v)
            else:
                # Se o vizinho já foi visitado e tem fonte diferente, encontramos um caminho
                if source[u] != source[v]:
                    print(dist[u] + dist[v] + 1)
                    return

if __name__ == '__main__':
    solve()