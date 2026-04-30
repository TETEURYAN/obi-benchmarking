import sys
from collections import deque

def can_see(ax, ah, bx, bh, trees):
    """Check if from tree A we can see tree B (no tree in between blocks the view)"""
    # Trees between A and B
    # The line of sight from top of A to top of B
    # A tree C blocks the view if the line from A to B passes below the top of C
    # Line from (ax, ah) to (bx, bh)
    # At position cx, the height of the line is:
    # ah + (bh - ah) * (cx - ax) / (bx - ax)
    # C blocks if hc > line_height at cx
    
    # We need to check all trees between A and B
    # This is O(N) per check which is too slow for N=3e5
    # We need a smarter approach
    pass

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
    
    # BFS/DP approach
    # dp[i] = minimum jumps to reach tree i
    # dp[0] = 0
    # dp[j] = min(dp[i] + 1) for all i where i can see j
    
    # Key insight: tree i can see tree j if no tree k between them (i < k < j) blocks the view
    # A tree k blocks i->j if hk >= line height at xk from (xi,hi) to (xj,hj)
    # line height at xk: hi + (hj-hi)*(xk-xi)/(xj-xi)
    # blocked if hk * (xj-xi) >= hi*(xj-xi) + (hj-hi)*(xk-xi)
    # hk*(xj-xi) >= hi*(xj-xk) + hj*(xk-xi)  ... wait let me redo
    # line at xk: hi + (hj-hi)*(xk-xi)/(xj-xi)
    # blocked if hk >= hi + (hj-hi)*(xk-xi)/(xj-xi)
    # hk*(xj-xi) >= hi*(xj-xi) + (hj-hi)*(xk-xi)
    # hk*(xj-xi) >= hi*xj - hi*xi + hj*xk - hj*xi - hi*xk + hi*xi
    # hk*(xj-xi) >= hi*xj - hi*xi + hj*xk - hj*xi - hi*xk + hi*xi
    # hk*(xj-xi) >= hi*(xj-xi) + (hj-hi)*(xk-xi)
    
    # For BFS with minimum jumps, we use a greedy approach:
    # From current position, jump as far as possible
    # This is like the "jump game" problem
    
    # Greedy: at each step, from all reachable trees in current level,
    # find the farthest tree reachable in next step
    
    # But "can see" is not simply "farther = better"
    # We need to use convex hull trick or similar
    
    # Actually, visibility is determined by upper convex hull between two trees
    # i can see j iff no tree between them is above the line segment from i to j
    # This means: the trees visible from i are those on the upper convex hull starting from i
    
    # BFS with levels, but we need efficient range queries
    # Use the fact that if i can reach j, and i can reach k>j, then j might reach further than k
    # Not necessarily true here.
    
    # Let's do BFS but prune: track the "frontier" as a convex hull
    
    dp = [float('inf')] * n
    dp[0] = 0
    
    # For each tree i, find all j > i that i can see
    # Use upper convex hull from each point
    
    # Simple O(N^2) might TLE for N=3e5, need O(N log N)
    # For now implement O(N^2) and see
    
    for i in range(n - 1):
        if dp[i] == float('inf'):
            continue
        xi, hi = trees[i]
        # Check visibility to j using upper convex hull
        # Maintain the "blocking" slope
        max_slope = float('-inf')  # slope needed to see over blocking trees... 
        # Actually track upper envelope
        # From i, j is visible if the slope from i to j is greater than all slopes from i to k for i<k<j
        # Wait: i sees j if no k between i and j has hk above the line i->j
        # Equivalently, i sees j if slope(i,j) >= slope(i,k) for all k between i and j? No...
        # i sees j if for all k between i and j: hk < line_ij at xk
        # This means the upper convex hull from i determines visibility
        
        upper_hull_slope = float('-inf')
        for j in range(i + 1, n):
            xj, hj = trees[j]
            slope_ij = (hj - hi) / (xj - xi)
            if slope_ij >= upper_hull_slope:
                # i can see j
                if dp[i] + 1 < dp[j]:
                    dp[j] = dp[i] + 1
                upper_hull_slope = max(upper_hull_slope, slope_ij)
            # Update upper hull: if slope_ij > upper_hull_slope, update
            # Actually upper_hull_slope should track max slope seen so far
            upper_hull_slope = max(upper_hull_slope, slope_ij)
    
    print(dp[n - 1])

solve()