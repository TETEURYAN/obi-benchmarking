import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    Xe = int(input_data[2])
    Ye = int(input_data[3])
    Xs = int(input_data[4])
    Ys = int(input_data[5])
    
    R = (N + 1) // 2
    C = (M + 1) // 2
    
    r_e = (Xe - 1) // 2
    c_e = (Ye - 1) // 2
    r_s = (Xs - 1) // 2
    c_s = (Ys - 1) // 2
    
    start = r_e * C + c_e
    end = r_s * C + c_s
    
    V = R * C
    adj = [[] for _ in range(V)]
    for r in range(R):
        for c in range(C):
            u = r * C + c
            if r > 0: adj[u].append((r - 1) * C + c)
            if r < R - 1: adj[u].append((r + 1) * C + c)
            if c > 0: adj[u].append(r * C + c - 1)
            if c < C - 1: adj[u].append(r * C + c + 1)
            
    V0 = (V + 1) // 2
    V1 = V // 2
    
    color_start = (r_e + c_e) % 2
    color_end = (r_s + c_s) % 2
    
    if color_start == color_end:
        c1 = color_start
        if c1 == 0:
            max_k = min(V0, V1 + 1)
        else:
            max_k = min(V1, V0 + 1)
        theoretical_max = 2 * max_k - 1
    else:
        max_k = min(V0, V1)
        theoretical_max = 2 * max_k
        
    max_len = [0]
    
    def get_reachable_size(mask, current):
        visited_bfs = mask | (1 << current)
        
        queue = [0] * V
        queue[0] = end
        visited_bfs |= (1 << end)
        size = 1
        
        head = 0
        tail = 1
        while head < tail:
            u = queue[head]
            head += 1
            for v in adj[u]:
                if not (visited_bfs & (1 << v)):
                    visited_bfs |= (1 << v)
                    queue[tail] = v
                    tail += 1
                    size += 1
                    
        can_reach = False
        for v in adj[current]:
            if v == end:
                can_reach = True
                break
            if not (mask & (1 << v)):
                if visited_bfs & (1 << v):
                    can_reach = True
                    break
                    
        if not can_reach:
            return -1000000
            
        return size

    def dfs(u, mask, length):
        if max_len[0] == theoretical_max:
            return
            
        if u == end:
            if length > max_len[0]:
                max_len[0] = length
            return
            
        reachable = get_reachable_size(mask, u)
        if length + reachable <= max_len[0]:
            return
            
        neighbors = []
        for v in adj[u]:
            if not (mask & (1 << v)):
                if v == end:
                    neighbors.append((100, v))
                else:
                    deg = 0
                    for w in adj[v]:
                        if not (mask & (1 << w)):
                            deg += 1
                    neighbors.append((deg, v))
                    
        neighbors.sort(key=lambda x: x[0])
        
        for deg, v in neighbors:
            dfs(v, mask | (1 << v), length + 1)
            if max_len[0] == theoretical_max:
                return

    dfs(start, 1 << start, 1)
    
    ans = 2 * max_len[0] - 1
    print(ans)

if __name__ == '__main__':
    solve()