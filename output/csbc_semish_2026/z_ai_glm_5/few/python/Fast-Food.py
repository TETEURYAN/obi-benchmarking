import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    X = []
    Y = []
    for _ in range(N):
        X.append(int(next(iterator)))
    
    for _ in range(N):
        Y.append(int(next(iterator)))

    if N <= 1:
        print(0)
        return

    points = []
    for i in range(N):
        points.append((X[i] + Y[i], X[i] - Y[i]))
    
    # Sort by u
    points.sort(key=lambda p: p[0])
    u_vals = [p[0] for p in points]
    
    # We need v values in the order of u-sorted points
    v_vals_in_u_order = [p[1] for p in points]
    
    # Sort by v to determine ranks
    # We store pairs (v_value, original_index_in_u_sorted_array) to track positions
    indexed_v = [(v_vals_in_u_order[i], i) for i in range(N)]
    indexed_v.sort(key=lambda p: p[0])
    
    # rank_in_v[i] stores the rank of the i-th point (in u-sorted order) in the v-sorted order
    rank_in_v = [0] * N
    v_vals = [0] * N
    for r, (v, idx) in enumerate(indexed_v):
        rank_in_v[idx] = r
        v_vals[r] = v

    # Precompute prefix max/min of ranks in v for the u-sorted array
    # pref_max_v[i] = max rank in v among first i+1 points in u-sorted order
    pref_max_v = [0] * N
    pref_min_v = [0] * N
    
    pref_max_v[0] = rank_in_v[0]
    pref_min_v[0] = rank_in_v[0]
    for i in range(1, N):
        pref_max_v[i] = max(pref_max_v[i-1], rank_in_v[i])
        pref_min_v[i] = min(pref_min_v[i-1], rank_in_v[i])

    # Binary search for the answer
    # Range of distance: 0 to 2 * 10^9
    low = -1
    high = 2000000000 + 1
    
    def check(K):
        # Find gaps in u
        # A gap is where u[i+1] - u[i] > K
        # We need at most one such gap.
        
        # Optimization: Find first and last gap
        # Since u is sorted, u[i+1] - u[i] > K implies all points j <= i are separated from k >= i+1
        # Actually, we just need to count gaps.
        # If count > 1, impossible.
        # If count == 1, store index.
        
        u_gap_idx = -1
        u_gap_count = 0
        
        # We can iterate, but since we do this multiple times, 
        # and the condition is monotonic, we can't precompute indices easily
        # because the threshold K changes.
        # However, N is small enough for O(N) check inside O(log Range).
        
        for i in range(N - 1):
            if u_vals[i+1] - u_vals[i] > K:
                u_gap_count += 1
                if u_gap_count > 1:
                    return False
                u_gap_idx = i
        
        v_gap_idx = -1
        v_gap_count = 0
        for i in range(N - 1):
            if v_vals[i+1] - v_vals[i] > K:
                v_gap_count += 1
                if v_gap_count > 1:
                    return False
                v_gap_idx = i
        
        # If no gaps in both, valid
        if u_gap_count == 0 and v_gap_count == 0:
            return True
        
        # If one has gaps > 1, already returned False
        
        # If one has 1 gap and other has 0, valid
        if u_gap_count == 0 or v_gap_count == 0:
            return True
            
        # Both have exactly 1 gap
        # u_gap_idx is the index of the last element of the left set in u-sorted order
        # The set is points 0 to u_gap_idx.
        # v_gap_idx is the index of the last element of the left set in v-sorted order
        # The set is points 0 to v_gap_idx.
        
        k = u_gap_idx
        m = v_gap_idx
        
        # We need to check if the u-left-set is contained in v-left-set OR v-right-set
        # u-left-set: indices 0..k in u-sorted array
        # Their ranks in v are rank_in_v[0]...rank_in_v[k]
        # We need max and min of these ranks.
        
        max_r = pref_max_v[k]
        min_r = pref_min_v[k]
        
        # v-left-set corresponds to ranks 0..m
        # v-right-set corresponds to ranks m+1..N-1
        
        # Condition 1: u-left-set subset of v-left-set
        # All ranks must be <= m
        if max_r <= m:
            return True
            
        # Condition 2: u-left-set subset of v-right-set
        # All ranks must be > m
        if min_r > m:
            return True
            
        return False

    while high - low > 1:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid

    print(high)

if __name__ == '__main__':
    solve()