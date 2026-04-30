import sys
from bisect import bisect_left, bisect_right, insort

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    # A horizontal cut at height h cuts through rectangles where h < A[i] (strictly inside)
    # A rectangle is cut if 0 < h < A[i], i.e., h >= 1 and h <= A[i]-1
    # 
    # When we cut at height h, we get pieces. The number of pieces depends on:
    # - The cut goes through some rectangles (those with A[i] > h)
    # - Rectangles with A[i] <= h are completely below or at the cut line
    #
    # Actually, let's think more carefully:
    # A cut at height h:
    # - Rectangles with A[i] > h are cut into two parts (top and bottom)
    # - Rectangles with A[i] <= h are only in the bottom part
    # - Rectangles with A[i] == h: the cut is exactly at the top, so not really cutting through
    #   Actually if h == A[i], the cut is at the top edge, so the rectangle is not split
    #
    # The number of pieces:
    # Bottom piece is always 1 (connected along the base)
    # Wait, no. The bottom pieces might be connected or separated.
    # 
    # Actually the paper is one connected sheet. After a horizontal cut at height h:
    # - Bottom part: all rectangles from 0 to h (or to A[i] if A[i] < h)
    # - Top part: portions of rectangles above h, but only those with A[i] > h
    #
    # The top part consists of contiguous groups of rectangles with A[i] > h
    # Each contiguous group forms one piece.
    # The bottom part is always 1 piece (all connected at the base).
    # 
    # So total pieces = 1 (bottom) + number of contiguous groups of rectangles with A[i] > h
    # 
    # But if h >= max(A), no cut happens through any rectangle, pieces = 1
    # If h = 0, all rectangles are above, so 1 contiguous group + bottom... 
    # Actually h must be between 1 and max(A)-1 for a meaningful cut.
    #
    # Number of contiguous groups with A[i] > h:
    # = number of i where A[i] > h and (i == 0 or A[i-1] <= h)
    # 
    # We want to maximize 1 + groups(h) over all valid h (1 <= h <= max(A)-1)
    # 
    # groups(h) = number of "starts" of runs where A[i] > h
    # A position i is a "start" if A[i] > h and (i==0 or A[i-1] <= h)
    #
    # For each position i that could be a start:
    # - If i == 0: it's a start when h < A[0], i.e., h in [1, A[0]-1]
    # - If i > 0: it's a start when A[i] > h and A[i-1] <= h, i.e., h in [A[i-1], A[i]-1]
    #   (h >= A[i-1] means A[i-1] <= h, and h < A[i] means h <= A[i]-1)
    #   But also h >= 1
    
    # For each potential start position i, it contributes 1 to groups(h) for h in some range.
    # We need to find h that maximizes sum of contributions.
    
    # Use a difference array approach on coordinate compressed values.
    
    # Collect all events
    from collections import defaultdict
    
    diff = defaultdict(int)
    
    for i in range(n):
        if i == 0:
            lo = 1
            hi = a[0] - 1
        else:
            lo = a[i-1]  # h >= a[i-1] (so a[i-1] <= h)
            hi = a[i] - 1  # h <= a[i]-1
            lo = max(lo, 1)
        
        if lo <= hi:
            diff[lo] += 1
            diff[hi + 1] -= 1
    
    if not diff:
        print(1)
        return
    
    keys = sorted(diff.keys())
    current = 0
    best = 0
    for k in keys:
        current += diff[k]
        if current > best:
            best = current
    
    print(1 + best)

solve()