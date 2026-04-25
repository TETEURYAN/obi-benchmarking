import sys

input_data = sys.stdin.read().split()
idx = 0
L = int(input_data[idx])
idx += 1
C = int(input_data[idx])
idx += 1
A = []
for i in range(L):
    row = [int(x) for x in input_data[idx:idx + C]]
    A.append(row)
    idx += C

D = [[0] * (C - 1) for _ in range(L)]
for i in range(L):
    for j in range(C - 1):
        D[i][j] = A[i][j + 1] - A[i][j]

diff = [[0] * (C - 1) for _ in range(L - 1)]
for r in range(L - 1):
    for j in range(C - 1):
        diff[r][j] = D[r + 1][j] - D[r][j]

class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        logn = 0
        while (1 << logn) <= n:
            logn += 1
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        self.st = [[0] * logn for _ in range(n)]
        for i in range(n):
            self.st[i][0] = arr[i]
        for j in range(1, logn):
            for i in range(n - (1 << j) + 1):
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])

    def query(self, l, r):
        k = self.log[r - l + 1]
        return min(self.st[l][k], self.st[r - (1 << k) + 1][k])

st = [SparseTable(diff[r]) for r in range(L - 1)]

ans = 0
for c1 in range(1, C + 1):
    for c2 in range(c1, C + 1):
        cols = c2 - c1 + 1
        if cols < 2:
            continue
        max_len = 1
        current_len = 1
        for r in range(1, L):
            min_d = st[r - 1].query(c1 - 1, c2 - 2)
            if min_d >= 0:
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)
        if max_len >= 2:
            ans = max(ans, max_len * cols)

print(ans)