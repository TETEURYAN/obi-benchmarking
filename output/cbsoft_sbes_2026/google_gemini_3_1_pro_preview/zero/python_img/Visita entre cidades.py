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
        P = int(input_data[idx])
        Q = int(input_data[idx+1])
        D = int(input_data[idx+2])
        idx += 3
        adj[P].append((Q, D))
        adj[Q].append((P, D))
        
    queue = deque([(A, 0)])
    visited = [False] * (N + 1)
    visited[A] = True
    
    while queue:
        curr, dist = queue.popleft()
        
        if curr == B:
            print(dist)
            return
            
        for nxt, d in adj[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, dist + d))

if __name__ == '__main__':
    solve()