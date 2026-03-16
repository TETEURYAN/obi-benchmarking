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
            prev = dp[i - 1]
            for pj in range(i - 1, j):
                val = prev[pj]
                if val != -INF:
                    cand = val - cost + P[j - 1]
                    if cand > best:
                        best = cand
            dp[i][j] = best

    ans = 0
    last = dp[K]
    for j in range(K, N + 1):
        val = last[j]
        if val != -INF and val + T > ans:
            ans = val + T

    total = sum(P)
    if ans > total:
        ans = total

    print(ans)

if __name__ == "__main__":
    main()
