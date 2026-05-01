import sys
sys.setrecursionlimit(200000)

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
    
    if start not in stones or target not in stones:
        print('N')
        return
    
    visited = set()
    stack = [start]
    visited.add(start)
    
    while stack:
        c, l = stack.pop()
        if (c, l) == target:
            print('S')
            return
        
        for dc in range(-3, 4):
            for dl in range(-3, 4):
                if abs(dc) + abs(dl) > 3:
                    continue
                if dc == 0 and dl == 0:
                    continue
                nc, nl = c + dc, l + dl
                if 1 <= nc <= N and 1 <= nl <= M:
                    if (nc, nl) in stones and (nc, nl) not in visited:
                        visited.add((nc, nl))
                        stack.append((nc, nl))
    
    print('N')

if __name__ == "__main__":
    main()