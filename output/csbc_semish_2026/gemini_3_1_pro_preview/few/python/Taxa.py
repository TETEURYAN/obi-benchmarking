import sys
import bisect

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F_str = input_data[1]
    
    if '.' in F_str:
        integer_part, decimal_part = F_str.split('.')
        decimal_part = (decimal_part + "00")[:2]
        F_int = int(integer_part) * 100 + int(decimal_part)
    else:
        F_int = int(F_str) * 100
        
    if N == 1:
        print("0.00")
        return
        
    X = [int(x) for x in input_data[2:N+2]]
    
    A = X + X
    M = 2 * N
    
    pref = [0] * (M + 1)
    for i in range(M):
        pref[i+1] = pref[i] + A[i]
        
    dp = [[0] * M for _ in range(M)]
    
    INF = 10**18
    
    for length in range(2, N + 1):
        for i in range(M - length + 1):
            j = i + length - 1
            
            pi = pref[i]
            pj = pref[j+1]
            pi_pj = pi + pj
            
            idx = bisect.bisect_right(pref, pi_pj // 2, i + 1, j + 1)
            
            min_val1 = INF
            dpi = dp[i]
            
            for k in range(i, idx - 1):
                tot = dpi[k] + dp[k+1][j] - pref[k+1]
                if tot < min_val1: 
                    min_val1 = tot
                
            if min_val1 != INF:
                min_val1 += pj
                
            min_val2 = INF
            for k in range(max(i, idx - 1), j):
                tot = dpi[k] + dp[k+1][j] + pref[k+1]
                if tot < min_val2: 
                    min_val2 = tot
                
            if min_val2 != INF:
                min_val2 -= pi
                
            dp[i][j] = min_val1 if min_val1 < min_val2 else min_val2

    ans = INF
    for i in range(N):
        if dp[i][i+N-1] < ans:
            ans = dp[i][i+N-1]
            
    total_tax = ans * F_int
    print(f"{total_tax // 100}.{total_tax % 100:02d}")

if __name__ == '__main__':
    solve()