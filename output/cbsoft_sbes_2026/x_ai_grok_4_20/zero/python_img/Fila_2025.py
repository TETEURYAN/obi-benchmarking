
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

count = 0
max_h = -1
for i in range(N-1, -1, -1):
    if A[i] < max_h:
        count += 1
    max_h = max(max_h, A[i])

print(count)
