
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    horizontal = list(map(int, data[1:n+1]))

    pos = [0] * (n + 1)
    for idx, num in enumerate(horizontal):
        pos[num] = idx

    fenwick = FenwickTree(n)
    inversions = 0

    for i in range(n, 0, -1):
        inversions += fenwick.query(pos[i])
        fenwick.update(pos[i] + 1, 1)

    print(inversions)

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 2)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

if __name__ == "__main__":
    main()
