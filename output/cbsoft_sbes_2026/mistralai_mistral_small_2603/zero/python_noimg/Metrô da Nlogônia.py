
import sys
from collections import deque

def bfs(start, graph):
    dist = [-1] * len(graph)
    q = deque()
    q.append(start)
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    max_dist = max(dist)
    farthest_node = dist.index(max_dist)
    return farthest_node, max_dist

def find_diameter_and_center(graph, n):
    node, _ = bfs(0, graph)
    farthest, diameter = bfs(node, graph)
    center = farthest
    for _ in range(diameter // 2):
        for neighbor in graph[center]:
            if bfs(neighbor, graph)[1] < diameter:
                center = neighbor
                break
    return diameter, center

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, M = int(input[ptr]), int(input[ptr+1])
    ptr += 2

    circle_graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        circle_graph[a].append(b)
        circle_graph[b].append(a)

    square_graph = [[] for _ in range(M+1)]
    for _ in range(M-1):
        x, y = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        square_graph[x].append(y)
        square_graph[y].append(x)

    d1, c1 = find_diameter_and_center(circle_graph, N)
    d2, c2 = find_diameter_and_center(square_graph, M)

    min_diameter = float('inf')
    best_pair = (1, 1)

    for u in circle_graph[c1]:
        for v in square_graph[c2]:
            new_d1 = (d1 + 1) // 2
            new_d2 = (d2 + 1) // 2
            current_diameter = max(new_d1, new_d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
            if current_diameter < min_diameter:
                min_diameter = current_diameter
                best_pair = (u, v)

    print(f"{best_pair[0]} {best_pair[1]}")

if __name__ == "__main__":
    main()
