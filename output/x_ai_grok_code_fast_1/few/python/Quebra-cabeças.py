import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M1 = int(input_data[idx])
idx += 1
A = []
for _ in range(M1):
    A.append(int(input_data[idx]))
    idx += 1
M2 = int(input_data[idx])
idx += 1
B = []
for _ in range(M2):
    B.append(int(input_data[idx]))
    idx += 1

dp = [[0] * (M2 + 1) for _ in range(M1 + 1)]
for i in range(1, M1 + 1):
    for j in range(1, M2 + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + A[i-1] * B[j-1])

print(dp[M1][M2])