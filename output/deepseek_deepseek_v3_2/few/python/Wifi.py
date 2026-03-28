import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    rects = []
    for _ in range(n):
        x1 = int(next(it))
        y1 = int(next(it))
        x2 = int(next(it))
        y2 = int(next(it))
        rects.append((x1, y1, x2, y2))
    
    parent = [-1] * n
    children = [[] for _ in range(n)]
    
    for i in range(n):
        x1_i, y1_i, x2_i, y2_i = rects[i]
        best = -1
        best_area = float('inf')
        for j in range(n):
            if i == j:
                continue
            x1_j, y1_j, x2_j, y2_j = rects[j]
            if x1_j <= x1_i and y1_i <= y1_j and x2_i <= x2_j and y2_j <= y2_i:
                area = (x2_j - x1_j) * (y1_j - y2_j)
                if area < best_area:
                    best_area = area
                    best = j
        parent[i] = best
        if best != -1:
            children[best].append(i)
    
    root = -1
    for i in range(n):
        if parent[i] == -1:
            root = i
            break
    
    ans = 0
    stack = [(root, False)]
    while stack:
        u, covered = stack.pop()
        if not covered:
            ans += 1
            covered = True
        for v in children[u]:
            stack.append((v, covered))
    
    print(ans)

if __name__ == "__main__":
    solve()