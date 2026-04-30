
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

max_sum = float('-inf')
current = 0
for i in range(N):
    current += A[i]
    if current > max_sum:
        max_sum = current
    if current < 0:
        current = 0

print(max_sum)
