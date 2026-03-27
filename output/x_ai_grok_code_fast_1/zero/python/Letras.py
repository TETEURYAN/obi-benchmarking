
import sys

input = sys.stdin.read
data = input().strip()
S = data
dp = [0] * 27
max_len = 0
for c in S:
    num = ord(c) - ord('A') + 1
    current_max = 0
    for j in range(1, num + 1):
        current_max = max(current_max, dp[j])
    dp[num] = current_max + 1
    max_len = max(max_len, dp[num])
print(max_len)
