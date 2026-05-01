import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
D = float(input_data[idx])
idx += 1
P = []
C = []
for i in range(N):
    p = float(input_data[idx])
    idx += 1
    c = float(input_data[idx])
    idx += 1
    P.append(p)
    C.append(c)

dp = [float('inf')] * N
dp[0] = 0.0
for j in range(1, N):
    for i in range(j):
        dist = P[j] - P[i]
        time = dist * dist / C[i]
        dp[j] = min(dp[j], dp[i] + time)

ans = float('inf')
for j in range(N):
    dist = D - P[j]
    time = dist * dist / C[j]
    ans = min(ans, dp[j] + time)

print(f"{ans:.3f}")