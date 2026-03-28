import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    order = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    parent = [0] * (n + 1)
    
    head = 0
    while head < len(order):
        u = order[head]
        head += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                order.append(v)
                
    reversed_order = order[::-1]
    
    def check(R):
        uncov = [0] * (n + 1)
        radar = [300005] * (n + 1)
        radars_needed = 0
        
        for u in reversed_order:
            if uncov[u] >= 0 and uncov[u] + radar[u] <= R:
                uncov[u] = -300005
                
            if uncov[u] == R:
                radars_needed += 1
                radar[u] = 0
                uncov[u] = -300005
                
            p = parent[u]
            if p != 0:
                if uncov[u] >= 0:
                    nxt_uncov = uncov[u] + 1
                    if nxt_uncov > uncov[p]:
                        uncov[p] = nxt_uncov
                if radar[u] != 300005:
                    nxt_radar = radar[u] + 1
                    if nxt_radar < radar[p]:
                        radar[p] = nxt_radar
                        
        if uncov[1] >= 0:
            radars_needed += 1
            
        return radars_needed <= k

    low = 0
    high = n
    ans = n
    
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