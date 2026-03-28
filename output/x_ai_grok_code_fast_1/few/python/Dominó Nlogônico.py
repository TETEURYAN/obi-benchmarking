import sys
import bisect

class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [float('-inf')] * (4 * n)

    def update(self, idx, val):
        self._update(1, 1, self.n, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, left, right):
        return self._query(1, 1, self.n, left, right)

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return float('-inf')
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self._query(2 * node, start, mid, left, right), self._query(2 * node + 1, mid + 1, end, left, right))

input_data = sys.stdin.read().split()
N = int(input_data[0])
X = list(map(int, input_data[1:1 + N]))
H = list(map(int, input_data[1 + N:1 + 2 * N]))

last = [0] * (N + 1)
for i in range(1, N + 1):
    target = X[i - 1] + H[i - 1]
    k = bisect.bisect_right(X[i:], target)
    if k == 0:
        last[i] = i
    else:
        last[i] = i + k

st = SegTree(N)
max_R = [0] * (N + 1)
max_R[N] = X[N - 1] + H[N - 1]
st.update(N, max_R[N])

for i in range(N - 1, 0, -1):
    if last[i] == i:
        max_R[i] = X[i - 1] + H[i - 1]
    else:
        max_in = st.query(i + 1, last[i])
        max_R[i] = max(X[i - 1] + H[i - 1], max_in)
    st.update(i, max_R[i])

ans = []
for i in range(1, N + 1):
    k = bisect.bisect_right(X, max_R[i])
    count = k - i + 1
    ans.append(str(count))

print(' '.join(ans))