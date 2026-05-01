import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    # Classic egg drop problem
    # Find minimum number of trials t such that we can check N floors with K eggs
    # With t trials and k eggs, max floors we can check = C(t,1) + C(t,2) + ... + C(t,k)
    # We need this sum >= N
    
    # Binary search on t
    # For a given t, compute sum of C(t,1)+...+C(t,min(t,K))
    # If >= N, t is feasible
    
    lo, hi = 1, 63  # log2(10^9) ~ 30, but with K=1 we need up to N trials
    # Actually if K=1, answer is N. If K>=log2(N), answer is ceil(log2(N+1))
    # hi should be N but N can be 10^9, so we cap differently
    # With t trials and K eggs, max coverage = sum C(t,i) for i=1..K
    # For K=1: sum = t, so t=N
    # We need hi to handle K=1 case where answer could be N=10^9
    
    # But we can't iterate up to 10^9 easily in binary search if computing C(t,k) is expensive
    # Binary search range: answer is between 1 and N
    # For each candidate t, compute coverage with K eggs in O(K) but K can be up to 10^9
    # However, once K >= t, all C(t,i) for i=1..t sum to 2^t - 1
    # So effective K = min(K, t)
    
    # We binary search t from 1 to 63 won't work for K=1, N=10^9
    # Let's think: if K >= 30, answer <= 30 (since 2^30 > 10^9)
    # If K=1, answer = N
    # So hi = N only when K=1
    
    # Better: binary search with hi = N (but log(N) steps = 30, each step O(min(K,t)) = O(30))
    # Total: O(30 * 30) = fine
    
    def coverage(t, k):
        # Compute sum of C(t,1) + C(t,2) + ... + C(t,min(k,t))
        # Stop early if sum >= N to avoid overflow issues
        effective_k = min(k, t)
        total = 0
        c = 1
        for i in range(1, effective_k + 1):
            c = c * (t - i + 1) // i
            total += c
            if total >= N:
                return total
        return total
    
    lo, hi = 1, N
    while lo < hi:
        mid = (lo + hi) // 2
        if coverage(mid, K) >= N:
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

solve()