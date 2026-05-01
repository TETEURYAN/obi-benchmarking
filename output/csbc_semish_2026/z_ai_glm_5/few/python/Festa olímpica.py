
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = int(data[0])
    M = int(data[1])
    T = [int(data[i]) for i in range(2, 2 + M)]
    
    # Compute final length after all turns
    L = N
    for Ti in T:
        L -= L // Ti
    
    # Output the first min(L, 10000) survivors
    count = min(L, 10000)
    
    output = []
    T_reversed = T[::-1]
    for p in range(1, count + 1):
        pos = p
        # Work backwards through all turns
        for Ti in T_reversed:
            q, r = divmod(pos - 1, Ti - 1)
            pos = q * Ti + r + 1
        output.append(str(pos))
    
    sys.stdout.write('\n'.join(output))

solve()
