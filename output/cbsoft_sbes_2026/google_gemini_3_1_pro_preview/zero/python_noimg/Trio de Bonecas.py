
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    K = int(input_data[1])
    D = [int(x) for x in input_data[2:N+2]]
    
    D.sort(reverse=True)
    
    INF = 10**18
    dp_prev2 = [INF] * (K + 1)
    dp_prev1 = [INF] * (K + 1)
    dp_curr = [INF] * (K + 1)
    dp_prev2[0] = 0
    dp_prev1[0] = 0
    dp_curr[0] = 0
    
    for i in range(2, N + 1):
        diff = D[i-2] - D[i-1]
        diff_sq = diff * diff
        
        max_j = i // 3
        if max_j > K:
            max_j = K
            
        for j in range(1, max_j + 1):
            opt2 = dp_prev2[j-1] + diff_sq
            if dp_prev1[j] < opt2:
                dp_curr[j] = dp_prev1[j]
            else:
                dp_curr[j] = opt2
                
        dp_prev2, dp_prev1, dp_curr = dp_prev1, dp_curr, dp_prev2

    print(dp_prev1[K])

if __name__ == '__main__':
    solve()
