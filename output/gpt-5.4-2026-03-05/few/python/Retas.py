import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

def count_inversions(arr):
    vals = sorted(set(arr))
    comp = {v: i + 1 for i, v in enumerate(vals)}
    fw = Fenwick(len(vals))
    inv = 0
    seen = 0
    for x in arr:
        cx = comp[x]
        inv += seen - fw.sum(cx)
        fw.add(cx, 1)
        seen += 1
    return inv

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
x1 = int(next(it))
x2 = int(next(it))

lines = []
for _ in range(n):
    a = int(next(it))
    b = int(next(it))
    y1 = a * x1 + b
    y2 = a * x2 + b
    lines.append((y1, y2))

lines.sort(key=lambda p: (p[0], p[1]))
arr = [p[1] for p in lines]

print(count_inversions(arr))