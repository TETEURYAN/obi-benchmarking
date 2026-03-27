import sys

data = sys.stdin.read().split()
N = int(data[0])
matrix = []
idx = 1
for i in range(N):
    row = [int(x) for x in data[idx:idx + N]]
    matrix.append(row)
    idx += N

INF = 10**18
dp = [[INF] * (N + 2) for _ in range(N + 1)]
for j in range(1, N + 1):
    dp[1][j] = matrix[0][j - 1]

for i in range(2, N + 1):
    for curr in range(1, N - i + 2):
        left = curr
        right = min(N, curr + i - 1)
        min_prev = min(dp[i - 1][p] for p in range(left, right + 1))
        sum_row = sum(matrix[i - 1][curr - 1: curr - 1 + i])
        dp[i][curr] = min_prev + sum_row

ans = min(dp[N][curr] for curr in range(1, N + 1))
print(ans)