import sys

data = sys.stdin.read().split()
P = int(data[0])
D1 = int(data[1])
D2 = int(data[2])

soma = D1 + D2
paridade = soma % 2

if paridade == P:
    print(0)
else:
    print(1)