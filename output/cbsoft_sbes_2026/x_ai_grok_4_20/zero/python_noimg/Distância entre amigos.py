
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

max_dist = 0
max_left = A[0] - 0
max_right = A[0] + 0

for i in range(1, N):
    curr = A[i]
    pos = i
    
    opt1 = curr + pos + max_left
    opt2 = curr - pos + max_right
    max_dist = max(max_dist, opt1, opt2)
    
    max_left = max(max_left, curr - pos)
    max_right = max(max_right, curr + pos)

print(max_dist)
