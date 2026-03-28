import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])

compradas = set()
for i in range(m):
    compradas.add(int(data[2 + i]))

print(n - len(compradas))