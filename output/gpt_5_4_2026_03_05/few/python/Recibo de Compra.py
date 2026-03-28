import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

R = int(data[0])
K = int(data[1])

min_sum = K * (K + 1) // 2
if min_sum > R:
    print(0)
    sys.exit()

dp = [[0] * (R + 1) for _ in range(K + 1)]
dp[0][0] = 1

for x in range(1, R + 1):
    upper_k = min(K, x)
    for k in range(upper_k, 0, -1):
        row = dp[k]
        prev = dp[k - 1]
        for s in range(R, x - 1, -1):
            row[s] += prev[s - x]

print(dp[K][R])