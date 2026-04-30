
import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    if N == 2:
        print(1)
        return

    # Encontrar um nó folha (grau 1)
    start = 1
    while len(adj[start]) != 1:
        start += 1

    # BFS para encontrar o nó mais distante (diâmetro)
    parent = [0] * (N+1)
    q = deque()
    q.append(start)
    parent[start] = -1
    last_node = start

    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                q.append(v)
                last_node = v

    # BFS do último nó para encontrar o outro extremo do diâmetro
    parent = [0] * (N+1)
    q.append(last_node)
    parent[last_node] = -1
    last_node2 = last_node

    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                q.append(v)
                last_node2 = v

    # Reconstruir o caminho do diâmetro
    path = []
    current = last_node2
    while current != -1:
        path.append(current)
        current = parent[current]

    # A menor distância entre capitais é o comprimento do caminho do diâmetro
    print(len(path) - 1)

if __name__ == "__main__":
    main()
