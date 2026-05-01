import sys

data = sys.stdin.read().split()
if not data:
    exit()

a, b = data[0], data[1]
pos = {"norte": 0, "leste": 1, "sul": 2, "oeste": 3}

d = abs(pos[a] - pos[b])
print(min(d, 4 - d) * 90)