import sys

MOD = 10**9 + 7

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

if n == 0:
    print(1)
elif n == 1:
    print(1)
elif n == 2:
    print(5)
else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 5
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 4 * dp[i - 2] + 2 * dp[i - 3]) % MOD
    print(dp[n])