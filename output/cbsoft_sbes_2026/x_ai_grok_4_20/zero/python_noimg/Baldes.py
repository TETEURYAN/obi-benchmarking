
import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
M = int(data[index])
index += 1

buckets = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    p = int(data[index])
    buckets[i].append(p)
    index += 1

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [None] * (4 * n)
        self.build(1, 1, n)
    
    def build(self, node, start, end):
        if start == end:
            vals = buckets[start]
            self.tree[node] = (min(vals), max(vals))
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        left = self.tree[2 * node]
        right = self.tree[2 * node + 1]
        self.tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    
    def update(self, node, start, end, idx, val):
        if start == end:
            buckets[idx].append(val)
            self.tree[node] = (min(buckets[idx]), max(buckets[idx]))
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        left = self.tree[2 * node]
        right = self.tree[2 * node + 1]
        self.tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return (float('inf'), float('-inf'))
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(2 * node, start, mid, l, r)
        right = self.query(2 * node + 1, mid + 1, end, l, r)
        if left[0] == float('inf'):
            return right
        if right[0] == float('inf'):
            return left
        return (min(left[0], right[0]), max(left[1], right[1]))

st = SegmentTree(N)

results = []
for _ in range(M):
    tp = int(data[index])
    index += 1
    if tp == 1:
        p = int(data[index])
        index += 1
        i = int(data[index])
        index += 1
        st.update(1, 1, N, i, p)
    else:
        a = int(data[index])
        index += 1
        b = int(data[index])
        index += 1
        mn, mx = st.query(1, 1, N, a, b)
        results.append(str(mx - mn))

print('\n'.join(results))
