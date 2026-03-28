import sys

MOD = 10**9 + 7
input_data = sys.stdin.read().split()
N = int(input_data[0])
K = int(input_data[1])

prev = [0] * K
prev[0] = 1
if K > 1:
    prev[1] = 1

for i in range(2, N + 1):
    curr = [0] * K
    s = sum(prev) % MOD
    curr[0] = s
    for j in range(1, K):
        curr[j] = prev[j - 1]
    prev = curr

total = sum(prev) % MOD
print(total)