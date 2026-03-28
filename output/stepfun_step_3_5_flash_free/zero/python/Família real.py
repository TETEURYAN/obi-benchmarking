
import sys
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    pais = [int(next(it)) for _ in range(N)]
    participantes = [int(next(it)) for _ in range(M)]
    
    children = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        p = pais[i - 1]
        children[p].append(i)
    
    dist = [-1] * (N + 1)
    dist[0] = 0
    fila = deque([0])
    while fila:
        u = fila.popleft()
        for v in children[u]:
            dist[v] = dist[u] + 1
            fila.append(v)
    
    max_geracao = max(dist[1:])
    total = [0] * (max_geracao + 1)
    participantes_count = [0] * (max_geracao + 1)
    
    participantes_set = set(participantes)
    
    for i in range(1, N + 1):
        g = dist[i]
        total[g] += 1
        if i in participantes_set:
            participantes_count[g] += 1
    
    resultados = []
    for g in range(1, max_geracao + 1):
        pct = (participantes_count[g] / total[g]) * 100
        resultados.append(f"{pct:.2f}")
    
    print(' '.join(resultados))

if __name__ == "__main__":
    main()
