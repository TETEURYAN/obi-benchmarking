
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K1 = int(input_data[1])
    K2 = int(input_data[2])
    P = int(input_data[3])
    
    adj_metro = [[] for _ in range(N + 1)]
    adj_bus = [[] for _ in range(N + 1)]
    
    idx = 4
    for _ in range(K1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj_metro[u].append(v)
        adj_metro[v].append(u)
        idx += 2
        
    for _ in range(K2):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj_bus[u].append(v)
        adj_bus[v].append(u)
        idx += 2
        
    A = int(input_data[idx])
    B = int(input_data[idx+1])
    
    if A == B:
        print(0)
        return
        
    dist = [float('inf')] * (2 * N + 1)
    visited = [False] * (2 * N + 1)
    
    dq = deque()
    
    dist[A] = 1
    dist[A + N] = 1
    dq.append(A)
    dq.append(A + N)
    
    while dq:
        u = dq.popleft()
        
        if visited[u]:
            continue
        visited[u] = True
        
        if u <= N:
            station = u
            for v in adj_metro[station]:
                if dist[v] > dist[u]:
                    dist[v] = dist[u]
                    dq.appendleft(v)
            if dist[station + N] > dist[u] + 1:
                dist[station + N] = dist[u] + 1
                dq.append(station + N)
        else:
            station = u - N
            for v in adj_bus[station]:
                if dist[v + N] > dist[u]:
                    dist[v + N] = dist[u]
                    dq.appendleft(v + N)
            if dist[station] > dist[u] + 1:
                dist[station] = dist[u] + 1
                dq.append(station)
                
    ans = min(dist[B], dist[B + N])
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans * P)

if __name__ == '__main__':
    solve()
