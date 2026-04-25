import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = [int(data[i+1]) for i in range(n)]
    
    # For a horizontal cut at height h (0 < h <= max(a)):
    # A rectangle i is "cut" if h <= a[i] (the cut passes through it)
    # A rectangle i is "not cut" if h > a[i] (the cut is above it, so it doesn't exist at that height)
    # 
    # The number of pieces = number of connected groups of rectangles that are cut
    # plus 1 for the base piece (below the cut) if any rectangle is cut
    # Wait, let me think more carefully.
    #
    # When we cut at height h:
    # - Rectangles with a[i] >= h are intersected by the cut
    # - Rectangles with a[i] < h are completely below the cut
    #
    # The pieces are:
    # 1. The bottom part: all rectangles form one connected piece below the cut
    #    (they're all connected at the base) -> 1 piece
    # 2. The top parts: each contiguous group of rectangles with a[i] >= h
    #    forms a separate top piece
    #
    # So total pieces = 1 + (number of contiguous groups of rectangles with a[i] >= h)
    # But only if there's at least one rectangle with a[i] >= h (otherwise no cut happens meaningfully)
    # Actually if no rectangle has a[i] >= h, the cut doesn't intersect anything -> 1 piece (no cut effect)
    # If all rectangles have a[i] < h, cut is above all -> 1 piece
    #
    # We want to maximize: 1 + number_of_groups(h)
    # where number_of_groups(h) = number of maximal contiguous runs where a[i] >= h
    #
    # The number of groups changes only at values h = a[i] for some i.
    # We need to find the h that maximizes the number of contiguous groups of indices with a[i] >= h.
    #
    # Key insight: as h increases, some rectangles drop out (those with a[i] < h).
    # The number of groups can be computed for each distinct height value.
    #
    # For each possible cut height h (which must be one of the a[i] values to be optimal,
    # or any value between consecutive distinct heights - but groups only change at a[i] values),
    # we need: count of i where a[i] >= h AND (i==0 OR a[i-1] < h)
    # = number of "starts" of runs
    #
    # A position i is a "start of a run at height h" if a[i] >= h and (i==0 or a[i-1] < h)
    # 
    # For each position i, it contributes a "start" for all h in (a[i-1], a[i]] if a[i] > a[i-1] (or i==0)
    # Actually: position i is a start for height h iff a[i] >= h and (i==0 or a[i-1] < h)
    # i.e., h <= a[i] and (i==0 or h > a[i-1])
    # So for i==0: h in [1, a[0]] -> contributes to all h in [1, a[0]]
    # For i>0: h in [a[i-1]+1, a[i]] if a[i] > a[i-1], else no contribution as a start
    #   (if a[i] <= a[i-1], then whenever h <= a[i], we also have h <= a[i-1] so i-1 is also active, not a start)
    #
    # We want to maximize number_of_groups(h) = sum of starts at height h
    # 
    # Use a difference array / event-based approach on distinct heights.
    
    # For each i, compute the interval of h where i is a "group start":
    # h in [lo, hi] where lo = a[i-1]+1 (or 1 if i==0), hi = a[i]
    # Only valid if lo <= hi
    
    from collections import defaultdict
    
    events = defaultdict(int)
    
    for i in range(n):
        hi = a[i]
        lo = a[i-1] + 1 if i > 0 else 1
        if lo <= hi:
            events[lo] += 1
            events[hi + 1] -= 1
    
    # Sweep through sorted event points
    sorted_keys = sorted(events.keys())
    
    max_groups = 0
    current = 0
    
    for k in sorted_keys:
        current += events[k]
        if current > max_groups:
            max_groups = current
    
    print(1 + max_groups)

solve()