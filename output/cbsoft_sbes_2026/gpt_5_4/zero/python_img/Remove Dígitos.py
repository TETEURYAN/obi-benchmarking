import sys

n = int(sys.stdin.readline())

dp = [0] + [10**9] * n

for i in range(1, n + 1):
    x = i
    while x > 0:
        d = x % 10
        if d != 0:
            dp[i] = min(dp[i], dp[i - d] + 1)
        x //= 10

print(dp[n])