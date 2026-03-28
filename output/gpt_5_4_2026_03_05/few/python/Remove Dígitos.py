import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

dp = [0] + [10**9] * n

for i in range(1, n + 1):
    x = i
    best = 10**9
    while x > 0:
        d = x % 10
        if d != 0:
            v = dp[i - d] + 1
            if v < best:
                best = v
        x //= 10
    dp[i] = best

print(dp[n])