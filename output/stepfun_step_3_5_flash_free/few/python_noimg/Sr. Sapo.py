import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    P = int(next(it))
    stones = set()
    for _ in range(P):
        c = int(next(it))
        l = int(next(it))
        stones.add((c, l))
    Sc = int(next(it))
    SL = int(next(it))
    Rc = int(next(it))
    RL = int(next(it))
    
    start = (Sc, SL)
    target = (Rc, RL)
    
    if start == target:
        print('S')
        return
        
    visited = set([start])
    queue = deque([start])
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == target:
            print('S')
            return
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            for step in range(1, 4):
                nx = x + dx * step
                ny = y + dy * step
                if (nx, ny) in stones and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    print('N')

if __name__ == "__main__":
    main()