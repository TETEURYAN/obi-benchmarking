import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    X1 = int(input_data[1])
    X2 = int(input_data[2])
    
    points = []
    idx = 3
    for _ in range(N):
        A = int(input_data[idx])
        B = int(input_data[idx+1])
        idx += 2
        
        y1 = A * X1 + B
        y2 = A * X2 + B
        points.append((y1, y2))
        
    points.sort(key=lambda p: (p[0], -p[1]))
    
    y2_values = [p[1] for p in points]
    unique_y2 = sorted(list(set(y2_values)))
    rank = {val: i + 1 for i, val in enumerate(unique_y2)}
    
    M = len(unique_y2)
    tree = [0] * (M + 1)
    
    def add(i, delta):
        while i <= M:
            tree[i] += delta
            i += i & (-i)
            
    def query(i):
        s = 0
        while i > 0:
            s += tree[i]
            i -= i & (-i)
        return s

    intersections = 0
    for p in points:
        r = rank[p[1]]
        intersections += query(M) - query(r - 1)
        add(r, 1)
        
    print(intersections)

if __name__ == '__main__':
    solve()