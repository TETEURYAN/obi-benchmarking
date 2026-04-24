
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    a = [int(x) for x in data[2:2+n]]
    
    INF = float('inf')
    
    # dp0 = min sum ending with a[i-1]
    # dp1 = min sum ending with m - a[i-1]
    dp0, dp1 = a[0], m - a[0]
    
    for i in range(1, n):
        v0, v1 = a[i], m - a[i]
        pv0, pv1 = a[i-1], m - a[i-1]
        
        # Compute new_dp0 (using v0)
        new_dp0 = INF
        if dp0 < INF and pv0 <= v0:
            new_dp0 = min(new_dp0, v0 + dp0)
        if dp1 < INF and pv1 <= v0:
            new_dp0 = min(new_dp0, v0 + dp1)
        
        # Compute new_dp1 (using v1)
        new_dp1 = INF
        if dp0 < INF and pv0 <= v1:
            new_dp1 = min(new_dp1, v1 + dp0)
        if dp1 < INF and pv1 <= v1:
            new_dp1 = min(new_dp1, v1 + dp1)
        
        dp0, dp1 = new_dp0, new_dp1
    
    result = min(dp0, dp1)
    print(-1 if result == INF else result)

solve()
