import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
pos = [0] * (n + 1)

for i in range(1, n + 1):
    atleta = data[i]
    pos[atleta] = i

sys.stdout.write("\n".join(map(str, pos[1:])))