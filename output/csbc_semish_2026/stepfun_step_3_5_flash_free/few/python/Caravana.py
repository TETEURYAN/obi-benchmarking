import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
pesos = list(map(int, data[1:1+n]))
media = sum(pesos) // n
for p in pesos:
    print(media - p)