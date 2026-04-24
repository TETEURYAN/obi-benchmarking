import sys
from bisect import bisect_left

input_data = sys.stdin.read().split()
if not input_data:
    exit()

C = int(input_data[0])
T = int(input_data[1])

R_sq = [0] * C
for i in range(C):
    r = int(input_data[2 + i])
    R_sq[i] = r * r

total_score = 0
idx = 2 + C
for _ in range(T):
    x = int(input_data[idx])
    y = int(input_data[idx+1])
    idx += 2
    
    d_sq = x * x + y * y
    pos = bisect_left(R_sq, d_sq)
    total_score += C - pos

print(total_score)