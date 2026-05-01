import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    pesos = [int(next(it)) for _ in range(n)]
    
    min_balde = [0] * (n + 1)
    max_balde = [0] * (n + 1)
    for i in range(1, n + 1):
        p = pesos[i - 1]
        min_balde[i] = p
        max_balde[i] = p

    class SegTree:
        def __init__(self, n, min_vals, max_vals):
            self.n = n
            self.size = 1
            while self.size < n:
                self.size *= 2
            self.tree = [None] * (2 * self.size)
            for i in range(n):
                self.tree[self.size + i] = (max_vals[i + 1], i + 1, -10**18, -1, min_vals[i + 1], i + 1, 10**18, -1)
            for i in range(n, self.size):
                self.tree[self.size + i] = (-10**18, -1, -10**18, -1, 10**18, -1, 10**18, -1)
            for i in range(self.size - 1, 0, -1):
                self.tree[i] = self.combine(self.tree[2 * i], self.tree[2 * i + 1])

        def combine(self, a, b):
            cand_max = []
            if a[1] != -1:
                cand_max.append((a[0], a[1]))
            if a[3] != -1:
                cand_max.append((a[2], a[3]))
            if b[1] != -1:
                cand_max.append((b[0], b[1]))
            if b[3] != -1:
                cand_max.append((b[2], b[3]))
            cand_max.sort(key=lambda x: x[0], reverse=True)
            if cand_max:
                max1, idx_max1 = cand_max[0]
                max2 = -10**18
                idx_max2 = -1
                for val, idx in cand_max[1:]:
                    if idx != idx_max1:
                        max2 = val
                        idx_max2 = idx
                        break
            else:
                max1 = -10**18
                idx_max1 = -1
                max2 = -10**18
                idx_max2 = -1

            cand_min = []
            if a[5] != -1:
                cand_min.append((a[4], a[5]))
            if a[7] != -1:
                cand_min.append((a[6], a[7]))
            if b[5] != -1:
                cand_min.append((b[4], b[5]))
            if b[7] != -1:
                cand_min.append((b[6], b[7]))
            cand_min.sort(key=lambda x: x[0])
            if cand_min:
                min1, idx_min1 = cand_min[0]
                min2 = 10**18
                idx_min2 = -1
                for val, idx in cand_min[1:]:
                    if idx != idx_min1:
                        min2 = val
                        idx_min2 = idx
                        break
            else:
                min1 = 10**18
                idx_min1 = -1
                min2 = 10**18
                idx_min2 = -1

            return (max1, idx_max1, max2, idx_max2, min1, idx_min1, min2, idx_min2)

        def update(self, pos, new_min, new_max):
            idx = self.size + (pos - 1)
            self.tree[idx] = (new_max, pos, -10**18, -1, new_min, pos, 10**18, -1)
            idx //= 2
            while idx:
                self.tree[idx] = self.combine(self.tree[2 * idx], self.tree[2 * idx + 1])
                idx //= 2

        def query(self, l, r):
            l += self.size - 1
            r += self.size - 1
            res_left = None
            res_right = None
            while l <= r:
                if l % 2 == 1:
                    if res_left is None:
                        res_left = self.tree[l]
                    else:
                        res_left = self.combine(res_left, self.tree[l])
                    l += 1
                if r % 2 == 0:
                    if res_right is None:
                        res_right = self.tree[r]
                    else:
                        res_right = self.combine(self.tree[r], res_right)
                    r -= 1
                l //= 2
                r //= 2
            if res_left is None:
                return res_right
            if res_right is None:
                return res_left
            return self.combine(res_left, res_right)

    seg = SegTree(n, min_balde, max_balde)
    output_lines = []
    for _ in range(m):
        tipo = int(next(it))
        if tipo == 1:
            p = int(next(it))
            i = int(next(it))
            if p < min_balde[i]:
                min_balde[i] = p
            if p > max_balde[i]:
                max_balde[i] = p
            seg.update(i, min_balde[i], max_balde[i])
        else:
            a = int(next(it))
            b = int(next(it))
            node = seg.query(a, b)
            if node[1] != node[5]:
                ans = node[0] - node[4]
            else:
                op1 = node[0] - node[6]
                op2 = node[2] - node[4]
                ans = max(op1, op2)
            output_lines.append(str(ans))
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()