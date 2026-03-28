import sys
from collections import Counter

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    def query(self, idx):
        s = 0
        while idx:
            s += self.tree[idx]
            idx -= idx & -idx
        return s

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    X1 = int(next(it))
    X2 = int(next(it))
    lines = []
    for _ in range(N):
        A = int(next(it))
        B = int(next(it))
        lines.append((A, B))

    if X1 == X2:
        L_vals = [A * X1 + B for A, B in lines]
        cnt = Counter(L_vals)
        total = sum(c * (c - 1) // 2 for c in cnt.values())
        print(total)
        return

    L_vals = []
    R_vals = []
    for A, B in lines:
        L = A * X1 + B
        R = A * X2 + B
        L_vals.append(L)
        R_vals.append(R)

    cnt_L = Counter(L_vals)
    soma_L = sum(c * (c - 1) // 2 for c in cnt_L.values())
    cnt_R = Counter(R_vals)
    soma_R = sum(c * (c - 1) // 2 for c in cnt_R.values())

    pairs = list(zip(L_vals, R_vals))
    pairs.sort(key=lambda x: (x[0], x[1]))
    R_seq = [r for _, r in pairs]

    all_R = sorted(set(R_vals))
    mapping = {val: idx + 1 for idx, val in enumerate(all_R)}
    bit = BIT(len(all_R))
    inversoes = 0
    count_processed = 0
    for r in R_seq:
        idx = mapping[r]
        inversoes += count_processed - bit.query(idx)
        bit.update(idx, 1)
        count_processed += 1

    total = inversoes + soma_L + soma_R
    print(total)

if __name__ == "__main__":
    main()