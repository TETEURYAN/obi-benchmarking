import sys

notas = list(map(float, sys.stdin.read().split()))
notas.sort()
soma = notas[1] + notas[2] + notas[3]
print(f"{soma:.1f}")