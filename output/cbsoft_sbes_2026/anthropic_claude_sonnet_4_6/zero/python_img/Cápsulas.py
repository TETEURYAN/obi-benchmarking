import sys

def coins_produced(days, cycles):
    total = 0
    for c in cycles:
        total += days // c
    return total

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    f = int(input_data[1])
    cycles = [int(input_data[i+2]) for i in range(n)]
    
    lo, hi = 1, 10**8
    
    while lo < hi:
        mid = (lo + hi) // 2
        if coins_produced(mid, cycles) >= f:
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

solve()