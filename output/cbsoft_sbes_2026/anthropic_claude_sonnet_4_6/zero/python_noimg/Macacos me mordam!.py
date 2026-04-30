
import sys
from collections import deque

def can_see(ax, ah, bx, bh, trees_between):
    """Check if from top of tree A, we can see top of tree B"""
    # For each tree C between A and B, check if C blocks the view
    # The line of sight from (ax, ah) to (bx, bh)
    # At position cx, the line of sight height is:
    # ah + (bh - ah) * (cx - ax) / (bx - ax)
    # Tree C blocks if hc >= line_of_sight_height at cx
    for (cx, ch) in trees_between:
        # line of sight height at cx
        # los = ah + (bh - ah) * (cx - ax) / (bx - ax)
        # ch >= los means blocked
        # ch * (bx - ax) >= ah * (bx - ax) + (bh - ah) * (cx - ax)
        los_num = ah * (bx - ax) + (bh - ah) * (cx - ax)
        ch_num = ch * (bx - ax)
        if ch_num >= los_num:
            return False
    return True

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    trees = []
    for _ in range(n):
        x = int(input_data[idx]); idx += 1
        h = int(input_data[idx]); idx += 1
        trees.append((x, h))
    
    # Sort by position
    trees.sort()
    
    if n == 1:
        print(0)
        return
    
    # BFS/DP: dp[i] = minimum jumps to reach tree i
    # dp[0] = 0, find dp[n-1]
    # For each tree i, we want to find the farthest tree j we can jump to
    # Greedy: from current position, jump as far as possible
    
    # Key insight: visibility is blocked by trees in between
    # From tree i to tree j, blocked if any tree k (i < k < j) has height >= line of sight
    
    # Greedy approach: BFS layer by layer
    # From each reachable set, find all trees reachable in one more jump
    
    # For efficiency: from position i, the farthest reachable j
    # We can use the convex hull / upper envelope idea
    
    # Actually, let's think: tree k blocks i->j if hk >= line_of_sight at xk
    # This means: (hk - hi) / (xk - xi) >= (hj - hi) / (xj - xi)
    # i.e., slope from i to k >= slope from i to j
    
    # So from tree i, tree j is visible iff no tree k between i and j has
    # slope(i,k) >= slope(i,j)
    # i.e., slope(i,j) > max slope from i to any k in (i, j)
    
    # The farthest visible tree from i going right:
    # We scan right, maintaining max slope seen so far
    # j is visible from i iff slope(i,j) > max_slope(i, k) for all k < j
    
    # Greedy: use BFS with levels
    # dp[i] = min jumps to reach i
    
    dp = [float('inf')] * n
    dp[0] = 0
    
    # For each i, find all j reachable from i
    # But O(n^2) might be too slow for n=3e5
    
    # Greedy: at each step, from the current frontier, jump as far as possible
    # This is like jump game II
    
    # From position i, farthest reachable: scan right maintaining upper convex hull of slopes
    # j is reachable from i iff slope(i->j) > all slopes(i->k) for i < k < j
    # This means j is on the "upper right convex hull" from i
    
    # For the greedy BFS approach with O(n log n):
    # We process trees left to right
    # Maintain for each tree the farthest it can reach
    
    # Simple O(n^2) might TLE for n=3e5, let's try greedy jump game style
    
    # Greedy: current position, current max reach, next max reach
    jumps = 0
    current_end = 0  # index of farthest tree reachable with 'jumps' jumps
    farthest = 0
    
    # Precompute for each i, the farthest j reachable
    # farthest_reach[i] = max j such that tree j is visible from tree i
    
    farthest_reach = [0] * n
    for i in range(n):
        # Scan right from i, track max slope
        max_slope_num = -float('inf')  # slope numerator/denominator comparison
        xi, hi = trees[i]
        farthest_reach[i] = i
        # Use fraction comparison: slope = (hj - hi) / (xj - xi)
        # max_slope as fraction: num/den
        max_s_num = None
        max_s_den = None
        for j in range(i+1, n):
            xj, hj = trees[j]
            s_num = hj - hi
            s_den = xj - xi
            # Compare s_num/s_den > max_slope?
            if max_s_num is None or s_num * max_s_den > max_s_num * s_den:
                # visible
                farthest_reach[i] = j
                max_s_num = s_num
                max_s_den = s_den
    
    # Now jump game II
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(n-1):
        farthest = max(farthest, farthest_reach[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n-1:
                break
    
    print(jumps)

solve()