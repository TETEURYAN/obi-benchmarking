import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
arr = data[1:1 + n]

last = {}
left = 0
best = 0

for right, x in enumerate(arr):
    if x in last and last[x] >= left:
        left = last[x] + 1
    last[x] = right
    length = right - left + 1
    if length > best:
        best = length

print(best)