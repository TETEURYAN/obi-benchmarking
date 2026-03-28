import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
D = float(input_data[1])

P = [0.0] * N
C = [0.0] * N

idx = 2
for i in range(N):
    P[i] = float(input_data[idx])
    C[i] = float(input_data[idx+1])
    idx += 2

P.append(D)

dp = [float('inf')] * (N + 1)
dp[0] = 0.0

for i in range(N):
    current_dp = dp[i]
    current_p = P[i]
    current_c = C[i]
    
    for j in range(i + 1, N + 1):
        dist = P[j] - current_p
        time = (dist * dist) / current_c
        if current_dp + time < dp[j]:
            dp[j] = current_dp + time

print(f"{dp[N]:.3f}")