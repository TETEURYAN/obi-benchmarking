import sys

data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1
queue = []
for i in range(n):
    queue.append(int(data[idx])); idx += 1
m = int(data[idx]); idx += 1
removed = set()
for i in range(m):
    removed.add(int(data[idx])); idx += 1

result = [x for x in queue if x not in removed]
print(*result)