
import sys
from collections import deque

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def build_graph(n):
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = read_ints()
        graph[x].append(y)
        graph[y].append(x)
    return graph

def farthest_node(graph, start, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest = start
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if dist[v] > dist[farthest]:
                    farthest = v
                q.append(v)
    return farthest, dist

def find_center(graph, n):
    if n == 1:
        return 1
    u, _ = farthest_node(graph, 1, n)
    v, dist_u = farthest_node(graph, u, n)
    _, dist_v = farthest_node(graph, v, n)
    
    diameter = dist_u[v]
    mid = diameter // 2
    
    current = v
    for _ in range(diameter - mid):
        for nei in graph[current]:
            if dist_u[nei] == dist_u[current] - 1:
                current = nei
                break
    center1 = current
    
    if diameter % 2 == 0:
        return center1
    for nei in graph[center1]:
        if dist_u[nei] == dist_u[center1] + 1 and dist_v[nei] == dist_v[center1] - 1:
            return nei
    return center1

def main():
    test = 1
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        if n == 0:
            continue
        graph = build_graph(n)
        center = find_center(graph, n)
        print(f"Teste {test}")
        print(center)
        print()
        test += 1

if __name__ == "__main__":
    main()
