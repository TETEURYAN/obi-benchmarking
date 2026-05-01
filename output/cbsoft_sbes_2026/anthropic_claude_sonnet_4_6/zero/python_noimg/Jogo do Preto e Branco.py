from itertools import combinations

def solve():
    L, C = map(int, input().split())
    P = int(input())
    black = set()
    for _ in range(P):
        x, y = map(int, input().split())
        black.add((x-1, y-1))
    
    # Find all empty cells that are adjacent to at least one black piece
    # These are candidates for white pieces
    candidates = []
    for r in range(L):
        for c in range(C):
            if (r, c) in black:
                continue
            # Check if adjacent to black
            adj_black = False
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if (nr, nc) in black:
                    adj_black = True
                    break
            if adj_black:
                candidates.append((r, c))
    
    # Now we need to find maximum subset of candidates such that
    # no two white pieces are adjacent to each other
    # This is maximum independent set on the adjacency graph of candidates
    
    n = len(candidates)
    
    # Build adjacency: which pairs of candidates are adjacent
    adj = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            r1, c1 = candidates[i]
            r2, c2 = candidates[j]
            if abs(r1-r2) + abs(c1-c2) == 1:
                adj[i] |= (1 << j)
    
    # Maximum independent set via bitmask DP
    # n <= L*C - P <= 36 - 1 = 35, but candidates are at most 36
    # With n up to ~35, we need efficient approach
    # Since L,C <= 6, total cells <= 36, candidates <= 36
    # But 2^36 is too large. Use branch and bound or smarter approach.
    
    # Actually with L,C<=6, max candidates = 36
    # Use branch and bound with pruning
    
    best = [0]
    
    def backtrack(idx, current_set, current_mask, count):
        if count + (n - idx) <= best[0]:
            return
        if idx == n:
            if count > best[0]:
                best[0] = count
            return
        # Try including candidates[idx]
        if not (current_mask & (1 << idx)):
            backtrack(idx+1, current_set | (1<<idx), current_mask | adj[idx], count+1)
        # Try excluding
        backtrack(idx+1, current_set, current_mask, count)
    
    backtrack(0, 0, 0, 0)
    print(best[0])

solve()