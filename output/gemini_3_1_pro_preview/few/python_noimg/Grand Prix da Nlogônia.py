import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    plans = []
    idx = 2
    for _ in range(M):
        U = int(input_data[idx])
        L = int(input_data[idx+1])
        R = int(input_data[idx+2])
        plans.append((U, L, R))
        idx += 3
        
    size = 1
    while size < N:
        size *= 2
        
    TOTAL_NODES = 2 * size - 1
    
    base_in_degree = [1] * (TOTAL_NODES + 1)
    base_in_degree[1] = 0
    base_in_degree[0] = 0
    
    extra_adj = [[] for _ in range(TOTAL_NODES + 1)]
    queue = [0] * (TOTAL_NODES + 1)
    
    plan_edges = []
    for U, L, R in plans:
        u_node = size + U - 1
        edges = []
        l = L + size - 1
        r = R + size - 1
        while l <= r:
            if l % 2 == 1:
                edges.append(l)
                l += 1
            if r % 2 == 0:
                edges.append(r)
                r -= 1
            l //= 2
            r //= 2
        plan_edges.append((u_node, edges))
        
    def check(X):
        in_degree = base_in_degree[:]
        
        for i in range(X):
            u_node, edges = plan_edges[i]
            extra_adj[u_node].extend(edges)
            for v in edges:
                in_degree[v] += 1
                
        q = queue
        q[0] = 1
        head = 0
        tail = 1
        
        while head < tail:
            u = q[head]
            head += 1
            
            if u < size:
                left = 2 * u
                in_degree[left] -= 1
                if not in_degree[left]:
                    q[tail] = left
                    tail += 1
                    
                right = left + 1
                in_degree[right] -= 1
                if not in_degree[right]:
                    q[tail] = right
                    tail += 1
            else:
                adj_u = extra_adj[u]
                if adj_u:
                    for v in adj_u:
                        in_degree[v] -= 1
                        if not in_degree[v]:
                            q[tail] = v
                            tail += 1
                            
        for i in range(X):
            u_node = plan_edges[i][0]
            if extra_adj[u_node]:
                extra_adj[u_node].clear()
                
        return head < TOTAL_NODES

    low = 1
    high = M
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()