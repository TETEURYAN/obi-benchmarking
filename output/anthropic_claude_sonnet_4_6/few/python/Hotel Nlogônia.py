import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    D = int(data[idx]); idx+=1
    W = int(data[idx]); idx+=1
    p = [int(data[idx+i]) for i in range(N)]
    idx += N

    # We need to choose a window of consecutive days [l, r] (0-indexed)
    # such that it contains exactly one contiguous block of D days (the "free" days)
    # and the remaining days cost <= W.
    # The free D days must be consecutive within [l, r].
    # We want to maximize r - l + 1.
    
    # For each possible placement of the D free days [i, i+D-1],
    # we can extend left and right as long as total cost <= W.
    # We want to maximize total length = D + left_extension + right_extension.
    
    # For a fixed free window [i, i+D-1]:
    # - We can add days to the left: days i-1, i-2, ... paying their costs
    # - We can add days to the right: days i+D, i+D+1, ... paying their costs
    # - Total paid cost <= W
    # We want to maximize left_ext + right_ext subject to sum of chosen days <= W
    # The optimal strategy: use two pointers / prefix sums
    
    # Precompute prefix sums
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + p[i]
    
    # For each free window start i (0-indexed), i in [0, N-D]:
    # Left costs: p[i-1], p[i-2], ..., p[0] (cumulative from i going left)
    # Right costs: p[i+D], p[i+D+1], ..., p[N-1] (cumulative from i+D going right)
    
    # For a fixed i, we want max left_ext + right_ext where:
    # sum(p[i-left_ext .. i-1]) + sum(p[i+D .. i+D+right_ext-1]) <= W
    
    # Two pointer approach over all i would be O(N) if we move i and adjust pointers.
    # But let's think differently:
    # 
    # For each i, precompute:
    # left_cost[j] = sum of j days to the left of i = prefix[i] - prefix[i-j]
    # right_cost[j] = sum of j days to the right of i+D-1 = prefix[i+D+j] - prefix[i+D]
    #
    # We want max (j + k) s.t. left_cost[j] + right_cost[k] <= W
    # 
    # For fixed i, if we fix left extension j, max right extension k is determined by binary search.
    # But iterating over all i and all j would be O(N^2).
    
    # Better approach: sliding window / two pointers across all i.
    # 
    # Key insight: as i increases by 1, the free window shifts right by 1.
    # The left boundary loses p[i-1] from left pool and gains p[i+D-1] ... wait no.
    # Actually when i increases by 1: left pool shrinks (loses leftmost available = p[i-1] becomes part of free... no)
    # 
    # Let me think with two pointers on the full window [l, r]:
    # The free D days are some [i, i+D-1] within [l, r].
    # Cost = prefix[i] - prefix[l] + prefix[r+1] - prefix[i+D]
    # = prefix[r+1] - prefix[l] - (prefix[i+D] - prefix[i])
    # We want to minimize cost for fixed [l,r], so maximize prefix[i+D] - prefix[i] (sum of D consecutive days in [l,r]).
    # 
    # So: for a fixed window [l, r] of length >= D, cost = (prefix[r+1] - prefix[l]) - max_D_sum_in_window
    # We want this cost <= W, and maximize r - l + 1.
    
    # Use sliding window (two pointers) on [l, r], maintaining max sum of D consecutive days.
    # For each r, find minimum l such that cost <= W.
    # Use a deque to maintain max of sliding window of size D sums.
    
    # Precompute sum of each D-window: s[i] = prefix[i+D] - prefix[i] for i in [0, N-D]
    # Then for window [l, r] (r-l+1 >= D), max D-sum = max(s[l], s[l+1], ..., s[r-D+1])
    # cost = prefix[r+1] - prefix[l] - max_s
    
    if D > N:
        print(0)
        return
    
    s = [prefix[i+D] - prefix[i] for i in range(N - D + 1)]
    
    # Two pointers: l and r, r goes from D-1 to N-1
    # Window [l, r] has length r-l+1 >= D
    # We need l <= r-D+1 (so that at least one D-window fits)
    # max_s = max(s[l..r-D+1])
    # cost = prefix[r+1] - prefix[l] - max_s <= W
    
    # Use a deque for sliding window maximum of s over indices [l, r-D+1]
    
    ans = D  # at minimum we can use just the D free days
    dq = deque()  # stores indices into s[], decreasing s values
    l = 0
    
    for r in range(D - 1, N):
        # New s index available: r - D + 1
        new_s_idx = r - D + 1
        # Add s[new_s_idx] to deque
        while dq and s[dq[-1]] <= s[new_s_idx]:
            dq.pop()
        dq.append(new_s_idx)
        
        # Now shrink l until cost <= W
        # cost = prefix[r+1] - prefix[l] - s[dq[0]]
        # But we need dq[0] >= l
        while True:
            # Remove expired front
            while dq and dq[0] < l:
                dq.popleft()
            max_s = s[dq[0]]
            cost = prefix[r+1] - prefix[l] - max_s
            if cost <= W:
                break
            l += 1
        
        ans = max(ans, r - l + 1)
    
    print(ans)

solve()