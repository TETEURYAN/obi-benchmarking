
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N == 0:
    print(0)
    sys.exit()

count = 0
max_h = A[-1]

for i in range(N-2, -1, -1):
    if A[i] <= max_h:
        count += 1
    else:
        max_h = A[i]

print(count)
