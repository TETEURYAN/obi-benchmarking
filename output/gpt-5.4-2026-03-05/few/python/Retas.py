import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, x1, x2 = data[0], data[1], data[2]

lines = []
idx = 3
for i in range(n):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    y1 = a * x1 + b
    y2 = a * x2 + b
    lines.append((y1, y2, i))

lines.sort(key=lambda t: (t[0], t[1], t[2]))

arr = [0] * n
for pos, (_, y2, _) in enumerate(lines):
    arr[pos] = (y2, pos)

arr.sort()

bit = [0] * (n + 2)

def add(i, v):
    i += 1
    while i <= n:
        bit[i] += v
        i += i & -i

def sum_prefix(i):
    s = 0
    i += 1
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

ans = 0
processed = 0
j = 0
while j < n:
    k = j
    y = arr[j][0]
    while k < n and arr[k][0] == y:
        k += 1

    for t in range(j, k):
        pos = arr[t][1]
        ans += processed - sum_prefix(pos)

    for t in range(j, k):
        pos = arr[t][1]
        add(pos, 1)
        processed += 1

    j = k

print(ans)