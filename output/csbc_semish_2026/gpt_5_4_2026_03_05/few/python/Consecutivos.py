import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
vals = list(map(int, data[1:1 + n]))

best = 1
cur = 1

for i in range(1, n):
    if vals[i] == vals[i - 1]:
        cur += 1
    else:
        if cur > best:
            best = cur
        cur = 1

if cur > best:
    best = cur

print(best)