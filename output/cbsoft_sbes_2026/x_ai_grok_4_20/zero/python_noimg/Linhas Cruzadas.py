
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:]))

pos = [0] * (N + 1)
for i in range(N):
    pos[P[i]] = i

fenwick = [0] * (N + 2)

def update(idx):
    while idx <= N:
        fenwick[idx] += 1
        idx += idx & -idx

def query(idx):
    res = 0
    while idx > 0:
        res += fenwick[idx]
        idx -= idx & -idx
    return res

ans = 0
for v in range(1, N + 1):
    idx = pos[v] + 1
    ans += query(N) - query(idx)
    update(idx)

print(ans)
