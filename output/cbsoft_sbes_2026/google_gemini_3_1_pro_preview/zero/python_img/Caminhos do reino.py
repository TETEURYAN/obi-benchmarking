
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = int(input_data[i])
        
    Q = int(input_data[N + 1])
    queries = []
    idx = N + 2
    for _ in range(Q):
        queries.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
        
    visited = [0] * (N + 1)
    curr = 1
    while visited[curr] == 0:
        visited[curr] = 1
        curr = F[curr]
        
    cycle_nodes = []
    cycle_start = curr
    while True:
        cycle_nodes.append(curr)
        curr = F[curr]
        if curr == cycle_start:
            break
            
    C = len(cycle_nodes)
    pos = [0] * (N + 1)
    in_cycle = [False] * (N + 1)
    for i, node in enumerate(cycle_nodes):
        pos[node] = i
        in_cycle[node] = True
        
    rev_F = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        rev_F[F[i]].append(i)
        
    d = [0] * (N + 1)
    r = [0] * (N + 1)
    queue = deque()
    
    for node in cycle_nodes:
        d[node] = 0
        r[node] = node
        queue.append(node)
        
    while queue:
        u = queue.popleft()
        for prev in rev_F[u]:
            if not in_cycle[prev]:
                d[prev] = d[u] + 1
                r[prev] = r[u]
                queue.append(prev)
                
    out = []
    for A, B in queries:
        if r[A] == r[B]:
            ans = d[A] - d[B]
            if ans < 0:
                ans = -ans
        else:
            L = (pos[r[B]] - pos[r[A]]) % C
            
            val1 = d[A] + L
            val2 = d[B]
            opt1 = val1 if val1 > val2 else val2
            
            val3 = d[A]
            val4 = d[B] + C - L
            opt2 = val3 if val3 > val4 else val4
            
            ans = opt1 if opt1 < opt2 else opt2
            
        out.append(str(ans))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
