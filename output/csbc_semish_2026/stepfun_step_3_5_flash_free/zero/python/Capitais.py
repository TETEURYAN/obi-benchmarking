
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    if n == 2:
        # Ler a única aresta e ignorar
        next(it); next(it)
        print(1)
        return

    grafo = [[] for _ in range(n+1)]
    grau = [0] * (n+1)
    for _ in range(n-1):
        u = int(next(it)); v = int(next(it))
        grafo[u].append(v)
        grafo[v].append(u)
        grau[u] += 1
        grau[v] += 1

    raiz = 1
    pai = [0] * (n+1)
    filhos = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    queue = deque([raiz])
    visited[raiz] = True
    while queue:
        v = queue.popleft()
        for w in grafo[v]:
            if not visited[w]:
                visited[w] = True
                pai[w] = v
                filhos[v].append(w)
                queue.append(w)

    # Ordem DFS pré-ordem
    pilha = [raiz]
    ordem = []
    while pilha:
        v = pilha.pop()
        ordem.append(v)
        for w in filhos[v]:
            pilha.append(w)

    INF = 10**9
    d_down = [INF] * (n+1)
    for v in reversed(ordem):
        if grau[v] == 1:
            d_down[v] = 0
        else:
            for w in filhos[v]:
                if 1 + d_down[w] < d_down[v]:
                    d_down[v] = 1 + d_down[w]

    best1 = [INF] * (n+1)
    best2 = [INF] * (n+1)
    argmin1 = [0] * (n+1)
    for v in range(1, n+1):
        for w in filhos[v]:
            val = 1 + d_down[w]
            if val < best1[v]:
                best2[v] = best1[v]
                best1[v] = val
                argmin1[v] = w
            elif val < best2[v]:
                best2[v] = val

    d_up = [INF] * (n+1)
    d_up[raiz] = INF
    for v in ordem:
        for w in filhos[v]:
            if w == argmin1[v]:
                use = best2[v]
            else:
                use = best1[v]
            opcoes = []
            if d_up[v] < INF:
                opcoes.append(d_up[v])
            if use < INF:
                opcoes.append(use)
            if grau[v] == 1:
                opcoes.append(0)
            if opcoes:
                d_up[w] = 1 + min(opcoes)
            else:
                d_up[w] = INF

    ans = 10**18
    for v in range(1, n+1):
        if grau[v] >= 2:
            dists = []
            for w in filhos[v]:
                dists.append(1 + d_down[w])
            if v != raiz:
                dists.append(d_up[v])
            if len(dists) >= 2:
                dists.sort()
                candidato = dists[0] + dists[1]
                if candidato < ans:
                    ans = candidato
    print(ans)

if __name__ == "__main__":
    main()
