
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    K = int(data[1])
    T = int(data[2])
    
    P_array = [int(x) for x in data[3:3+N]]
    G_array = [int(x) for x in data[3+N:3+2*N]]
    
    x_positions = [i + 1 for i, g in enumerate(G_array) if g == 1]
    
    INF = float('inf')
    dp = [[INF] * 1 for _ in range(N + 1)]
    for j in range(N + 1):
        dp[j][0] = 0
        
    for i in range(1, K + 1):
        max_v = 9 * i
        next_dp = [[INF] * (max_v + 1) for _ in range(N + 1)]
        x = x_positions[i - 1]
        
        valid_dp = [[(v, val) for v, val in enumerate(dp_j) if val != INF] for dp_j in dp]
            
        for j in range(i, N - K + i + 1):
            cost = abs(x - j)
            P = P_array[j - 1]
            
            curr_j = list(next_dp[j - 1])
            
            for v_prev, prev_val in valid_dp[j - 1]:
                val2 = prev_val + cost
                nxt_v = v_prev + P
                if val2 < curr_j[nxt_v]:
                    curr_j[nxt_v] = val2
                    
            next_dp[j] = curr_j
            
        dp = next_dp
        
    ans = 0
    for v, min_swaps in enumerate(dp[N]):
        if min_swaps <= T:
            ans = v
            
    print(ans)

if __name__ == '__main__':
    solve()
