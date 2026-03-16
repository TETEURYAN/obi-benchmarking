
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
        y1 = A * X1 + B
        y2 = A * X2 + B
        lines.append((y1, y2))
        
    lines.sort(key=lambda x: (x[0], -x[1]))
    
    y2_vals = [x[1] for x in lines]
    
    unique_y2 = sorted(list(set(y2_vals)))
    rank = {val: i + 1 for i, val in enumerate(unique_y2)}
    
    M = len(unique_y2)
    bit = [0] * (M + 1)
    
    def add(i, delta):
        while i <= M:
            bit[i] += delta
            i += i & (-i)
            
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    inversions = 0
    for i, y2 in enumerate(y2_vals):
        r = rank[y2]
        inversions += i - query(r - 1)
        add(r, 1)
        
    print(inversions)

if __name__ == '__main__':
    solve()
