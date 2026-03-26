import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1
    
    a = []
    for i in range(N):
        a.append(int(data[idx])); idx += 1
    
    b = []
    for i in range(N):
        b.append(int(data[idx])); idx += 1
    
    # positions of friends (1-indexed)
    top = [i for i in range(N) if a[i] == 1]
    bot = [i for i in range(N) if b[i] == 1]
    
    # We need to find a matching between top and bot positions
    # such that each matched pair occupies the same column,
    # and the total number of swaps is minimized.
    # 
    # The cost to move a person from position p to position q on one side
    # is |p - q| swaps (bubble sort style).
    # But we need to be careful: moving multiple people on the same side
    # costs the sum of individual moves only if they don't cross each other
    # (if they maintain relative order, no extra cost).
    #
    # Key insight: The optimal solution pairs top[i] with bot[sigma(i)]
    # for some permutation sigma. The cost on the top side is the number of
    # swaps to sort top positions to the target positions, and similarly for bot.
    # 
    # For a fixed set of K target columns (positions where pairs meet),
    # the optimal assignment is: sort top positions -> assign to sorted targets,
    # sort bot positions -> assign to sorted targets.
    # The cost is sum|top_sorted[i] - targets_sorted[i]| + sum|bot_sorted[i] - targets_sorted[i]|
    # 
    # But we need to choose the targets optimally.
    # 
    # Actually, the targets must be K distinct positions from 0..N-1.
    # We want to minimize sum|top[i] - t[i]| + sum|bot[i] - t[i]| where t is sorted targets
    # and top, bot are sorted.
    # 
    # This is equivalent to: for each i, choose t[i] to minimize |top[i]-t[i]| + |bot[i]-t[i]|
    # subject to t being strictly increasing integers.
    # 
    # Without the constraint, optimal t[i] is any value between min(top[i],bot[i]) and max(top[i],bot[i]).
    # Cost for pair i = |top[i] - bot[i]|.
    # 
    # With the constraint that t must be strictly increasing integers, we use DP.
    # 
    # DP: dp[i][j] = min cost to assign targets to first i pairs where t[i] = j
    # dp[i][j] = min over j' < j of dp[i-1][j'] + cost(i, j)
    # cost(i, j) = |top[i] - j| + |bot[i] - j|
    # 
    # N up to 150000, K up to 150000 -> O(K*N) too slow.
    # 
    # Better: use the fact that optimal t[i] without constraints is in [lo[i], hi[i]]
    # where lo[i] = min(top[i],bot[i]), hi[i] = max(top[i],bot[i]).
    # Cost(i,j) = |top[i]-j| + |bot[i]-j| = hi[i]-lo[i] if lo[i]<=j<=hi[i], else distance to interval * 2 + hi[i]-lo[i]... 
    # Actually cost(i,j) = max(top[i],bot[i]) - min(top[i],bot[i]) when j in [lo,hi], else |j-lo|+|j-hi| + ... 
    # cost(i,j) = |top[i]-j|+|bot[i]-j|
    
    top.sort()
    bot.sort()
    
    # DP with slope trick or SMAWK - use DP O(K^2) won't work for K=150000
    # Use the observation: optimal unconstrained t[i] in [lo[i],hi[i]]
    # and the constraint is t strictly increasing.
    # This is the "isotonic regression" style problem.
    # 
    # Since cost(i,j) is convex in j, and we want min sum cost(i, t[i]) with t[i] < t[i+1],
    # we can use slope trick DP.
    
    # Slope trick DP for strictly increasing sequence
    # Transform: let s[i] = t[i] - i, then s must be non-decreasing (s[i] <= s[i+1])
    # cost'(i, s) = cost(i, s+i) = |top[i]-(s+i)| + |bot[i]-(s+i)|
    
    import heapq
    
    # Slope trick: maintain the piecewise linear function as two heaps
    # We process each i, add cost'(i,s), then enforce s[i] <= s[i+1] (non-decreasing)
    
    # For non-decreasing constraint with slope trick:
    # After adding cost for position i, the DP function is convex PL.
    # For next position, we just add next cost (no need to clip since non-decreasing is handled by not allowing decrease)
    
    INF = float('inf')
    
    # slope trick for sum of convex functions with non-decreasing constraint
    # Use max-heap (left) and min-heap (right) - but here we just need the minimum
    
    # Actually for non-decreasing (s[0]<=s[1]<=...<=s[K-1]):
    # Standard slope trick: maintain left heap (max-heap of breakpoints on left side)
    
    # f(s) after processing i terms, convex PL
    # Adding new term g(s) = |a - s| + |b - s| where a=top[i]-i, b=bot[i]-i
    # g has breakpoints at min(a,b) and max(a,b), slope goes -2, 0 (if a!=b) or -2,+2 (if a==b... wait)
    # g(s) = |a-s|+|b-s|: slope is -2 for s<min(a,b), 0 for min(a,b)<=s<=max(a,b), +2 for s>max(a,b)
    # (when a==b, slope is -2 then +2)
    
    # Slope trick with left heap (max-heap):
    # We track the minimum value and the left breakpoints
    
    total_base = sum(abs(top[i]-bot[i]) for i in range(K))
    
    # Use slope trick
    # f starts at 0 (empty)
    # left heap: max-heap of left breakpoints (slopes go from negative to 0)
    # We only need left heap since we want minimum and enforce non-decreasing
    
    # For non-decreasing constraint in slope trick:
    # When adding new function, if new left breakpoint < current max of left heap,
    # we need to "push down" - but for non-decreasing we don't restrict from above.
    # Actually for non-decreasing s[i], the DP is:
    # dp[i](s) = min_{s'<=s} dp[i-1](s') + cost_i(s)
    # The "min_{s'<=s}" operation on a convex function f gives a non-increasing then flat function
    # which equals f for s >= argmin(f), and min(f) for s < argmin(f).
    # But since cost_i is also convex, the sum remains convex after this.
    # 
    # Slope trick: the left heap represents breakpoints where slope increases by 1 each.
    # For the "prefix min" operation (non-decreasing constraint), we remove all right breakpoints
    # (making the function flat to the right of minimum). But we only track left heap here.
    
    # Let me implement standard slope trick for this.
    # We maintain: min_val (current minimum of DP function), L = max-heap of left breakpoints
    # The function is: min_val + sum of max(0, l - s) * 2 ... 
    # Actually each breakpoint in L contributes a slope change of +2 (going left to right, slope increases by 2 at each breakpoint... no)
    
    # Let me think more carefully.
    # g_i(s) = |top[i]-i - s| + |bot[i]-i - s|
    # Let li = min(top[i]-i, bot[i]-i), ri = max(top[i]-i, bot[i]-i)
    # g_i(s) = (ri - li) + 2*max(0, li - s) + 2*max(0, s - ri)
    # So base cost = ri - li = |top[i]-bot[i]|, already counted in total_base
    # Extra cost = 2*max(0, li-s) + 2*max(0, s-ri)
    
    # DP with non-decreasing constraint:
    # dp[0](s) = g_0(s)
    # dp[i](s) = min_{s'<=s} dp[i-1](s') + g_i(s)
    
    # Slope trick: maintain left heap L (max-heap), right heap R (min-heap), and min_val
    # For non-decreasing: after computing dp[i-1] + g_i, apply prefix-min (remove right heap)
    # But since we enforce non-decreasing at each step, right heap becomes empty after prefix-min.
    # Wait, but then next g_i might add right breakpoints again.
    
    # Standard approach: since we enforce non-decreasing at each step,
    # after prefix-min the function is non-increasing then flat (no right part).
    # Then adding g_i (which has both left and right parts) gives a function with right part = right part of g_i.
    # Then we apply prefix-min again (remove right part).
    # So effectively we never need the right heap!
    # The minimum of dp[i] = min of (prefix-min of dp[i-1]) + g_i
    # = min_val_{i-1} + min_s(g_i(s)) ... no that's not right either.
    
    # Let me reconsider. After prefix-min operation on dp[i-1]:
    # h(s) = min_{s'<=s} dp[i-1](s') = dp[i-1](s) for s >= s*, min_val for s < s*
    # where s* = argmin dp[i-1].
    # h is non-decreasing (flat then increasing... wait no: h is non-decreasing because it's the running minimum from left... 
    # Actually h(s) = min_{s'<=s} dp[i-1](s'): as s increases, we take min over larger set, so h is non-increasing!
    # h is non-increasing.
    # Then dp[i](s) = h(s) + g_i(s).
    # h is non-increasing (flat at min_val for s>=s*, then increasing going left... 
    # h(s) for s < s* equals dp[i-1](s) which is > min_val and decreasing as s->s*
    # h(s) for s >= s* equals min_val (flat)
    # So h is non-increasing then flat. It's a convex function? No, it's concave then flat... 
    # Hmm, h is actually: decreasing (following dp[i-1] which is convex, so left part is decreasing) until s*, then flat.
    # So h is non-increasing. Not convex in general.
    
    # I think I'm overcomplicating this. Let me use a different approach.
    
    # The key insight: the optimal targets t[0] < t[1] < ... < t[K-1] (sorted)
    # paired with sorted top and sorted bot.
    # 
    # This is equivalent to: choose K distinct integers from {0,...,N-1},
    # minimize sum_i (|top[i] - t[i]| + |bot[i] - t[i]|).
    # 
    # This can be solved with DP:
    # dp[i][j] = min cost using first i pairs, last target = j
    # dp[i][j] = min_{j'<j} dp[i-1][j'] + |top[i]-j| + |bot[i]-j|
    # 
    # With slope trick this is O(K log K) or O(N log N).
    
    # Let's implement slope trick properly.
    # 
    # dp[i](x) = min_{y < x} dp[i-1](y) + cost_i(x)   [strictly increasing: y < x, i.e., y <= x-1]
    # 
    # Transform: x -> x (keep as is, strictly increasing means x[i+1] >= x[i]+1)
    # Substitute x_i = t_i - i (so x non-decreasing, x[i+1] >= x[i])
    # Wait strictly increasing t means t[i+1] >= t[i]+1, so t[i+1]-（i+1) >= t[i]-i, i.e., x non-decreasing.
    # cost_i(t) = |top[i]-t| + |bot[i]-t|, with t = x+i:
    # cost_i(x) = |top[i]-i-x| + |bot[i]-i-x|
    # Let A[i] = top[i]-i, B[i] = bot[i]-i
    # cost_i(x) = |A[i]-x| + |B[i]-x|
    # 
    # Now problem: choose x[0] <= x[1] <= ... <= x[K-1] (integers, but actually can be equal now)
    # minimize sum cost_i(x[i])
    # 
    # This is isotonic regression with L1 cost (sum of two L1 terms = still L1-like).
    # 
    # Slope trick for non-decreasing sequence:
    # Process i=0..K-1:
    # dp[i](x) = min_{y<=x} dp[i-1](y) + cost_i(x)
    # 
    # The "min_{y<=x} dp[i-1](y)" = prefix minimum of dp[i-1], call it h_{i-1}(x).
    # h_{i-1} is non-increasing (as x grows, min over larger set can only decrease or stay).
    # Wait: h(x) = min_{y<=x} f(y). As x increases, we include more y values, so h(x) is non-increasing. Yes.
    # 
    # Then dp[i](x) = h_{i-1}(x) + cost_i(x).
    # h_{i-1} is non-increasing, cost_i is convex (V-shaped or flat-bottomed V).
    # Their sum is... not necessarily convex.
    # 
    # Hmm. But actually for the isotonic regression problem with convex costs,
    # the DP function dp[i] IS convex. Let me verify:
    # dp[0](x) = cost_0(x) = convex. ✓
    # h_0(x) = min_{y<=x} dp[0](y) = dp[0](x) for x <= argmin, min_val for x >= argmin.
    # This is non-increasing then flat = convex? No: it's decreasing then flat, which is convex (the slope is non-decreasing: goes from negative to 0). Yes! It IS convex.
    # dp[1](x) = h_0(x) + cost_1(x) = sum of two convex functions = convex. ✓
    # By induction, dp[i] is always convex. ✓
    # 
    # So slope trick works! And since after prefix-min the function is still convex (non-increasing then flat),
    # we can maintain it with slope trick.
    # 
    # Slope trick representation: convex PL function f with integer breakpoints.
    # Maintain: min_val, left heap L (max-heap of breakpoints where slope increases, left of minimum),
    #           right heap R (min-heap of breakpoints where slope increases, right of minimum).
    # Each breakpoint appears with multiplicity = slope change at that point.
    # 
    # For cost_i(x) = |A-x| + |B-x| (A=A[i], B=B[i]):
    # Breakpoints: at min(A,B) slope changes by +2 (from -2 to 0 or -2 to... wait)
    # slope of |A-x|: -1 for x<A, +1 for x>A
    # slope of |B-x|: -1 for x<B, +1 for x>B
    # sum: slope = -2 for x < min(A,B), 0 for min(A,B) < x < max(A,B), +2 for x > max(A,B)
    # (if A==B: slope = -2 for x<A, +2 for x>A)
    # Breakpoints: min(A,B) with slope change +2, max(A,B) with slope change +2.
    # 
    # Prefix-min operation on convex f:
    # h(x) = min_{y<=x} f(y)
    # This removes the right part (all right breakpoints), making f flat after its minimum.
    # In slope trick: clear the right heap R, keep L and min_val.
    # 
    # Adding cost_i(x) to h(x):
    # h has slope: ... (from L heap) ... 0 (flat after minimum, no right breakpoints)
    # Adding cost_i adds breakpoints min(A,B) and max(A,B) to appropriate heaps.
    # 
    # But we need to maintain the heap invariant (all L elements <= all R elements).
    # 
    # Let me implement this step by step:
    # 
    # State: (min_val, L=max-heap, R=min-heap)
    # Initially: min_val=0, L=[], R=[]  (f(x) = 0 for all x, but that's not right for empty)
    # Actually for i=0, we start with f(x) = 0 (before adding any cost), then add cost_0.
    # 
    # Operation "add convex function g with breakpoints p, q (p<=q), base value g_min":
    #   min_val += g_min
    #   Add p to L, q to R (tentatively)
    #   Fix heap invariant:
    #     if L.top > R.top: swap them (move L.top to R, R.top to L), adjust min_val
    #     Actually standard slope trick add for |x - m|: push m to L and R, then fix.
    # 
    # Hmm, let me just implement the standard slope trick for this problem.
    # 
    # For each i:
    #   1. Apply prefix-min: clear R (set R = [])  -- makes function non-increasing then flat
    #   2. Add cost_i(x) = |A[i]-x| + |B[i]-x|:
    #      Let lo = min(A[i],B[i]), hi = max(A[i],B[i])
    #      This adds slope -2 at lo and +2 at hi (i.e., two copies of lo to L-side, two copies of hi to R-side... 
    #      Actually slope changes: at lo, slope increases by 2; at hi, slope increases by 2.
    #      Before lo: slope contribution -2; between lo,hi: 0; after hi: +2.
    #      So we add lo twice to the "left breakpoints" and hi twice to "right breakpoints"? 
    #      No. The breakpoints are where slope changes. Left breakpoints are those <= argmin, right are > argmin.
    # 
    # I think the cleanest way: represent the function by its slope changes.
    # Use a max-heap for left breakpoints (each stored once, slope changes by +1 each... 
    # but here slope changes by +2 at each breakpoint of cost_i).
    # 
    # Alternative: just use two copies. Push lo twice to heap, hi twice to heap, then fix.
    # 
    # Let me look at this more carefully with the standard slope trick.
    # 
    # Standard slope trick for sum of |x - c_i|:
    # Each |x - c_i| adds breakpoint c_i to both L and R (or equivalently, adds c_i once to L and once to R).
    # After adding, fix: if L.max > R.min, pop both, swap, push back, adjust min_val.
    # 
    # For our cost_i = |x - A| + |x - B| = two terms:
    # Add |x - A|: push A to L and R, fix.
    # Add |x - B|: push B to L and R, fix.
    # But we also do prefix-min before each addition (except first).
    # 
    # After prefix-min (clear R), when we add |x - c|:
    # Push c to L. Now L.max might be > R.min (but R is empty, so no issue).
    # Push c to R. Now check if L.max > R.min: if so, fix.
    # 
    # Wait, after prefix-min R is empty. Then:
    # Add |x - A|:
    #   Push A to L: L = [..., A]
    #   Push A to R: R = [A]
    #   Check: L.max vs R.min = A vs A: equal, no swap needed? 
    #   Hmm but L.max could be > A if previous L had larger elements.
    #   If L.max > R.min: pop l=L.max, pop r=R.min, min_val += l - r, push r to L, push l to R.
    # 
    # This is getting complex. Let me just implement it carefully.
    
    # Actually, I realize: after prefix-min, R is cleared. The function is non-increasing then flat.
    # Its slope is <= 0 everywhere (non-positive). The minimum is achieved for all x >= some threshold.
    # In terms of heaps: L contains all the breakpoints (where slope increases by 1 each, going left to right).
    # R is empty.
    # 
    # When we add |x - c| (slope -1 for x<c, +1 for x>c):
    # The new function = old + |x-c|.
    # Old function has slope <= 0 everywhere (non-increasing then flat).
    # New function: slope changes at c by +2 (from |x-c|: slope -1 before c, +1 after c, change = +2... 
    # wait |x-c| has slope -1 for x<c and +1 for x>c, so slope change at c is +2? No: slope goes from -1 to +1, change = +2. Hmm but usually we say slope change = +1 at c for |x-c|... 
    # Oh I see, |x-c| has slope change +2 at c (from -1 to +1). But in standard slope trick for sum of |x-c_i|, each term contributes slope change +2 at c_i... but we usually say each term contributes one breakpoint to L and one to R.
    # 
    # I think the confusion is: in standard slope trick, we track breakpoints where slope increases by 1.
    # For |x - c|: slope is -1 then +1, so slope increases by 1 at c (from the left heap perspective, c is added once) and increases by 1 at c again (from right heap, c is added once). So c appears in both L and R.
    # 
    # OK let me just implement it with the understanding that each |x-c| adds c to both L and R.
    
    # FINAL IMPLEMENTATION:
    
    import heapq
    
    L = []  # max-heap (store negatives)
    R = []  # min-heap
    min_val = 0
    
    for i in range(K):
        # Step 1: prefix-min (clear R)
        # After clearing R, function is non-increasing then flat (slope <= 0 everywhere)
        R.clear()
        
        # Step 2: add cost_i(x) = |A[i] - x| + |B[i] - x|
        # = |x - A[i]| + |x - B[i]|
        # Add two terms: |x - A[i]| and |x - B[i]|
        
        for c in [top[i] - i, bot[i] - i]:
            # Add |x - c| to current function
            # Push c to L and R
            heapq.heappush(L, -c)
            heapq.heappush(R, c)
            # Fix: if L.max > R.min
            l_max = -L[0]
            r_min = R[0]
            if l_max > r_min:
                heapq.heappop(L)
                heapq.heappop(R)
                min_val += l_max - r_min
                heapq.heappush(L, -r_min)
                heapq.heappush(R, l_max)
    
    print(min_val)

solve()