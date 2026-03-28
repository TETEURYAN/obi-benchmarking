import sys

data = sys.stdin.read().split()
N = int(data[0])
acessos = [int(x) for x in data[1:]]
soma = 0
dias = 0
for a in acessos:
    soma += a
    dias += 1
    if soma >= 1000000:
        break
print(dias)