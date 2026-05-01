import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    adj = [[] for _ in range(n+1)]
    adj_rev = [[] for _ in range(n+1)]
    idx = 1
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        adj[a].append(b)
        adj_rev[b].append(a)
    
    def bfs(grafo, inicio):
        visitados = [False] * (n+1)
        fila = deque([inicio])
        visitados[inicio] = True
        count = 1
        while fila:
            u = fila.popleft()
            for v in grafo[u]:
                if not visitados[v]:
                    visitados[v] = True
                    count += 1
                    fila.append(v)
        return count
    
    if bfs(adj, 1) != n or bfs(adj_rev, 1) != n:
        print('N')
    else:
        print('S')

if __name__ == "__main__":
    main()