import sys

data = sys.stdin.read().split()
if not data:
    exit()

c = int(data[0])
seen = set()
fabricados = 0

for i in range(1, c + 1):
    x = int(data[i])
    if x not in seen:
        seen.add(x)
        fabricados += 2

print(fabricados)