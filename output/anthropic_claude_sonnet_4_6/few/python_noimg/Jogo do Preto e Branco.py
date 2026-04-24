import sys
from itertools import combinations

def solve():
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx]); idx+=1
    C = int(data[idx]); idx+=1
    P = int(data[idx]); idx+=1
    
    black = set()
    for _ in range(P):
        x = int(data[idx])-1; idx+=1
        y = int(data[idx])-1; idx+=1
        black.add((x,y))
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # Find candidate cells: empty cells adjacent to at least one black cell
    candidates = []
    for r in range(L):
        for c in range(C):
            if (r,c) in black:
                continue
            # check if adjacent to black
            adj_black = False
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if (nr,nc) in black:
                    adj_black = True
                    break
            if adj_black:
                candidates.append((r,c))
    
    # We need to find maximum independent set among candidates
    # where two candidates are "conflicting" if they are adjacent to each other
    # (white pieces cannot be adjacent to each other)
    # Since L,C <= 6, candidates <= 36, but P>=1 so candidates <= 35
    # We can use bitmask DP or brute force with backtracking
    
    n = len(candidates)
    
    # Build conflict graph
    conflict = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            r1,c1 = candidates[i]
            r2,c2 = candidates[j]
            if abs(r1-r2)+abs(c1-c2) == 1:
                conflict[i] |= (1<<j)
    
    # Maximum independent set via bitmask
    # n <= 35 in worst case... that's too large for 2^35
    # But actually with L,C<=6 and P>=1, candidates <= 35
    # However, typical cases will be much smaller
    # Let's use branch and bound / backtracking
    
    best = [0]
    
    def backtrack(idx, chosen, count):
        if count + (n - idx) <= best[0]:
            return
        if idx == n:
            if count > best[0]:
                best[0] = count
            return
        # Try placing white at candidates[idx]
        if not (chosen & conflict[idx]):
            backtrack(idx+1, chosen | (1<<idx), count+1)
        # Try not placing
        backtrack(idx+1, chosen, count)
    
    backtrack(0, 0, 0)
    print(best[0])

solve()