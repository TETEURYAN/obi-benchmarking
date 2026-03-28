import sys

idades = [int(sys.stdin.readline().strip()) for _ in range(3)]
idades.sort()
print(idades[1])