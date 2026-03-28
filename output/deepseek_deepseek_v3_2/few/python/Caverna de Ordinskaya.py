import sys
sys.setrecursionlimit(200000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    A = [int(next(it)) for _ in range(N)]

    # dp[i][0] = menor soma possível até o mergulho i se escolhemos a_i
    # dp[i][1] = menor soma possível até o mergulho i se escolhemos M - a_i
    INF = 10**18
    dp = [[INF, INF] for _ in range(N)]
    dp[0][0] = A[0]
    dp[0][1] = M - A[0]

    for i in range(1, N):
        a = A[i]
        b = M - a
        # de dp[i-1][0] (escolheu a_{i-1})
        prev_a = A[i-1]
        # transição para a_i
        if a >= prev_a:
            dp[i][0] = min(dp[i][0], dp[i-1][0] + a)
        # transição para M - a_i
        if b >= prev_a:
            dp[i][1] = min(dp[i][1], dp[i-1][0] + b)

        # de dp[i-1][1] (escolheu M - a_{i-1})
        prev_b = M - A[i-1]
        # transição para a_i
        if a >= prev_b:
            dp[i][0] = min(dp[i][0], dp[i-1][1] + a)
        # transição para M - a_i
        if b >= prev_b:
            dp[i][1] = min(dp[i][1], dp[i-1][1] + b)

    ans = min(dp[N-1][0], dp[N-1][1])
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    solve()