
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = float(input_data[1])
    
    A = [int(x) for x in input_data[2:N+2]]
    
    if N == 1:
        print(f"{0.00:.2f}")
        return
        
    A2 = A + A
    M = 2 * N - 1
    
    pref = [0] * (M + 1)
    for i in range(M):
        pref[i+1] = pref[i] + A2[i]
        
    dp = [[0] * M for _ in range(M)]
    
    for length in range(2, N + 1):
        for i in range(M - length + 1):
            j = i + length - 1
            
            min_cost = float('inf')
            pi = pref[i]
            pj1 = pref[j+1]
            dpi = dp[i]
            
            for k in range(i, j):
                pk1 = pref[k+1]
                left_sum = pk1 - pi
                right_sum = pj1 - pk1
                
                cost = dpi[k] + dp[k+1][j] + (left_sum if left_sum > right_sum else right_sum)
                if cost < min_cost:
                    min_cost = cost
                    
            dp[i][j] = min_cost
            
    ans = float('inf')
    for i in range(N):
        if dp[i][i+N-1] < ans:
            ans = dp[i][i+N-1]
            
    print(f"{ans * F:.2f}")

if __name__ == '__main__':
    solve()
