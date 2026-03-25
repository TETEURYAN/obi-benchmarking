import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    n_len = len(input_data)
    
    out = []
    
    while idx < n_len:
        N = int(input_data[idx])
        M = int(input_data[idx+1])
        I = int(input_data[idx+2])
        idx += 3
        
        ages = [0] * (N + 1)
        for i in range(1, N + 1):
            ages[i] = int(input_data[idx])
            idx += 1
            
        adj_orig = [[] for _ in range(N + 1)]
        adj_rev = [[] for _ in range(N + 1)]
        in_degree = [0] * (N + 1)
        
        for _ in range(M):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            adj_orig[u].append(v)
            adj_rev[v].append(u)
            in_degree[v] += 1
            
        topo_order = []
        queue = [i for i in range(1, N + 1) if in_degree[i] == 0]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            topo_order.append(u)
            for v in adj_orig[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        reach = [0] * (N + 1)
        if len(topo_order) == N:
            for u in topo_order:
                for p in adj_rev[u]:
                    reach[u] |= (1 << p) | reach[p]
        else:
            for i in range(1, N + 1):
                visited = [False] * (N + 1)
                visited[i] = True
                q = [i]
                h = 0
                while h < len(q):
                    u = q[h]
                    h += 1
                    for v in adj_rev[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                            reach[i] |= (1 << v)
                            
        reachable_nodes = [[] for _ in range(N + 1)]
        for i in range(1, N + 1):
            mask = reach[i]
            while mask > 0:
                lsb = mask & -mask
                v = lsb.bit_length() - 1
                reachable_nodes[i].append(v)
                mask ^= lsb
                
        pos = list(range(N + 1))
        emp = list(range(N + 1))
        
        for _ in range(I):
            inst = input_data[idx]
            idx += 1
            if inst == 'T':
                A = int(input_data[idx])
                B = int(input_data[idx+1])
                idx += 2
                
                pA = pos[A]
                pB = pos[B]
                
                pos[A] = pB
                pos[B] = pA
                
                emp[pA] = B
                emp[pB] = A
            else:
                E = int(input_data[idx])
                idx += 1
                
                u = pos[E]
                if not reachable_nodes[u]:
                    out.append('*')
                else:
                    min_age = min([ages[emp[v]] for v in reachable_nodes[u]])
                    out.append(str(min_age))
                    
    if out:
        print('\n'.join(out))

if __name__ == '__main__':
    solve()