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
    
    Y2_arr = [x[1] for x in lines]
    
    sorted_unique = sorted(list(set(Y2_arr)))
    rank = {val: i + 1 for i, val in enumerate(sorted_unique)}
    
    max_rank = len(rank)
    bit = [0] * (max_rank + 1)
    
    def add(i, delta):
        while i <= max_rank:
            bit[i] += delta
            i += i & (-i)
            
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    inv = 0
    total_inserted = 0
    for y in Y2_arr:
        r = rank[y]
        inv += total_inserted - query(r - 1)
        add(r, 1)
        total_inserted += 1
        
    print(inv)

if __name__ == '__main__':
    solve()