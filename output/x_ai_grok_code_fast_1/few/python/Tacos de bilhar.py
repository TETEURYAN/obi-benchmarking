import sys

input_data = sys.stdin.read().split()

C = int(input_data[0])

comprimentos = list(map(int, input_data[1:]))

estoque = set()

fabricados = 0

for comp in comprimentos:

    if comp not in estoque:

        estoque.add(comp)

        fabricados += 2

print(fabricados)