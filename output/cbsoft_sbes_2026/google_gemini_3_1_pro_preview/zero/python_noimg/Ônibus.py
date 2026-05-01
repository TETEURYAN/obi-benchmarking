import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = int(input_data[1])
    B = int(input_data[2])
    
    adj = [[] for _ in range(N + 1)]
    
    idx = 3
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    queue = deque([(A, 0)])
    visited = [False] * (N + 1)
    visited[A] = True
    
    while queue:
        curr, dist = queue.popleft()
        
        if curr == B:
            print(dist)
            return
            
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))

if __name__ == '__main__':
    solve()