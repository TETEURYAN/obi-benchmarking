import sys

data = sys.stdin.read().split()
N = int(data[0])
X = int(data[1])
Y = int(data[2])
Z = int(data[3])

costs = sorted([X, Y, Z])
count = 0
remaining = N
for c in costs:
    if remaining >= c:
        remaining -= c
        count += 1
print(count)