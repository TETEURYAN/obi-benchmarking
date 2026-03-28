import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    S = [int(x) for x in input_data[2:]]
    S.sort(reverse=True)
    
    INF = 10**18
    dp0 = [0] + [INF] * K
    dp1 = [0] + [INF] * K
    dp2 = [0] + [INF] * K
    
    for i in range(2, N + 1):
        diff = S[i-2] - S[i-1]
        diff_sq = diff * diff
        
        max_k = i // 3
        if max_k > K:
            max_k = K
            
        for k in range(1, max_k + 1):
            val = dp0[k-1] + diff_sq
            dp1_k = dp1[k]
            if dp1_k < val:
                dp2[k] = dp1_k
            else:
                dp2[k] = val
                
        dp0, dp1, dp2 = dp1, dp2, dp0
        
    print(dp1[K])

if __name__ == '__main__':
    solve()