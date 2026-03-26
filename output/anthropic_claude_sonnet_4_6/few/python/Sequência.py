import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    L = int(data[idx]); idx+=1
    H = int(data[idx]); idx+=1
    
    s = [int(data[idx+i]) for i in range(N)]; idx+=N
    m = [int(data[idx+i]) for i in range(N)]; idx+=N
    
    # prefix sums
    prefix = [0] * (N+1)
    for i in range(N):
        prefix[i+1] = prefix[i] + s[i]
    
    # marked_prefix[i] = number of marked elements in s[0..i-1]
    marked = [0] * (N+1)
    for i in range(N):
        marked[i+1] = marked[i] + m[i]
    
    # We want max of prefix[j] - prefix[i] where L <= marked[j] - marked[i] <= H
    # i.e., marked[j] - H <= marked[i] <= marked[j] - L
    # For each j from 0 to N, we want min prefix[i] where marked[i] in [marked[j]-H, marked[j]-L]
    # and i <= j
    
    # Since marked values go from 0 to total_marked (up to N),
    # and H <= 20, we can use a sliding window approach.
    
    # Group indices by their marked count value.
    # For each j, we need min prefix[i] for i <= j with marked[i] in [marked[j]-H, marked[j]-L]
    
    # We'll iterate j from 0 to N.
    # We maintain for each possible marked count c, the minimum prefix[i] seen so far with marked[i]=c
    
    # Since H <= 20, for each j we only look at at most H-L+1 <= 21 values of c.
    
    INF = float('inf')
    
    # min_prefix_by_mark[c] = minimum prefix[i] among all i seen so far with marked[i] = c
    max_marked = marked[N]
    min_prefix_by_mark = [INF] * (max_marked + 1)
    
    ans = -INF
    
    for j in range(N+1):
        mj = marked[j]
        # Update min_prefix_by_mark with index j (as potential i for future j's)
        # But we need i <= j, so we add j to the structure before processing j as endpoint? No.
        # Actually i < j or i == j means empty subarray if i==j.
        # The subarray is s[i..j-1] with sum prefix[j]-prefix[i], i can equal j (empty).
        # We want i <= j.
        # So we should add i=j to structure, then query for j as right endpoint.
        # Wait: subarray from i+1 to j (1-indexed) = prefix[j]-prefix[i], i from 0 to j.
        # So i ranges 0..j, meaning we add i=j before querying j as right endpoint.
        
        # Add current j as a potential left boundary (i = j)
        if mj <= max_marked:
            if prefix[j] < min_prefix_by_mark[mj]:
                min_prefix_by_mark[mj] = prefix[j]
        
        # Query: find min prefix[i] with marked[i] in [mj - H, mj - L]
        # But this would give subarray ending at j with marked count in [L, H]
        # Wait, we need marked[j] - marked[i] in [L, H]
        # => marked[i] in [marked[j]-H, marked[j]-L]
        lo = mj - H
        hi = mj - L
        
        if hi < 0:
            continue
        lo = max(lo, 0)
        if lo > hi:
            continue
        
        for c in range(lo, hi+1):
            if c <= max_marked and min_prefix_by_mark[c] < INF:
                val = prefix[j] - min_prefix_by_mark[c]
                if val > ans:
                    ans = val
    
    print(ans)

solve()