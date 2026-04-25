import sys

P, D1, D2 = map(int, sys.stdin.read().split())
soma = D1 + D2
paridade = soma % 2
winner = 0 if P == paridade else 1
print(winner)