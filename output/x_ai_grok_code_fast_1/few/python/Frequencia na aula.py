import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])

registros = set()

for i in range(1, N + 1):
    registros.add(int(input_data[i]))

print(len(registros))