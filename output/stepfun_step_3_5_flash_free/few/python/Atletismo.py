import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
ordem = list(map(int, data[1:1+n]))
pos = [0] * (n + 1)
for i, atleta in enumerate(ordem, start=1):
    pos[atleta] = i
for i in range(1, n + 1):
    print(pos[i])