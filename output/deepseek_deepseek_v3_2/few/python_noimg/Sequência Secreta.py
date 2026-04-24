import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    seq = list(map(int, data[1:1+n]))

    # dp[i][last] = máximo marcados até posição i, com último marcado = last (1 ou 2)
    # last = 0 significa que nenhum foi marcado ainda
    dp = [[-10**9] * 3 for _ in range(n)]
    dp[0][0] = 0
    dp[0][seq[0]] = 1

    for i in range(1, n):
        for last in (0, 1, 2):
            # não marcar i
            dp[i][last] = max(dp[i][last], dp[i-1][last])
            # marcar i, se possível
            if last != seq[i]:
                dp[i][seq[i]] = max(dp[i][seq[i]], dp[i-1][last] + 1)

    ans = max(dp[n-1][1], dp[n-1][2])
    print(ans)

if __name__ == "__main__":
    solve()