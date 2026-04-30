
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    X1 = int(input_data[1])
    X2 = int(input_data[2])
    
    lines = []
    idx = 3
    for _ in range(N):
        A = int(input_data[idx])
        B = int(input_data[idx+1])
        idx += 2
        
        Y1 = A * X1 + B
        Y2 = A * X2 + B
        lines.append((Y1, Y2))
        
    lines.sort(key=lambda x: (x[0], -x[1]))
    
    Y2_array = [x[1] for x in lines]
    
    sorted_unique_Y2 = sorted(list(set(Y2_array)))
    rank = {val: i + 1 for i, val in enumerate(sorted_unique_Y2)}
    
    M = len(sorted_unique_Y2)
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
    inserted = 0
    for y in Y2_array:
        r = rank[y]
        intersections += inserted - query(r - 1)
        add(r, 1)
        inserted += 1
        
    print(intersections)

if __name__ == '__main__':
    solve()
