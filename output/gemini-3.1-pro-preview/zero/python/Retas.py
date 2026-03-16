
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    X1 = int(input_data[1])
    X2 = int(input_data[2])
    
    it = iter(input_data[3:])
    lines = [(int(A) * X1 + int(B), int(A) * X2 + int(B)) for A, B in zip(it, it)]
    
    lines.sort(key=lambda x: (x[0], -x[1]))
    
    y2_vals = [x[1] for x in lines]
    
    unique_y2 = sorted(list(set(y2_vals)))
    y2_rank = {val: i + 1 for i, val in enumerate(unique_y2)}
    
    M = len(unique_y2)
    bit = [0] * (M + 1)
    
    ans = 0
    for i, y2 in enumerate(y2_vals):
        rank = y2_rank[y2]
        
        s = 0
        idx = rank - 1
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
            
        ans += i - s
        
        idx = rank
        while idx <= M:
            bit[idx] += 1
            idx += idx & (-idx)
            
    print(ans)

if __name__ == '__main__':
    solve()
