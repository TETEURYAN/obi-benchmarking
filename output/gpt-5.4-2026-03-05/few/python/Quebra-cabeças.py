import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

idx = 0
N = data[idx]
idx += 1

M1 = data[idx]
idx += 1
A = data[idx:idx + M1]
idx += M1

M2 = data[idx]
idx += 1
B = data[idx:idx + M2]

NEG = -10**18

dp = [[NEG] * (M2 + 1) for _ in range(M1 + 1)]
dp[0][0] = 0

for c in range(1, N + 1):
    ndp = [[NEG] * (M2 + 1) for _ in range(M1 + 1)]
    max_i = min(M1, c)
    max_j = min(M2, c)
    for i in range(max_i + 1):
        row_dp = dp[i]
        row_ndp = ndp[i]
        for j in range(max_j + 1):
            cur = row_dp[j]
            if cur == NEG:
                continue

            if cur > row_ndp[j]:
                row_ndp[j] = cur

            if i < M1:
                v = ndp[i + 1][j]
                if cur > v:
                    ndp[i + 1][j] = cur

            if j < M2:
                v = row_ndp[j + 1]
                if cur > v:
                    row_ndp[j + 1] = cur

            if i < M1 and j < M2:
                val = cur + A[i] * B[j]
                if val > ndp[i + 1][j + 1]:
                    ndp[i + 1][j + 1] = val

    dp = ndp

print(dp[M1][M2])