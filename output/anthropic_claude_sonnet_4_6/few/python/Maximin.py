import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    L = int(data[1])
    R = int(data[2])
    a = sorted(int(data[3 + i]) for i in range(n))
    
    # For a chosen value x in [L, R], the pessimistic score is min |a_i - x| over all i.
    # We want to maximize this over x in [L, R].
    
    # The function f(x) = min_i |a_i - x| is piecewise linear.
    # Its maximum occurs either at the endpoints L, R, or at midpoints between consecutive a_i values.
    
    # Candidate points: L, R, and midpoints between consecutive sorted a values.
    
    def min_diff(x, a):
        # Binary search for closest element in sorted a
        import bisect
        pos = bisect.bisect_left(a, x)
        best = float('inf')
        if pos < len(a):
            best = min(best, abs(a[pos] - x))
        if pos > 0:
            best = min(best, abs(a[pos-1] - x))
        return best
    
    import bisect
    
    best = 0
    
    # Check endpoints
    best = max(best, min_diff(L, a))
    best = max(best, min_diff(R, a))
    
    # Check midpoints between consecutive elements
    for i in range(len(a) - 1):
        # midpoint between a[i] and a[i+1]
        # For integer x, the best x in [a[i], a[i+1]] maximizing min dist is floor((a[i]+a[i+1])/2) or ceil
        mid_floor = (a[i] + a[i+1]) // 2
        mid_ceil = (a[i] + a[i+1] + 1) // 2
        for mid in [mid_floor, mid_ceil]:
            if L <= mid <= R:
                best = max(best, min_diff(mid, a))
    
    # Also check: what if the optimal x is to the left of all a_i or right of all a_i?
    # That's covered by L and R endpoints already, but let's also consider:
    # If L < a[0], then f(x) = a[0] - x for x <= a[0], maximized at x = L (already checked)
    # If R > a[-1], then f(x) = x - a[-1] for x >= a[-1], maximized at x = R (already checked)
    
    print(best)

solve()