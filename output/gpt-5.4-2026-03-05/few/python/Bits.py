import sys

MOD = 10**9 + 7

data = sys.stdin.read().split()
if not data:
    sys.exit()

N = int(data[0])
K = int(data[1])

if K == 1:
    print(1)
    sys.exit()

if K == N + 1:
    print(pow(2, N, MOD))
    sys.exit()

dp = [0] * K
dp[0] = 1
total = 1

for _ in range(N):
    new0 = total
    new = [0] * K
    new[0] = new0 % MOD
    new_total = new[0]
    for j in range(1, K):
        new[j] = dp[j - 1]
        new_total += new[j]
    total = new_total % MOD
    dp = new

print(total)