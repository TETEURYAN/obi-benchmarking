import sys

data = sys.stdin.read().split()
if not data:
    exit()

L = int(data[0])
N = int(data[1])

q, r = divmod(L, N)
ans = r * (q + 1) * (q + 1) + (N - r) * q * q

print(ans)