import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        parent[i] = int(data[idx]); idx += 1
    
    present = [False] * (N + 1)
    for _ in range(M):
        p = int(data[idx]); idx += 1
        present[p] = True
    
    depth = [-1] * (N + 1)
    depth[0] = 0
    
    from collections import deque
    q = deque()
    q.append(0)
    max_depth = 0
    depth_count = [0] * (N + 2)
    depth_present = [0] * (N + 2)
    
    while q:
        u = q.popleft()
        for v in range(1, N + 1):
            if parent[v] == u:
                depth[v] = depth[u] + 1
                max_depth = max(max_depth, depth[v])
                q.append(v)
                depth_count[depth[v]] += 1
                if present[v]:
                    depth_present[depth[v]] += 1
    
    result = []
    for d in range(1, max_depth + 1):
        if depth_count[d] == 0:
            perc = 0.0
        else:
            perc = (depth_present[d] / depth_count[d]) * 100.0
        result.append(f"{perc:.2f}")
    
    print(" ".join(result))

if __name__ == "__main__":
    main()