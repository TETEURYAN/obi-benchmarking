from collections import deque
import sys
input = sys.stdin.readline

def main():
    line = sys.stdin.readline().split()
    N, A, B = int(line[0]), int(line[1]), int(line[2])
    
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        p, q = map(int, sys.stdin.readline().split())
        graph[p].append(q)
        graph[q].append(p)
    
    # BFS from A to B
    dist = [-1] * (N + 1)
    dist[A] = 0
    queue = deque([A])
    
    while queue:
        node = queue.popleft()
        if node == B:
            break
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    print(dist[B])

main()