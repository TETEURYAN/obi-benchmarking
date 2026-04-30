
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N == 0:
    print(0)
    sys.exit(0)

total = sum(A)
if total > 0:
    print(total)
    sys.exit(0)

max_sum = max(A)
if max_sum <= 0:
    print(0)
    sys.exit(0)

B = A + A
prefix = [0] * (2 * N + 1)
for i in range(2 * N):
    prefix[i + 1] = prefix[i] + B[i]

min_prefix = [0] * (2 * N + 1)
min_prefix[0] = 0
for i in range(1, 2 * N + 1):
    min_prefix[i] = min(min_prefix[i - 1], prefix[i])

ans = max_sum
for i in range(1, 2 * N + 1):
    curr = prefix[i] - min_prefix[i - 1]
    if curr > ans:
        ans = curr

print(ans)
