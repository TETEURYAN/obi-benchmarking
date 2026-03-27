import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
F = float(input_data[idx])
idx += 1
X = [int(input_data[idx + i]) for i in range(N)]

# Duplicate the array
S = X + X
NN = 2 * N

# Prefix sums
prefix = [0] * (NN + 1)
for i in range(1, NN + 1):
    prefix[i] = prefix[i - 1] + S[i - 1]

def get_sum(i, j):
    # sum from i to j inclusive, 1-based
    return prefix[j] - prefix[i - 1]

# DP table
dp = [[float('inf')] * (NN + 1) for _ in range(NN + 1)]
for i in range(1, NN + 1):
    dp[i][i] = 0.0

for length in range(2, NN + 1):
    for i in range(1, NN - length + 2):
        j = i + length - 1
        for k in range(i, j):
            left_sum = get_sum(i, k)
            right_sum = get_sum(k + 1, j)
            cost = dp[i][k] + dp[k + 1][j] + F * max(left_sum, right_sum)
            if cost < dp[i][j]:
                dp[i][j] = cost

# Find min over i=1 to N of dp[i][i+N-1]
min_cost = float('inf')
for i in range(1, N + 1):
    min_cost = min(min_cost, dp[i][i + N - 1])

print(f"{min_cost:.2f}")