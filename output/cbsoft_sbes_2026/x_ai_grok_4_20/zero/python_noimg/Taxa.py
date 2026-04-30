
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
F = float(data[1])
X = list(map(int, data[2:2+N]))

S = [0] * (2 * N + 1)
for i in range(1, 2 * N + 1):
    S[i] = S[i-1] + X[(i-1) % N]

total = S[N]
INF = 10**18
dp = [[INF] * (N + 1) for _ in range(N)]

for i in range(N):
    dp[i][1] = 0

for len_ in range(2, N + 1):
    for i in range(N):
        j = (i + len_ - 1) % N
        for k in range(1, len_):
            left = (i + k - 1) % N
            cost_split = max(S[i + k] - S[i], total - (S[i + k] - S[i]))
            prev = dp[i][k] if k > 1 else 0
            nxt = dp[(i + k) % N][len_ - k] if len_ - k > 1 else 0
            total_cost = prev + nxt + cost_split * F
            if total_cost < dp[i][len_]:
                dp[i][len_] = total_cost

ans = INF
for i in range(N):
    ans = min(ans, dp[i][N])

print(f"{ans:.2f}")
