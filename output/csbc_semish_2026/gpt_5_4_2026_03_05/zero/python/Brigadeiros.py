import sys

def main():
    input = sys.stdin.readline
    N, K, T = map(int, input().split())
    P = [0] + list(map(int, input().split()))
    G = list(map(int, input().split()))
    
    friends = [i + 1 for i, x in enumerate(G) if x == 1]
    
    INF = -10**18
    dp = [[INF] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 0
    
    for i in range(1, K + 1):
        s = friends[i - 1]
        for j in range(i, N - (K - i) + 1):
            prev = dp[i - 1]
            best_prev = INF
            for p in range(i - 1, j):
                val = prev[p]
                if val == INF:
                    continue
                cost = abs(s - j)
                total_cost = 0
                total_cost = cost
                cand = val - total_cost
                if cand > best_prev:
                    best_prev = cand
            if best_prev != INF:
                dp[i][j] = best_prev + P[j]
    
    ans = 0
    for j in range(K, N + 1):
        val = dp[K][j]
        if val != INF and val + T >= 0:
            if val > ans:
                ans = val
    
    best = 0
    for j in range(K, N + 1):
        val = dp[K][j]
        if val != INF:
            cost_adjusted = val
            if cost_adjusted + T >= 0:
                if cost_adjusted > best:
                    best = cost_adjusted
    
    res = 0
    for j in range(K, N + 1):
        if dp[K][j] != INF and dp[K][j] + T >= 0:
            res = max(res, dp[K][j])
    
    print(res)

if __name__ == "__main__":
    main()
