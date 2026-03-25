import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = min([dp[i - int(d)] for d in str(i) if d != '0']) + 1

print(dp[n])