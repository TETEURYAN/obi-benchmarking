import sys
from collections import defaultdict

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
D = int(input_data[idx])
idx += 1
C = [int(input_data[idx + i]) for i in range(N)]

prefix = [0]
for c in C:
    prefix.append(prefix[-1] + c)
total = prefix[-1]

# Continuous subarrays
count1 = 0
counter = defaultdict(int)
counter[0] = 1
for j in range(1, N + 1):
    target = prefix[j] - D
    if target in counter:
        count1 += counter[target]
    counter[prefix[j]] += 1

# Extremities
diff = D - total
all_prefix = prefix[:-1]  # 0 to N-1
unique = sorted(set(all_prefix))
rank_map = {val: i + 1 for i, val in enumerate(unique)}
M = len(unique)

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

fenwick = Fenwick(M)
count2 = 0
for i in range(N - 1, 0, -1):
    target = prefix[i] - diff
    if target in rank_map:
        rank = rank_map[target]
        count2 += fenwick.query(rank)
    rank_i = rank_map[prefix[i]]
    fenwick.update(rank_i, 1)

print(count1 + count2)