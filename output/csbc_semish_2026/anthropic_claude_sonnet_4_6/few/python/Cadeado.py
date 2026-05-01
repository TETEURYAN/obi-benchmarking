import sys

data = sys.stdin.read().split()
n = int(data[0])
total = 0
for i in range(n):
    c = int(data[1 + 2*i])
    s = int(data[2 + 2*i])
    diff = abs(c - s)
    total += min(diff, 10 - diff)
print(total)