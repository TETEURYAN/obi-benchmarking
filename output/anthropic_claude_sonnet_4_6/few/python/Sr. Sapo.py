import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    P = int(data[idx]); idx += 1
    
    stones = set()
    for _ in range(P):
        c = int(data[idx]); idx += 1
        l = int(data[idx]); idx += 1
        stones.add((c, l))
    
    sc = int(data[idx]); idx += 1
    sl = int(data[idx]); idx += 1
    rc = int(data[idx]); idx += 1
    rl = int(data[idx]); idx += 1
    
    start = (sc, sl)
    end = (rc, rl)
    
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    
    while queue:
        c, l = queue.popleft()
        if (c, l) == end:
            print('S')
            return
        for dc in [-3, -2, -1, 1, 2, 3]:
            nc = c + dc
            nl = l
            if (nc, nl) in stones and (nc, nl) not in visited:
                visited.add((nc, nl))
                queue.append((nc, nl))
        for dl in [-3, -2, -1, 1, 2, 3]:
            nc = c
            nl = l + dl
            if (nc, nl) in stones and (nc, nl) not in visited:
                visited.add((nc, nl))
                queue.append((nc, nl))
    
    print('N')

main()