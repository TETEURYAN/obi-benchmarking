import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    A = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        P = int(input_data[idx]); idx += 1
        Q = int(input_data[idx]); idx += 1
        adj[P].append(Q)
        adj[Q].append(P)
    
    # BFS from A to B
    dist = [-1] * (N + 1)
    dist[A] = 0
    queue = deque([A])
    
    while queue:
        node = queue.popleft()
        if node == B:
            break
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    print(dist[B])

main()