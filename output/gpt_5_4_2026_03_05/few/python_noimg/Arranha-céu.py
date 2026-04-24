import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
q = int(data[1])

bit = [0] * (n + 1)
arr = [0] * (n + 1)

def add(i, delta):
    while i <= n:
        bit[i] += delta
        i += i & -i

def sum_prefix(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

idx = 2
for i in range(1, n + 1):
    v = int(data[idx])
    idx += 1
    arr[i] = v
    add(i, v)

out = []
for _ in range(q):
    t = int(data[idx])
    idx += 1
    if t == 0:
        k = int(data[idx])
        p = int(data[idx + 1])
        idx += 2
        delta = p - arr[k]
        arr[k] = p
        add(k, delta)
    else:
        k = int(data[idx])
        idx += 1
        out.append(str(sum_prefix(k)))

sys.stdout.write("\n".join(out))