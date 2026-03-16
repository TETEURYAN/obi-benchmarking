import sys

def main():
    input = sys.stdin.readline
    N, K, T = map(int, input().split())
    P = list(map(int, input().split()))
    G = list(map(int, input().split()))

    friends = [i + 1 for i, x in enumerate(G) if x == 1]

    INF = 10**18
    dp = [[-INF] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 0

    for i in range(1, K + 1):
        s = friends[i - 1]
        for j in range(i, N - (K - i) + 1):
            cost = abs(s - j)
            best = -INF
            prev_row = dp[i - 1]
            for p in range(i - 1, j):
                val = prev_row[p]
                if val > best:
                    best = val
            if best > -INF:
                dp[i][j] = best + P[j - 1] - cost

    ans = 0
    last = dp[K]
    for j in range(K, N + 1):
        val = last[j]
        if val >= -INF // 2 and val + T > ans:
            ans = val + T

    total_p = sum(P)
    if ans > total_p:
        ans = total_p

    print(ans)

if __name__ == "__main__":
    main()
