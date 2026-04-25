import sys

data = sys.stdin.read().split()
V = int(data[0])
A = int(data[1])
F = int(data[2])
P = int(data[3])

contas = [A, F, P]
contas.sort()

soma = 0
count = 0
for c in contas:
    if soma + c <= V:
        soma += c
        count += 1
    else:
        break

print(count)