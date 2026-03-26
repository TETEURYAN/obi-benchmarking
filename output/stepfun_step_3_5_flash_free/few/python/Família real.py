import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    parents = [int(next(it)) for _ in range(N)]
    participants = [int(next(it)) for _ in range(M)]
    
    adj = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        p = parents[i-1]
        adj[p].append(i)
    
    geracao = [-1] * (N+1)
    geracao[0] = 0
    fila = deque([0])
    while fila:
        u = fila.popleft()
        for v in adj[u]:
            if geracao[v] == -1:
                geracao[v] = geracao[u] + 1
                fila.append(v)
    
    total = [0] * (N+1)
    compareceu = [0] * (N+1)
    present_set = set(participants)
    for i in range(1, N+1):
        k = geracao[i]
        total[k] += 1
        if i in present_set:
            compareceu[k] += 1
    
    max_geracao = max(geracao[1:]) if N >= 1 else 0
    resultados = []
    for k in range(1, max_geracao+1):
        pct = compareceu[k] / total[k] * 100.0
        resultados.append("{:.2f}".format(pct))
    
    print(" ".join(resultados))

if __name__ == "__main__":
    main()