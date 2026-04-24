import sys

data = sys.stdin.read().split()
n = int(data[0])
m = int(data[1])
owned = set()
for i in range(m):
    owned.add(int(data[2 + i]))
print(n - len(owned))