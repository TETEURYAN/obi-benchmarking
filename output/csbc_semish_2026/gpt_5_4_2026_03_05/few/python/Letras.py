import sys

s = sys.stdin.read().strip()
if not s:
    sys.exit()

dp = [0] * 26

for ch in s:
    x = ord(ch) - 65
    best = 0
    for i in range(x + 1):
        if dp[i] > best:
            best = dp[i]
    dp[x] = best + 1

print(max(dp))