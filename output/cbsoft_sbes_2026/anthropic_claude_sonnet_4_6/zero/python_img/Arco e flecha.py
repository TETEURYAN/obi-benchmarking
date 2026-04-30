import sys
from sortedcontainers import SortedList

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    
    sl = SortedList()
    prev_penalty = 0
    output = []
    
    for k in range(n):
        xk = int(input_data[idx]); idx += 1
        yk = int(input_data[idx]); idx += 1
        
        xr = xk + prev_penalty
        yr = yk + prev_penalty
        
        dist_sq = xr * xr + yr * yr
        
        # Count how many elements in sl are <= dist_sq
        # SortedList supports bisect_right
        penalty = sl.bisect_right(dist_sq)
        
        output.append(penalty)
        sl.add(dist_sq)
        prev_penalty = penalty
    
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

main()