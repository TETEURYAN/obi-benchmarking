import sys

data = sys.stdin.read().split()
N = int(data[0])
total = 0
for i in range(N):
    ci = int(data[1 + 2 * i])
    si = int(data[2 + 2 * i])
    diff1 = (ci - si) % 10
    diff2 = (si - ci) % 10
    total += min(diff1, diff2)
print(total)