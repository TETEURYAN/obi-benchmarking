Looking at this problem, I need to split N buildings into two groups to minimize the maximum Manhattan distance between any two buildings in the same group.

Key insight: Binary search on the answer D. For a given D, can we split buildings into two groups such that the diameter (max pairwise Manhattan distance) of each group is ≤ D?

Manhattan distance: |xi - xj| + |yi - yj| ≤ D

The Manhattan distance can be transformed: |xi - xj| + |yi - yj| = max(|(xi+yi)-(xj+yj)|, |(xi-yi)-(xj-yj)|)... wait, actually that's the Chebyshev transformation.

Actually, |xi-xj| + |yi-yj| ≤ D iff max(|(xi+yi)-(xj+yj)|, |(xi-yi)-(xj-yj)|) ≤ D after rotation. Let u = x+y, v = x-y. Then Chebyshev distance = max(|ui-uj|, |vi-vj|) = Manhattan distance.

So the diameter in Manhattan = diameter in Chebyshev (max(|ui-uj|, |vi-vj|)).

For a set to have Chebyshev diameter ≤ D: max(u) - min(u) ≤ D AND max(v) - min(v) ≤ D.

So I need to split points into two groups where each group fits in a rectangle of size D×D in (u,v) space.

Binary search on D. For fixed D, check if we can partition into two groups each with u-range ≤ D and v-range ≤ D.

The overall u-range is [umin, umax]. If umax - umin ≤ D, the u constraint is satisfied for any split. Similarly for v.

If umax - umin > D: we must separate points with u < umin+D from points with u > umax-D... Actually we need to split so that each group's u-range ≤ D. This means one group has all points with u ≤ some threshold, and the other has the rest (sorted by u). But we also need v-range ≤ D for each group.

Strategy for checking feasibility with diameter D:
- Sort by u. The split must be: group A = points with u ≤ some cutoff, group B = rest (or some subset). But it's more complex.
- Actually: if we must split by u, the only valid splits are: group1 has u in [umin, umin+D], group2 has u in [umax-D, umax]. Points in the overlap [umax-D, umin+D] can go to either group.
- For each such split, check if v-ranges are ≤ D.

Let me think more carefully. Sort points by u. For a given D:
- Points with u > umin + D MUST go to group B (can't be with umin point)
- Points with u < umax - D MUST go to group A (can't be with umax point)
- If umin+D < umax-D: impossible (some point can't be in either group alone... wait they'd need to be separated from both extremes)

Actually if there exist points that can't coexist with umin AND can't coexist with umax, it's impossible.

Let me implement: sort by u. Find which points must be in "left" group (can't be with umax), which must be in "right" group (can't be with umin), and which are flexible. Check v-ranges.

import sys
from math import inf

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    X = [int(input_data[idx+i]) for i in range(n)]; idx+=n
    Y = [int(input_data[idx+i]) for i in range(n)]; idx+=n
    
    U = [X[i]+Y[i] for i in range(n)]
    V = [X[i]-Y[i] for i in range(n)]
    
    points = sorted(zip(U, V))
    us = [p[0] for p in points]
    vs = [p[1] for p in points]
    
    def check(D):
        umin, umax = us[0], us[-1]
        if umax - umin <= D:
            vmin, vmax = min(vs), max(vs)
            if vmax - vmin <= D: return True
        # Split: left group u in [umin, umin+D], right group u in [umax-D, umax]
        # Find boundary using binary search
        import bisect
        cut1 = bisect.bisect_right(us, umin + D)  # points 0..cut1-1 can be in left
        cut2 = bisect.bisect_left(us, umax - D)   # points cut2..n-1 can be in right
        if cut2 > cut1: return False  # some points can't be in either
        # Points 0..cut2-1 must be in left, cut1..n-1 must be in right, cut2..cut1-1 flexible
        # Left group: 0..cut1-1 (must include 0..cut2-1, flexible cut2..cut1-1 go left)
        # Right group: cut2..n-1
        # Check both v-ranges
        # Left = 0..cut1-1, Right = cut2..n-1
        lv = vs[:cut1]; rv = vs[cut2:]
        if not lv or not rv: 
            all_v = vs; return max(all_v)-min(all_v) <= D
        if max(lv)-min(lv) <= D and max(rv)-min(rv) <= D: return True
        # Also try left=0..cut2-1 flexible go right: left=0..cut2-1, right=cut2..n-1... but cut2 might not cover
        # Try all splits at each flexible point
        # flexible points are cut2..cut1-1, try split at each
        # precompute prefix max/min v for left, suffix max/min v for right
        pre_vmax = [0]*n; pre_vmin = [0]*n
        pre_vmax[0] = pre_vmin[0] = vs[0]
        for i in range(1,n):
            pre_vmax[i] = max(pre_vmax[i-1], vs[i])
            pre_vmin[i] = min(pre_vmin[i-1], vs[i])
        suf_vmax = [0]*n; suf_vmin = [0]*n
        suf_vmax[-1] = suf_vmin[-1] = vs[-1]
        for i in range(n-2,-1,-1):
            suf_vmax[i] = max(suf_vmax[i+1], vs[i])
            suf_vmin[i] = min(suf_vmin[i+1], vs[i])
        for split in range(cut2, cut1+1):
            # left = 0..split-1, right = split..n-1
            if split == 0:
                rv_range = suf_vmax[0]-suf_vmin[0]
                if rv_range <= D: return True
                continue
            if split == n:
                lv_range = pre_vmax[n-1]-pre_vmin[n-1]
                if lv_range <= D: return True
                continue
            lv_range = pre_vmax[split-1]-pre_vmin[split-1]
            rv_range = suf_vmax[split]-suf_vmin[split]
            if lv_range <= D and rv_range <= D: return True
        return False
    
    lo, hi = 0, 2*10**9
    while lo < hi:
        mid = (lo+hi)//2
        if check(mid): hi = mid
        else: lo = mid+1
    print(lo)

solve()