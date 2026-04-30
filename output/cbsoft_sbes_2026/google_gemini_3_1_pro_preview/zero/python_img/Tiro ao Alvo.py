import sys
from bisect import bisect_left

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    C = int(input_data[0])
    T = int(input_data[1])
    
    radii_sq = []
    idx = 2
    for _ in range(C):
        r = int(input_data[idx])
        radii_sq.append(r * r)
        idx += 1
        
    total_score = 0
    for _ in range(T):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        d_sq = x * x + y * y
        
        pos = bisect_left(radii_sq, d_sq)
        total_score += (C - pos)
        
    print(total_score)

if __name__ == '__main__':
    solve()