import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
tamanhos = list(map(int, input_data[1:]))
substituir = 0
reforcar = 0
for x in tamanhos:
    if x < 50:
        substituir += 1
    elif x < 85:
        reforcar += 1
print(substituir, reforcar)