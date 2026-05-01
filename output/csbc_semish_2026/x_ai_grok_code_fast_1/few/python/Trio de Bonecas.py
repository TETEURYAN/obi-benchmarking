import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
K = int(data[1])
T = list(map(int, data[2:]))
T.sort()
N_K = N - K
pairs = []
for i in range(N_K - 1):
    cost = (T[i] - T[i + 1]) ** 2
    pairs.append(cost)
num_pairs = len(pairs)
DP = [[float('inf')] * (num_pairs + 1) for _ in range(K + 1)]
DP[0][0] = 0
for k in range(1, K + 1):
    for i in range(1, num_pairs + 1):
        for j in range(i):
            if j == 0 or abs((i - 1) - (j - 1)) >= 2:
                DP[k][i] = min(DP[k][i], DP[k - 1][j] + pairs[i - 1])
print(min(DP[K]))