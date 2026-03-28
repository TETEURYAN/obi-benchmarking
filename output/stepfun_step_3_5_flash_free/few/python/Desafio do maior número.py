import sys

numeros = list(map(int, sys.stdin.read().split()))
print(max(numeros[:-1]))