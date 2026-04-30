
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    P = int(input_data[2])
    
    stones = set()
    idx = 3
    for _ in range(P):
        c = int(input_data[idx])
        l = int(input_data[idx+1])
        stones.add((c, l))
        idx += 2
        
    sc = int(input_data[idx])
    sl = int(input_data[idx+1])
    rc = int(input_data[idx+2])
    rl = int(input_data[idx+3])
    
    if (sc, sl) == (rc, rl):
        print('S')
        return
        
    queue = deque([(sc, sl)])
    visited = set([(sc, sl)])
    
    while queue:
        curr_c, curr_l = queue.popleft()
        
        if curr_c == rc and curr_l == rl:
            print('S')
            return
            
        for d in (1, 2, 3, -1, -2, -3):
            nc, nl = curr_c + d, curr_l
            if (nc, nl) in stones and (nc, nl) not in visited:
                visited.add((nc, nl))
                queue.append((nc, nl))
                
            nc, nl = curr_c, curr_l + d
            if (nc, nl) in stones and (nc, nl) not in visited:
                visited.add((nc, nl))
                queue.append((nc, nl))
                
    print('N')

if __name__ == '__main__':
    solve()
