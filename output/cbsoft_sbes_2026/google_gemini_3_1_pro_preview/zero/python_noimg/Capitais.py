
import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    
    adj = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    
    idx = 1
    for _ in range(N - 1):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
        
    queue = deque()
    dist = [-1] * (N + 1)
    source = [-1] * (N + 1)
    
    for i in range(1, N + 1):
        if degree[i] == 1:
            queue.append(i)
            dist[i] = 0
            source[i] = i
            
    ans = float('inf')
    
    while queue:
        u = queue.popleft()
        
        if dist[u] * 2 + 1 >= ans:
            break
            
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                source[v] = source[u]
                queue.append(v)
            elif source[v] != source[u]:
                ans = min(ans, dist[u] + dist[v] + 1)
                
    print(ans)

if __name__ == '__main__':
    solve()
