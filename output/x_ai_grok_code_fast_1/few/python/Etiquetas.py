import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
K = int(input_data[1])
C = int(input_data[2])
A = list(map(int, input_data[3:]))
total_sum = sum(A)
M = N - C + 1
sum_window = []
for i in range(M):
    s = sum(A[i:i+C])
    sum_window.append(s)
INF = 10**18
dp = [[INF] * (K + 1) for _ in range(M + 1)]
dp[0][0] = 0
for j in range(1, M + 1):
    for k in range(K + 1):
        dp[j][k] = dp[j - 1][k]
        if k >= 1:
            prev_j = j - C
            if prev_j >= 0:
                dp[j][k] = min(dp[j][k], dp[prev_j][k - 1] + sum_window[j - 1])
            else:
                dp[j][k] = min(dp[j][k], sum_window[j - 1])
print(total_sum - dp[M][K])