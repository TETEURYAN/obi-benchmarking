import sys

input_data = sys.stdin.read().split()
idx = 0

N = int(input_data[idx])
idx += 1
Q = int(input_data[idx])
idx += 1

A = [0] * (N + 1)
for i in range(1, N + 1):
    A[i] = int(input_data[idx])
    idx += 1

class FenwickTree:
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

ft = FenwickTree(N)
for i in range(1, N + 1):
    ft.update(i, A[i])

for _ in range(Q):
    event_type = int(input_data[idx])
    idx += 1
    K = int(input_data[idx])
    idx += 1
    if event_type == 0:
        P = int(input_data[idx])
        idx += 1
        delta = P - A[K]
        A[K] = P
        ft.update(K, delta)
    else:
        print(ft.query(K))