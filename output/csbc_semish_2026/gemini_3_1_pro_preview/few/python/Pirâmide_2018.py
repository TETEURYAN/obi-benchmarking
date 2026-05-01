import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])

A = []
idx = 1
for _ in range(N):
    row = []
    for _ in range(N):
        row.append(int(input_data[idx]))
        idx += 1
    A.append(row)

pref = []
for i in range(N):
    p = [0] * (N + 1)
    for j in range(N):
        p[j+1] = p[j] + A[i][j]
    pref.append(p)

def get_sum(r, L, R):
    return pref[r][R] - pref[r][L-1]

dp = [float('inf')] * (N + 2)
dp[1] = get_sum(N-1, 1, N)

for i in range(N-1, 0, -1):
    new_dp = [float('inf')] * (N + 2)
    for j in range(1, N - i + 2):
        cost = get_sum(i - 1, j, j + i - 1)
        opt1 = dp[j - 1] if j - 1 >= 1 else float('inf')
        opt2 = dp[j] if j <= N - i else float('inf')
        new_dp[j] = cost + min(opt1, opt2)
    dp = new_dp

ans = min(dp[1:N+1])
print(ans)