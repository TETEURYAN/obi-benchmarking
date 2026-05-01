
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
arrows = []
index = 1
for i in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    arrows.append((x, y))
    index += 2

penalties = [0] * N
prev_p = 0
points = []

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx
    
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

MAX_COORD = 2000001
ft = FenwickTree(MAX_COORD)

def get_dist_sq(x, y):
    return x * x + y * y

for k in range(N):
    xr = arrows[k][0] + prev_p
    yr = arrows[k][1] + prev_p
    dist_sq = get_dist_sq(xr, yr)
    
    if k == 0:
        p = 0
    else:
        p = ft.query(dist_sq + 1)
    
    penalties[k] = p
    prev_p = p
    
    coord = dist_sq
    if coord < 0:
        coord = 0
    if coord >= MAX_COORD:
        coord = MAX_COORD - 1
    ft.update(coord + 1, 1)

for p in penalties:
    print(p)
