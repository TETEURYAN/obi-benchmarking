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
    
    max_rank = len(unique_y2)
    bit = [0] * (max_rank + 1)
    
    inversions = 0
    for i in range(N):
        y2 = y2_vals[i]
        r = rank[y2]
        
        s = 0
        q_idx = r - 1
        while q_idx > 0:
            s += bit[q_idx]
            q_idx -= q_idx & (-q_idx)
            
        inversions += i - s
        
        a_idx = r
        while a_idx <= max_rank:
            bit[a_idx] += 1
            a_idx += a_idx & (-a_idx)
            
    print(inversions)

if __name__ == '__main__':
    solve()