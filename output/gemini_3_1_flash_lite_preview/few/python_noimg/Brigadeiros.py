import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    T = int(input_data[2])
    
    P = [int(x) for x in input_data[3:3+N]]
    G = [int(x) for x in input_data[3+N:3+2*N]]
    
    pos_amigos = [i for i, val in enumerate(G) if val == 1]
    
    # dp[i][j] = min cost to place first i friends in first j positions
    # i: 0 to K, j: 0 to N
    # Cost is sum of |pos_amigos[i] - final_pos[i]|
    # Since order is preserved, we just need to pick K positions out of N
    
    inf = float('inf')
    dp = [[inf] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 0
    
    for i in range(K):
        for j in range(N):
            if dp[i][j] == inf:
                continue
            # Try placing the (i+1)-th friend at position k (j <= k < N)
            for k in range(j, N):
                cost = abs(pos_amigos[i] - k)
                if dp[i][j] + cost <= T:
                    if dp[i+1][k+1] > dp[i][j] + cost:
                        dp[i+1][k+1] = dp[i][j] + cost
    
    # Now we need to find the max sum of brigadeiros for a set of K positions
    # that satisfy the cost constraint.
    # Actually, the DP above is slightly wrong because it doesn't track the sum.
    # Let's redefine: dp[i][j] = min cost to place first i friends in a subset of first j positions.
    # We need to maximize sum of P[pos] for chosen positions.
    
    # Correct DP: dp[i][j] = max brigadeiros using i friends in first j positions with cost <= T
    # Since T is large, we need to track cost.
    # dp[i][j][cost] is too big.
    # But N is small (300).
    # dp[i][j] = min cost to place first i friends in first j positions.
    # This doesn't help with max brigadeiros.
    
    # Let's use: dp[i][j] = max brigadeiros using i friends in first j positions with total cost c.
    # Since we want to maximize sum, and cost is a constraint:
    # dp[i][j] = list of (cost, sum) pairs? No, too slow.
    # Actually, for a fixed set of K positions, the cost is sum(|pos_amigos[i] - final_pos[i]|).
    # We can use DP: dp[i][j][c] = max brigadeiros using i friends in first j positions with cost c.
    
    dp = [[[-1] * (T + 1) for _ in range(N + 1)] for _ in range(K + 1)]
    for j in range(N + 1):
        dp[0][j][0] = 0
        
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            # Option 1: Don't put friend i at position j-1
            for c in range(T + 1):
                dp[i][j][c] = dp[i][j-1][c]
            
            # Option 2: Put friend i at position j-1
            cost = abs(pos_amigos[i-1] - (j-1))
            for c in range(cost, T + 1):
                if dp[i-1][j-1][c - cost] != -1:
                    dp[i][j][c] = max(dp[i][j][c], dp[i-1][j-1][c - cost] + P[j-1])
                    
    print(max(dp[K][N]))

solve()