import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
A = list(map(int, data[1:1+n]))

max_diff = A[0] - 0
ans = 0
for j in range(1, n):
    candidate = (A[j] + j) + max_diff
    if candidate > ans:
        ans = candidate
    if A[j] - j > max_diff:
        max_diff = A[j] - j

print(ans)