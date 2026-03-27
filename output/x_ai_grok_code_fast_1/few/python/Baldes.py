import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
min_p = [0] * (N + 1)
max_p = [0] * (N + 1)
for i in range(1, N + 1):
    p = int(input_data[idx])
    idx += 1
    min_p[i] = p
    max_p[i] = p
INF = 10**9 + 10

class SegTree:
    def __init__(self, n, is_min=True):
        self.n = n
        self.tree = [None] * (4 * n)
        self.is_min = is_min
        self.build(1, 1, n)

    def build(self, node, start, end):
        if start == end:
            if self.is_min:
                self.tree[node] = (min_p[start], INF, start)
            else:
                self.tree[node] = max_p[start]
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        self.merge(node)

    def merge(self, node):
        left = self.tree[2 * node]
        right = self.tree[2 * node + 1]
        if self.is_min:
            if left[0] < right[0]:
                min_val = left[0]
                second = min(left[1], right[0])
                idx = left[2]
            elif right[0] < left[0]:
                min_val = right[0]
                second = min(right[1], left[0])
                idx = right[2]
            else:
                min_val = left[0]
                second = min(left[1], right[1])
                idx = left[2]
            self.tree[node] = (min_val, second, idx)
        else:
            self.tree[node] = max(left, right)

    def update(self, node, start, end, pos):
        if start == end:
            if self.is_min:
                self.tree[node] = (min_p[pos], INF, pos)
            else:
                self.tree[node] = max_p[pos]
            return
        mid = (start + end) // 2
        if pos <= mid:
            self.update(2 * node, start, mid, pos)
        else:
            self.update(2 * node + 1, mid + 1, end, pos)
        self.merge(node)

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            if self.is_min:
                return (INF, INF, -1)
            else:
                return -INF
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(2 * node, start, mid, l, r)
        right = self.query(2 * node + 1, mid + 1, end, l, r)
        if self.is_min:
            if left[0] < right[0]:
                min_val = left[0]
                second = min(left[1], right[0])
                idx = left[2]
            elif right[0] < left[0]:
                min_val = right[0]
                second = min(right[1], left[0])
                idx = right[2]
            else:
                min_val = left[0]
                second = min(left[1], right[1])
                idx = left[2]
            return (min_val, second, idx)
        else:
            return max(left, right)

min_tree = SegTree(N, True)
max_tree = SegTree(N, False)
for _ in range(M):
    op = int(input_data[idx])
    idx += 1
    if op == 1:
        p = int(input_data[idx])
        idx += 1
        i = int(input_data[idx])
        idx += 1
        min_p[i] = min(min_p[i], p)
        max_p[i] = max(max_p[i], p)
        min_tree.update(1, 1, N, i)
        max_tree.update(1, 1, N, i)
    else:
        a = int(input_data[idx])
        idx += 1
        b = int(input_data[idx])
        idx += 1
        max_val = max_tree.query(1, 1, N, a, b)
        min_val, second_val, idx_min = min_tree.query(1, 1, N, a, b)
        if max_p[idx_min] == max_val:
            ans = max_val - second_val
        else:
            ans = max_val - min_val
        print(ans)