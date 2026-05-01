import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

N = int(data[0])
K = int(data[1])

if K >= N:
    x = 0
    p = 1
    while p < N + 1:
        p <<= 1
        x += 1
    print(x)
    sys.exit()

dp = [0] * (K + 1)
m = 0
while dp[K] < N:
    m += 1
    for k in range(K, 0, -1):
        dp[k] = dp[k] + dp[k - 1] + 1

print(m)