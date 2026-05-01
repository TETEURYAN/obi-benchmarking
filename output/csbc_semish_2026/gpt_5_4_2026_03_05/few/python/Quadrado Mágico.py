import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = []
idx = 1
zr = zc = -1

for i in range(n):
    row = data[idx:idx + n]
    idx += n
    for j, v in enumerate(row):
        if v == 0:
            zr, zc = i, j
    a.append(row)

target = None

for i in range(n):
    if i != zr:
        target = sum(a[i])
        break

if target is None:
    for j in range(n):
        if j != zc:
            s = 0
            for i in range(n):
                s += a[i][j]
            target = s
            break

row_sum = sum(a[zr])
missing = target - row_sum

print(missing)
print(zr + 1)
print(zc + 1)