import sys
from sortedcontainers import SortedList

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    sl = SortedList()
    prev_penalty = 0
    out = []
    
    for k in range(n):
        xk = int(data[idx]); idx += 1
        yk = int(data[idx]); idx += 1
        
        xr = xk + prev_penalty
        yr = yk + prev_penalty
        
        dist_sq = xr * xr + yr * yr
        
        # Count elements in sl that are <= dist_sq
        penalty = sl.bisect_right(dist_sq)
        
        out.append(penalty)
        sl.add(dist_sq)
        prev_penalty = penalty
    
    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()