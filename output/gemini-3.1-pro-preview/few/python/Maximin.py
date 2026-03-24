import sys
from bisect import bisect_left

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
L = int(input_data[1])
R = int(input_data[2])

A = [int(x) for x in input_data[3:3+N]]
A.sort()

candidates = set()
candidates.add(L)
candidates.add(R)

for i in range(N - 1):
    mid = (A[i] + A[i+1]) // 2
    if L <= mid <= R:
        candidates.add(mid)
    if L <= mid + 1 <= R:
        candidates.add(mid + 1)

max_min_dist = -1

for x in candidates:
    idx = bisect_left(A, x)
    dist = float('inf')
    if idx < N:
        dist = min(dist, A[idx] - x)
    if idx > 0:
        dist = min(dist, x - A[idx-1])
        
    if dist > max_min_dist:
        max_min_dist = dist

print(max_min_dist)