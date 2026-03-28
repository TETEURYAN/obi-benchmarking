import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
C = int(input_data[1])
M = int(input_data[2])

carimbadas = set(map(int, input_data[3:3+C]))
compradas = set(map(int, input_data[3+C:]))

faltam = 0
for fig in carimbadas:
    if fig not in compradas:
        faltam += 1

print(faltam)