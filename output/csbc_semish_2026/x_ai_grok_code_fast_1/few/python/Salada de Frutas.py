import sys

input_data = sys.stdin.read().split()
R = int(input_data[0])
N = int(input_data[1])
costs = [float('inf')] * 101
idx = 2
for _ in range(N):
    Ti = int(input_data[idx])
    Pi = int(input_data[idx + 1])
    costs[Ti] = min(costs[Ti], Pi)
    idx += 2

valid_costs = [c for c in costs[1:] if c != float('inf')]

dp = [0] * (R + 1)
for c in valid_costs:
    for s in range(R, c - 1, -1):
        dp[s] = max(dp[s], dp[s - c] + 1)

print(max(dp))