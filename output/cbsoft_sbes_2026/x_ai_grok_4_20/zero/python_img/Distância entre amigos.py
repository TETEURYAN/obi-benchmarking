
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

max_dist = 0
max_left = A[0]
max_right = A[-1]

for i in range(N):
    curr = A[i]
    dist1 = curr + i + max_left
    dist2 = curr + (N - 1 - i) + max_right
    max_dist = max(max_dist, dist1, dist2)
    
    max_left = max(max_left, curr - i)
    max_right = max(max_right, curr - (N - 1 - i))

print(max_dist)
