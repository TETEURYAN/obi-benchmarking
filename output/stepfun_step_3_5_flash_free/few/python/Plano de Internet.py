import sys

data = sys.stdin.read().split()
if not data:
    exit()
X = int(data[0])
N = int(data[1])
soma = sum(map(int, data[2:2+N]))
print((N + 1) * X - soma)