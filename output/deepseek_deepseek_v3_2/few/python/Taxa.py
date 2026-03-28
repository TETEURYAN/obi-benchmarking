import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    F = float(next(it))
    areas = [int(next(it)) for _ in range(N)]

    # Duplicar o array para lidar com circularidade
    arr = areas + areas
    prefix = [0] * (2 * N + 1)
    for i in range(2 * N):
        prefix[i + 1] = prefix[i] + arr[i]

    INF = float('inf')
    dp = [[INF] * (2 * N) for _ in range(2 * N)]

    # Inicializar intervalos de tamanho 1
    for i in range(2 * N):
        dp[i][i] = 0.0

    # DP para intervalos crescentes
    for length in range(2, N + 1):
        for l in range(2 * N - length + 1):
            r = l + length - 1
            total = prefix[r + 1] - prefix[l]
            # Tentar todas as divisões possíveis
            for k in range(l, r):
                left_sum = prefix[k + 1] - prefix[l]
                right_sum = total - left_sum
                tax = max(left_sum, right_sum) * F
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + tax)

    # Encontrar o mínimo considerando todas as posições iniciais de tamanho N
    ans = INF
    for i in range(N):
        ans = min(ans, dp[i][i + N - 1])
    print(f"{ans:.2f}")

if __name__ == "__main__":
    solve()