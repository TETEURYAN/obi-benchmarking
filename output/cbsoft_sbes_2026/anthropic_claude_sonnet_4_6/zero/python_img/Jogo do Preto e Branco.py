from itertools import combinations

def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    L = int(input_data[idx]); idx+=1
    C = int(input_data[idx]); idx+=1
    P = int(input_data[idx]); idx+=1
    
    black = set()
    for _ in range(P):
        x = int(input_data[idx])-1; idx+=1
        y = int(input_data[idx])-1; idx+=1
        black.add((x,y))
    
    # Find candidate cells: empty cells adjacent to at least one black cell
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    
    candidates = []
    for r in range(L):
        for c in range(C):
            if (r,c) in black:
                continue
            # Check if adjacent to black
            adj_black = False
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if (nr,nc) in black:
                    adj_black = True
                    break
            if adj_black:
                candidates.append((r,c))
    
    # Now we need to find maximum independent set among candidates
    # where two candidates are "conflicting" if they are adjacent to each other
    # (no two white pieces can be neighbors)
    # Also each white piece must be adjacent to at least one black (already filtered)
    
    # Build conflict graph
    n = len(candidates)
    conflict = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            r1,c1 = candidates[i]
            r2,c2 = candidates[j]
            if abs(r1-r2)+abs(c1-c2) == 1:
                conflict[i][j] = True
                conflict[j][i] = True
    
    # Maximum independent set - since n <= L*C - P <= 36 - 1 = 35
    # But with constraints L,C <= 6, max cells = 36, P >= 1, so candidates <= 35
    # Use bitmask DP or backtracking
    
    # Build adjacency as bitmask
    adj_mask = [0]*n
    for i in range(n):
        for j in range(n):
            if conflict[i][j]:
                adj_mask[i] |= (1<<j)
    
    # Maximum independent set via bitmask
    # n can be up to ~35, bitmask would be too large
    # Use backtracking with pruning
    
    best = [0]
    
    def backtrack(idx, chosen, forbidden):
        nonlocal best
        # Upper bound: chosen + remaining non-forbidden
        remaining = 0
        for i in range(idx, n):
            if not (forbidden >> i & 1):
                remaining += 1
        if chosen + remaining <= best[0]:
            return
        if idx == n:
            if chosen > best[0]:
                best[0] = chosen
            return
        # If current idx is forbidden, skip
        if forbidden >> idx & 1:
            backtrack(idx+1, chosen, forbidden)
        else:
            # Include idx
            backtrack(idx+1, chosen+1, forbidden | adj_mask[idx])
            # Exclude idx
            backtrack(idx+1, chosen, forbidden)
    
    backtrack(0, 0, 0)
    print(best[0])

solve()