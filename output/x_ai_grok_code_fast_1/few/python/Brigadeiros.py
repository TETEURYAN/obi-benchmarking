import sys

data = sys.stdin.read().split()
idx = 0
N = int(data[idx])
idx += 1
K = int(data[idx])
idx += 1
T = int(data[idx])
idx += 1
P = [0] * (N + 1)
for i in range(1, N + 1):
    P[i] = int(data[idx])
    idx += 1
G = []
for i in range(N):
    G.append(int(data[idx]))
    idx += 1
A = [i + 1 for i in range(N) if G[i] == 1]

INF = float('-inf')
max_cost = min(T, 300 * 300) + 1
prev_dp = [[INF] * (max_cost + 1) for _ in range(K + 1)]
prev_dp[0][0] = 0

for i in range(N):
    curr_dp = [[INF] * (max_cost + 1) for _ in range(K + 1)]
    for j in range(K + 1):
        for c in range(max_cost + 1):
            if prev_dp[j][c] == INF:
                continue
            # not assign
            if curr_dp[j][c] < prev_dp[j][c]:
                curr_dp[j][c] = prev_dp[j][c]
            # assign
            if j < K:
                new_c = c + abs(A[j] - (i + 1))
                if new_c <= max_cost:
                    new_sum = prev_dp[j][c] + P[i + 1]
                    if curr_dp[j + 1][new_c] < new_sum:
                        curr_dp[j + 1][new_c] = new_sum
    prev_dp = curr_dp

ans = INF
for c in range(max_cost + 1):
    if c <= T:
        ans = max(ans, prev_dp[K][c])
print(ans)