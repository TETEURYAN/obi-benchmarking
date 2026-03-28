import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    S = int(data[idx]); idx+=1
    T = int(data[idx]); idx+=1
    P = int(data[idx]); idx+=1
    
    A = [0] * (S+1)
    for i in range(1, S+1):
        A[i] = int(data[idx]); idx+=1
    
    adj = [[] for _ in range(S+1)]
    for _ in range(T):
        I = int(data[idx]); idx+=1
        J = int(data[idx]); idx+=1
        # Can slide from I to J if A[I] > A[J]
        if A[I] > A[J]:
            adj[I].append(J)
        elif A[J] > A[I]:
            adj[J].append(I)
        # If equal, no sliding possible
    
    # BFS/DFS from P, count reachable nodes (not counting P itself)
    visited = [False] * (S+1)
    visited[P] = True
    queue = deque([P])
    count = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)
    
    print(count)

main()