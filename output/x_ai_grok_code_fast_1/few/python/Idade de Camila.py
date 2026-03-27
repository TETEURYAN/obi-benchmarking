import sys

input_data = sys.stdin.read().split()
idades = [int(x) for x in input_data]
idades.sort()
print(idades[1])