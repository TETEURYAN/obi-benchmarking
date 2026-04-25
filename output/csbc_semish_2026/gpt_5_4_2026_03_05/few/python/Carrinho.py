import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
D = float(data[1])

pos = []
cap = []
idx = 2
for _ in range(n):
    pos.append(float(data[idx]))
    cap.append(float(data[idx + 1]))
    idx += 2

pos.append(D)
cap.append(0.0)

m = n + 1
INF = 1e100
dp = [INF] * m
dp[0] = 0.0

for i in range(n):
    if dp[i] >= INF:
        continue
    pi = pos[i]
    ci = cap[i]
    for j in range(i + 1, m):
        dist = pos[j] - pi
        if dist <= ci + 1e-12:
            val = dp[i] + dist * dist / ci
            if val < dp[j]:
                dp[j] = val
        else:
            break

print(f"{dp[n]:.3f}")