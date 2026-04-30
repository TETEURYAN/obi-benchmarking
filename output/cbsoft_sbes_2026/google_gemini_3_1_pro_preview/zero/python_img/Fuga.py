import sys

sys.setrecursionlimit(2000)

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
    
    r_e = (Xe + 1) // 2 - 1
    c_e = (Ye + 1) // 2 - 1
    r_s = (Xs + 1) // 2 - 1
    c_s = (Ys + 1) // 2 - 1
    
    V = R * C
    V0 = 0
    V1 = 0
    for i in range(R):
        for j in range(C):
            if (i + j) % 2 == 0:
                V0 += 1
            else:
                V1 += 1
                
    color_in = (r_e + c_e) % 2
    color_out = (r_s + c_s) % 2
    
    if color_in == color_out:
        if color_in == 0:
            k = min(V0, V1 + 1)
        else:
            k = min(V1, V0 + 1)
        upper_bound = 2 * k - 1
    else:
        k = min(V0, V1)
        upper_bound = 2 * k
        
    adj = [[] for _ in range(V)]
    for i in range(R):
        for j in range(C):
            u = i * C + j
            if i > 0: adj[u].append((i - 1) * C + j)
            if i < R - 1: adj[u].append((i + 1) * C + j)
            if j > 0: adj[u].append(i * C + j - 1)
            if j < C - 1: adj[u].append(i * C + j + 1)
            
    start = r_e * C + c_e
    target = r_s * C + c_s
    
    max_len = [0]
    
    def dfs(u, mask, depth):
        if u == target:
            if depth > max_len[0]:
                max_len[0] = depth
            return
            
        if max_len[0] == upper_bound:
            return
            
        neighbors = []
        for v in adj[u]:
            if not (mask & (1 << v)):
                deg = 0
                for nxt in adj[v]:
                    if not (mask & (1 << nxt)):
                        deg += 1
                neighbors.append((deg, v))
                
        neighbors.sort(key=lambda x: x[0])
        
        for deg, v in neighbors:
            dfs(v, mask | (1 << v), depth + 1)
            if max_len[0] == upper_bound:
                return

    dfs(start, 1 << start, 1)
    
    ans = 2 * max_len[0] - 1
    print(ans)

if __name__ == '__main__':
    solve()