import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
k = data[1]

a = data[2:2 + n]
b = data[2 + n:2 + 2 * n]

pa = []
pb = []

for i, x in enumerate(a, 1):
    if x == 1:
        pa.append(i)

for i, x in enumerate(b, 1):
    if x == 1:
        pb.append(i)

d = [pa[i] - pb[i] for i in range(k)]
d.sort()

median = d[k // 2]
ans = 0
for x in d:
    ans += abs(x - median)

print(ans)