import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    # forbidden pairs as a set of frozensets
    forbidden = set()
    for _ in range(M):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        forbidden.add((x-1, y-1))
    
    # For each subset (bitmask), check if it's a valid sandwich
    # A subset is valid if no forbidden pair is entirely contained in it
    # N <= 20, so 2^20 = 1048576 subsets
    
    count = 0
    total = 1 << N
    
    for mask in range(1, total):
        valid = True
        for (x, y) in forbidden:
            if (mask >> x) & 1 and (mask >> y) & 1:
                valid = False
                break
        if valid:
            count += 1
    
    print(count)

solve()