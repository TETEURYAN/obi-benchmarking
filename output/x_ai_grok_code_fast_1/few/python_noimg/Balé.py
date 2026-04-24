import sys

class Fenwick:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & -index
        return sum_val

data = sys.stdin.read().split()
N = int(data[0])
a = list(map(int, data[1:]))

ft = Fenwick(100001)
count = 0
for j in range(N):
    greater = j - ft.query(a[j])
    count += greater
    ft.update(a[j], 1)

print(count)