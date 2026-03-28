import sys

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
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & -idx
        return s

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    levels = list(map(int, data[1:1 + n]))
    max_level = 100000
    bit = BIT(max_level)
    total_inv = 0
    for i, h in enumerate(levels):
        count_le = bit.query(h)
        total_inv += i - count_le
        bit.update(h, 1)
    print(total_inv)

if __name__ == "__main__":
    main()