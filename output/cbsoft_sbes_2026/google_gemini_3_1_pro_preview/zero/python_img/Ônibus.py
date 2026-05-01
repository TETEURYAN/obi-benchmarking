import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = int(input_data[1])
    b = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    
    idx = 3
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    queue = deque([(a, 0)])
    visited = [False] * (n + 1)
    visited[a] = True
    
    while queue:
        curr, dist = queue.popleft()
        
        if curr == b:
            print(dist)
            return
            
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))

if __name__ == '__main__':
    main()