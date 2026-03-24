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
    
    visited = [0] * (N + 1)
    curr = 1
    while visited[curr] == 0:
        visited[curr] = 1
        curr = F[curr]
        
    cycle_nodes = []
    temp = curr
    while True:
        cycle_nodes.append(temp)
        temp = F[temp]
        if temp == curr:
            break
            
    C = len(cycle_nodes)
    pos = [0] * (N + 1)
    in_cycle = [False] * (N + 1)
    for i in range(C):
        node = cycle_nodes[i]
        pos[node] = i
        in_cycle[node] = True
        
    adj_rev = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        adj_rev[F[i]].append(i)
        
    R = [0] * (N + 1)
    D = [0] * (N + 1)
    q = deque()
    
    for node in cycle_nodes:
        R[node] = node
        D[node] = 0
        q.append(node)
        
    while q:
        u = q.popleft()
        for v in adj_rev[u]:
            if not in_cycle[v]:
                R[v] = R[u]
                D[v] = D[u] + 1
                q.append(v)
                
    idx = N + 2
    out = []
    for _ in range(Q):
        A = int(input_data[idx])
        B = int(input_data[idx+1])
        idx += 2
        
        if R[A] == R[B]:
            diff = D[A] - D[B]
            out.append(str(diff if diff >= 0 else -diff))
        else:
            rA = R[A]
            rB = R[B]
            pA = pos[rA]
            pB = pos[rB]
            
            L1 = pB - pA
            if L1 < 0:
                L1 += C
                
            L2 = pA - pB
            if L2 < 0:
                L2 += C
            
            ans1 = D[A] if D[A] >= D[B] + L2 else D[B] + L2
            ans2 = D[A] + L1 if D[A] + L1 >= D[B] else D[B]
            
            out.append(str(ans1 if ans1 < ans2 else ans2))
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()