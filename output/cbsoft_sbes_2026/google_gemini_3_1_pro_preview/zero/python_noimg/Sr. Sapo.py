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
    
    visited = set()
    queue = deque()
    
    queue.append((sc, sl))
    visited.add((sc, sl))
    
    while queue:
        c, l = queue.popleft()
        
        if c == rc and l == rl:
            print('S')
            return
            
        for dc in (-3, -2, -1, 1, 2, 3):
            nc = c + dc
            if (nc, l) in stones and (nc, l) not in visited:
                visited.add((nc, l))
                queue.append((nc, l))
                
        for dl in (-3, -2, -1, 1, 2, 3):
            nl = l + dl
            if (c, nl) in stones and (c, nl) not in visited:
                visited.add((c, nl))
                queue.append((c, nl))
                
    print('N')

if __name__ == '__main__':
    solve()