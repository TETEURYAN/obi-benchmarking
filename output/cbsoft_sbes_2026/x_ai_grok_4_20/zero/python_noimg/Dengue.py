
import sys
from collections import deque

def bfs_dist(graph, start, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def find_farthest(graph, start, n):
    dist = bfs_dist(graph, start, n)
    max_d = 0
    far = start
    for i in range(1, n + 1):
        if dist[i] > max_d:
            max_d = dist[i]
            far = i
    return far, max_d

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    test_num = 1
    while True:
        N = int(data[index])
        index += 1
        if N == 0:
            break
        if N == 1:
            print(f"Teste {test_num}")
            print(1)
            print()
            test_num += 1
            continue
        graph = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            graph[x].append(y)
            graph[y].append(x)
        
        # Encontrar um extremo da árvore
        a, _ = find_farthest(graph, 1, N)
        # Encontrar o outro extremo
        b, diameter = find_farthest(graph, a, N)
        
        # O centro está no meio do diâmetro
        if diameter % 2 == 0:
            # Dois centros possíveis, precisamos escolher o que minimiza o max dist
            # Mas como é árvore, ambos têm o mesmo ecc
            # Vamos pegar o primeiro no caminho de a para b
            # Para encontrar um dos centros, fazemos BFS de a até b
            parent = [-1] * (N + 1)
            dist = [-1] * (N + 1)
            dist[a] = 0
            q = deque([a])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
            # Reconstruir caminho de b até a
            path = []
            current = b
            while current != -1:
                path.append(current)
                current = parent[current]
            path = path[::-1]  # de a até b
            center1 = path[diameter // 2]
            print(f"Teste {test_num}")
            print(center1)
            print()
        else:
            # Um centro
            parent = [-1] * (N + 1)
            dist = [-1] * (N + 1)
            dist[a] = 0
            q = deque([a])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
            path = []
            current = b
            while current != -1:
                path.append(current)
                current = parent[current]
            path = path[::-1]
            center = path[diameter // 2]
            print(f"Teste {test_num}")
            print(center)
            print()
        test_num += 1

if __name__ == "__main__":
    main()
