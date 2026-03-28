import sys

def coins_produced(cycles, days):
    total = 0
    for c in cycles:
        total += days // c
    return total

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    f = int(data[1])
    cycles = [int(data[i+2]) for i in range(n)]
    
    lo, hi = 1, 10**8
    
    while lo < hi:
        mid = (lo + hi) // 2
        if coins_produced(cycles, mid) >= f:
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

solve()