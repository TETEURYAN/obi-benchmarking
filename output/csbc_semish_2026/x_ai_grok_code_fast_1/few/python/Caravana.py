import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
pesos = [int(input_data[i+1]) for i in range(N)]
S = sum(pesos)
peso_final = S // N
for p in pesos:
    print(peso_final - p)