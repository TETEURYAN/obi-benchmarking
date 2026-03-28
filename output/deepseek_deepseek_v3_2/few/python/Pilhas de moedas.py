import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    heights = list(map(int, data[2:2+N]))
    
    freq = {}
    for h in heights:
        freq[h] = freq.get(h, 0) + 1
    
    distinct_counts = sorted(freq.items(), key=lambda x: x[0])
    distinct = len(distinct_counts)
    
    if distinct <= K:
        print(0)
        return
    
    # DP para minimizar moedas adicionadas mantendo ≤ K grupos
    # dp[i][j] = min moedas usando os primeiros i grupos para formar j grupos
    INF = 10**9
    dp = [[INF]*(K+1) for _ in range(distinct+1)]
    dp[0][0] = 0
    
    # precompute prefix sums
    prefix_sum = [0]*(distinct+1)
    prefix_total = [0]*(distinct+1)
    for i in range(1, distinct+1):
        value, count = distinct_counts[i-1]
        prefix_sum[i] = prefix_sum[i-1] + count
        prefix_total[i] = prefix_total[i-1] + value * count
    
    for i in range(1, distinct+1):
        for j in range(1, min(K+1, i+1)):
            best = INF
            # tentamos fazer o último grupo englobar grupos [t..i]
            for t in range(1, i+1):
                total_count = prefix_sum[i] - prefix_sum[t-1]
                total_value = prefix_total[i] - prefix_total[t-1]
                target_height = distinct_counts[i-1][0]
                cost = target_height * total_count - total_value
                if dp[t-1][j-1] != INF:
                    best = min(best, dp[t-1][j-1] + cost)
            dp[i][j] = best
    
    print(dp[distinct][K])

if __name__ == "__main__":
    solve()