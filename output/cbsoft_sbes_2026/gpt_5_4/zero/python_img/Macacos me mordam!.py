import sys

def ceil_div(a, b):
    return -((-a) // b)

def floor_div(a, b):
    return a // b

class LiChaoMin:
    __slots__ = ("xs", "n", "INF", "m", "b")
    def __init__(self, xs):
        self.xs = xs
        n = 1
        while n < len(xs):
            n <<= 1
        self.n = n
        self.INF = 10**30
        self.m = [0] * (2 * n)
        self.b = [self.INF] * (2 * n)

    def _f(self, m, b, x):
        return m * x + b

    def add_line(self, m_new, b_new):
        self._add_line(1, 0, self.n - 1, m_new, b_new)

    def _add_line(self, node, l, r, m_new, b_new):
        if self.b[node] == self.INF:
            self.m[node] = m_new
            self.b[node] = b_new
            return

        xl = self.xs[l] if l < len(self.xs) else self.xs[-1]
        xr = self.xs[r] if r < len(self.xs) else self.xs[-1]
        mid = (l + r) >> 1
        xm = self.xs[mid] if mid < len(self.xs) else self.xs[-1]

        m_cur, b_cur = self.m[node], self.b[node]

        if self._f(m_new, b_new, xm) < self._f(m_cur, b_cur, xm):
            self.m[node], self.b[node], m_new, b_new = m_new, b_new, m_cur, b_cur
            m_cur, b_cur = self.m[node], self.b[node]

        if l == r:
            return

        if self._f(m_new, b_new, xl) < self._f(m_cur, b_cur, xl):
            self._add_line(node << 1, l, mid, m_new, b_new)
        elif self._f(m_new, b_new, xr) < self._f(m_cur, b_cur, xr):
            self._add_line(node << 1 | 1, mid + 1, r, m_new, b_new)

    def query(self, x_idx):
        x = self.xs[x_idx]
        node = 1
        l = 0
        r = self.n - 1
        ans = self.INF
        while True:
            if self.b[node] != self.INF:
                v = self.m[node] * x + self.b[node]
                if v < ans:
                    ans = v
            if l == r:
                break
            mid = (l + r) >> 1
            if x_idx <= mid:
                node = node << 1
                r = mid
            else:
                node = node << 1 | 1
                l = mid + 1
        return ans

def main():
    input = sys.stdin.readline
    N = int(input())
    trees = [tuple(map(int, input().split())) for _ in range(N)]
    trees.sort()
    X = [x for x, h in trees]
    H = [h for x, h in trees]

    if N == 2:
        print(1)
        return

    # nearest greater-or-equal to left/right
    L = [-1] * N
    st = []
    for i in range(N):
        while st and H[st[-1]] < H[i]:
            st.pop()
        L[i] = st[-1] if st else -1
        st.append(i)

    R = [N] * N
    st = []
    for i in range(N - 1, -1, -1):
        while st and H[st[-1]] < H[i]:
            st.pop()
        R[i] = st[-1] if st else N
        st.append(i)

    # Build intervals [l_j, r_j] of trees visible from j
    lvis = [0] * N
    rvis = [0] * N

    hull = []
    ptr = 0
    for j in range(N):
        while len(hull) >= 2:
            a = hull[-2]
            b = hull[-1]
            left = ceil_div(H[b] - H[a], X[b] - X[a])
            right = ceil_div(H[j] - H[b], X[j] - X[b])
            if left >= right:
                hull.pop()
                if ptr > len(hull) - 1:
                    ptr = len(hull) - 1
            else:
                break
        hull.append(j)
        if j == 0:
            lvis[j] = 0
        else:
            while ptr + 1 < len(hull):
                a = hull[ptr]
                b = hull[ptr + 1]
                if ceil_div(H[j] - H[a], X[j] - X[a]) <= ceil_div(H[j] - H[b], X[j] - X[b]):
                    ptr += 1
                else:
                    break
            lvis[j] = hull[ptr]

    hull = []
    ptr = 0
    for jj in range(N - 1, -1, -1):
        j = jj
        while len(hull) >= 2:
            a = hull[-2]
            b = hull[-1]
            left = floor_div(H[b] - H[a], X[a] - X[b])
            right = floor_div(H[j] - H[b], X[b] - X[j])
            if left <= right:
                hull.pop()
                if ptr > len(hull) - 1:
                    ptr = len(hull) - 1
            else:
                break
        hull.append(j)
        if j == N - 1:
            rvis[j] = N - 1
        else:
            while ptr + 1 < len(hull):
                a = hull[ptr]
                b = hull[ptr + 1]
                if floor_div(H[j] - H[a], X[a] - X[j]) >= floor_div(H[j] - H[b], X[b] - X[j]):
                    ptr += 1
                else:
                    break
            rvis[j] = hull[ptr]

    # DP with segment tree over intervals:
    # dp[i] = 1 + min dp[j] such that i in [lvis[j], rvis[j]]
    # Process layers BFS-like using range activation and point query.
    INF = 10**18
    dp = [INF] * N
    dp[0] = 0

    events_add = [[] for _ in range(N + 1)]
    events_rem = [[] for _ in range(N + 1)]

    xs = list(range(N))
    lichao = LiChaoMin(xs)

    # We need multiset of constants over active intervals.
    # Since Li Chao doesn't support deletion for constants, use sweep by layers instead.

    current = [0]
    dist = 0
    seen = [False] * N
    seen[0] = True

    while current:
        if seen[N - 1]:
            break

        diff = [0] * (N + 1)
        for j in current:
            l = lvis[j]
            r = rvis[j]
            diff[l] += 1
            if r + 1 < N:
                diff[r + 1] -= 1

        nxt = []
        acc = 0
        for i in range(N):
            acc += diff[i]
            if acc > 0 and not seen[i]:
                seen[i] = True
                dp[i] = dist + 1
                nxt.append(i)

        current = nxt
        dist += 1

    print(dp[N - 1])

if __name__ == "__main__":
    main()
