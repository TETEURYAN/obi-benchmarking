
import sys
sys.setrecursionlimit(20000)

def main():
    data = sys.stdin.read().strip().split()
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
    
    children = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        p = parent[i]
        children[p].append(i)
    
    depth = [-1] * (N + 1)
    depth[0] = 0
    max_depth = 0
    
    stack = [0]
    while stack:
        u = stack.pop()
        for v in children[u]:
            depth[v] = depth[u] + 1
            max_depth = max(max_depth, depth[v])
            stack.append(v)
    
    gen_count = [0] * (max_depth + 1)
    gen_present = [0] * (max_depth + 1)
    
    for i in range(1, N + 1):
        d = depth[i]
        gen_count[d] += 1
        if present[i]:
            gen_present[d] += 1
    
    result = []
    for d in range(1, max_depth + 1):
        if gen_count[d] == 0:
            perc = 0.0
        else:
            perc = (gen_present[d] / gen_count[d]) * 100.0
        result.append(f"{perc:.2f}")
    
    print(" ".join(result))

if __name__ == "__main__":
    main()
