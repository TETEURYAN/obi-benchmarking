import sys

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
    
    sr = (Xe - 1) // 2
    sc = (Ye - 1) // 2
    er = (Xs - 1) // 2
    ec = (Ys - 1) // 2
    
    start = sr * C + sc
    target = er * C + ec
    
    adj = [[] for _ in range(R * C)]
    for r in range(R):
        for c in range(C):
            u = r * C + c
            if r > 0: adj[u].append((r - 1) * C + c)
            if r < R - 1: adj[u].append((r + 1) * C + c)
            if c > 0: adj[u].append(r * C + c - 1)
            if c < C - 1: adj[u].append(r * C + c + 1)
            
    for u in range(R * C):
        adj[u].sort(key=lambda v: len(adj[v]))
        
    adj = [tuple(l) for l in adj]
    
    count = [0, 0]
    for r in range(R):
        for c in range(C):
            count[(r + c) % 2] += 1
            
    color_start = (sr + sc) % 2
    color_end = (er + ec) % 2
    
    if color_start == color_end:
        k = min(count[1 - color_start], count[color_start] - 1)
        max_nodes = 2 * k + 1
    else:
        k = min(count[color_start], count[1 - color_start])
        max_nodes = 2 * k
        
    max_len = 0
    
    def dfs(u, mask, length):
        nonlocal max_len
        for v in adj[u]:
            if not (mask & (1 << v)):
                if v == target:
                    if length + 1 > max_len:
                        max_len = length + 1
                        if max_len == max_nodes:
                            raise StopIteration
                else:
                    dfs(v, mask | (1 << v), length + 1)
                    
    try:
        dfs(start, 1 << start, 1)
    except StopIteration:
        pass
        
    print(2 * max_len - 1)

if __name__ == '__main__':
    solve()