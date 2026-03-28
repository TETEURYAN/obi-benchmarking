import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

events = []
for i in range(N-1):
    if A[i] != A[i+1]:
        mn = min(A[i], A[i+1])
        mx = max(A[i], A[i+1])
        events.append((mn, 1))
        events.append((mx, -1))

events.sort()

current = 0
max_overlap = 0
for val, delta in events:
    current += delta
    max_overlap = max(max_overlap, current)

print(1 + max_overlap)