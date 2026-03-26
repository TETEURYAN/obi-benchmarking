import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj = [[] for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        p = int(input_data[i + 1])
        adj[p].append(i)
        
    attendees = [False] * (N + 1)
    for i in range(M):
        attendees[int(input_data[N + 2 + i])] = True
        
    gen = [0] * (N + 1)
    q = deque([0])
    
    max_g = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            gen[v] = gen[u] + 1
            if gen[v] > max_g:
                max_g = gen[v]
            q.append(v)
            
    total_gen = [0] * (max_g + 1)
    attend_gen = [0] * (max_g + 1)
    
    for i in range(1, N + 1):
        g = gen[i]
        total_gen[g] += 1
        if attendees[i]:
            attend_gen[g] += 1
            
    res = []
    for g in range(1, max_g + 1):
        pct = (attend_gen[g] / total_gen[g]) * 100.0
        res.append(f"{pct:.2f}")
        
    print(" ".join(res))

if __name__ == '__main__':
    solve()