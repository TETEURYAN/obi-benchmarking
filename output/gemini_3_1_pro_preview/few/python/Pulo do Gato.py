import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

C = int(input_data[0])
tiles = [int(x) for x in input_data[1:C+1]]

dp = [float('inf')] * C
dp[0] = 0

for i in range(C):
    if dp[i] != float('inf'):
        if i + 1 < C and tiles[i + 1] == 1:
            if dp[i] + 1 < dp[i + 1]:
                dp[i + 1] = dp[i] + 1
        if i + 2 < C and tiles[i + 2] == 1:
            if dp[i] + 1 < dp[i + 2]:
                dp[i + 2] = dp[i] + 1

if dp[C - 1] == float('inf'):
    print("-1")
else:
    print(dp[C - 1])