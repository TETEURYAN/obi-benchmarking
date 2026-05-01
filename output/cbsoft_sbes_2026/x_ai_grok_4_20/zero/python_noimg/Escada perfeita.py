
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

total = sum(A)
if total % N != 0:
    print(-1)
    sys.exit(0)

avg = total // N
target = [avg - (N - 1 - i) for i in range(N)]

if target[0] < 0:
    print(-1)
    sys.exit(0)

moves = 0
for i in range(N):
    if A[i] > target[i]:
        moves += A[i] - target[i]

print(moves)
