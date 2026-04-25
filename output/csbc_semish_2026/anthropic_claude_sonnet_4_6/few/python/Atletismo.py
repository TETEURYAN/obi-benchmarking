import sys

data = sys.stdin.read().split()
n = int(data[0])
rank = [0] * (n + 1)
for i in range(n):
    athlete = int(data[i + 1])
    rank[athlete] = i + 1
output = []
for i in range(1, n + 1):
    output.append(str(rank[i]))
print('\n'.join(output))