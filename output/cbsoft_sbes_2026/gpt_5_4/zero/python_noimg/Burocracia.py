import sys

sys.setrecursionlimit(1_000_000)

input = sys.stdin.readline

N = int(input())
par = [0] * (N + 1)
tmp = list(map(int, input().split()))
children = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    par[i] = tmp[i - 2]
    children[par[i]].append(i)

tin = [0] * (N + 1)
tout = [0] * (N + 1)
depth0 = [0] * (N + 1)
order = []

timer = 0
stack = [(1, 0)]
while stack:
    v, state = stack.pop()
    if state == 0:
        tin[v] = timer
        order.append(v)
        timer += 1
        stack.append((v, 1))
        for u in reversed(children[v]):
            depth0[u] = depth0[v] + 1
            stack.append((u, 0))
    else:
        tout[v] = timer - 1

LOG = (N).bit_length()
up = [[0] * (N + 1) for _ in range(LOG)]
for v in range(1, N + 1):
    up[0][v] = par[v]
for j in range(1, LOG):
    uj = up[j]
    prev = up[j - 1]
    for v in range(1, N + 1):
        uj[v] = prev[prev[v]]

def kth_ancestor(v, k):
    b = 0
    while k:
        if k & 1:
            v = up[b][v]
        k >>= 1
        b += 1
    return v

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, i, delta):
        i += 1
        n = self.n + 1
        bit = self.bit
        while i <= n:
            bit[i] += delta
            i += i & -i

    def range_add(self, l, r, delta):
        self.add(l, delta)
        if r + 1 < self.n:
            self.add(r + 1, -delta)

    def sum(self, i):
        i += 1
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

bit = BIT(N)

Q = int(input())
out = []

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 2:
        v = op[1]
        l = tin[v] + 1
        r = tout[v]
        if l <= r:
            bit.range_add(l, r, depth0[v] + 1)
    else:
        v, k = op[1], op[2]
        cur_depth = bit.sum(tin[v])
        target_depth = cur_depth - k
        ans = kth_ancestor(v, depth0[v] - target_depth)
        out.append(str(ans))

sys.stdout.write("\n".join(out))