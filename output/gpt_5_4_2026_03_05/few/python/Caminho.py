import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
p = data[1:1+n]

dark = [0] * n
for i in range(n - 1):
    if p[i] + p[i + 1] < 1000:
        dark[i] = 1
if p[-1] + p[0] < 1000:
    dark[-1] = 1

total_dark = sum(dark)
if total_dark == 0:
    print(0)
elif total_dark == n:
    print(n)
else:
    cur = 0
    best = 0
    for i in range(2 * n):
        if dark[i % n]:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    if best > n:
        best = n
    print(best)