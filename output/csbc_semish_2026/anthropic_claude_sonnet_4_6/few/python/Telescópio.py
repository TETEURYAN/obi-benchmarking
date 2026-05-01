import sys

data = sys.stdin.read().split()
A = int(data[0])
N = int(data[1])

count = 0
for i in range(N):
    F = int(data[2 + i])
    if F * A >= 40000000:
        count += 1

print(count)