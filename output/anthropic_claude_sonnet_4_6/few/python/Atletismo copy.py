import sys

data = sys.stdin.read().split()
n = int(data[0])
rank = [0] * (n + 1)
for i in range(n):
    athlete = int(data[1 + i])
    rank[athlete] = i + 1
out = []
for i in range(1, n + 1):
    out.append(str(rank[i]))
print('\n'.join(out))