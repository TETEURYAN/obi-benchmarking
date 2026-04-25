Since raridade of color i is 2^i, and 2^N > 2^1 + 2^2 + ... + 2^(N-1), we should always prefer keeping the highest-colored Upa. So we greedily pick upas from highest to lowest color, skipping any that conflict with already chosen ones.

The key insight: since 2^i > sum of all 2^j for j < i, we want to maximize by always keeping the highest available upa. We process colors from N down to 1, and include color i if it doesn't conflict with any already-included color.

import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    conflict = [set() for _ in range(N + 1)]
    
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        conflict[u].add(v)
        conflict[v].add(u)
    
    chosen = set()
    
    for i in range(N, 0, -1):
        # Check if i conflicts with any chosen
        can_add = True
        for c in conflict[i]:
            if c in chosen:
                can_add = False
                break
        if can_add:
            chosen.add(i)
    
    result = sorted(chosen)
    print(len(result))
    print(*result)

main()