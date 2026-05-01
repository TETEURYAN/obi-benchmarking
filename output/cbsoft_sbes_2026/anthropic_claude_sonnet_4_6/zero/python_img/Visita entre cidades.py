import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    A = int(input_data[idx]); idx+=1
    B = int(input_data[idx]); idx+=1
    
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        P = int(input_data[idx]); idx+=1
        Q = int(input_data[idx]); idx+=1
        D = int(input_data[idx]); idx+=1
        graph[P].append((Q, D))
        graph[Q].append((P, D))
    
    # BFS/DFS to find distance from A to B
    dist = [-1] * (N+1)
    dist[A] = 0
    queue = deque([A])
    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + weight
                queue.append(neighbor)
    
    print(dist[B])

main()