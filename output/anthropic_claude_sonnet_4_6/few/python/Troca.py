import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    up = [int(data[idx + i]) for i in range(N)]
    idx += N
    down = [int(data[idx + i]) for i in range(N)]
    idx += N
    
    # We need to track which side is up for each card.
    # flipped[i] = True means card i is currently flipped (showing original down side)
    # We use a difference array / lazy approach with a Fenwick tree to count flips
    # For each position, if total flips is odd -> show down[i], else show up[i]
    
    # Use a BIT (Fenwick tree) for range update, point query
    # Range update [l, r]: add 1 to all positions l..r
    # Point query at i: sum of updates affecting i
    # We use difference array approach with BIT
    
    # BIT for point query after range updates
    bit = [0] * (N + 2)
    
    def update(i, val):
        while i <= N:
            bit[i] += val
            i += i & (-i)
    
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s
    
    def range_update(l, r, val):
        update(l, val)
        update(r + 1, -val)
    
    for _ in range(T):
        I = int(data[idx]); idx += 1
        J = int(data[idx]); idx += 1
        range_update(I, J, 1)
    
    result = []
    for i in range(1, N + 1):
        flips = query(i)
        if flips % 2 == 0:
            result.append(up[i-1])
        else:
            result.append(down[i-1])
    
    print(*result)

main()