import sys

input_data = sys.stdin.read().split()
D = int(input_data[0])

pontos = [0, 400, 800, 1200, 1600, 2000]
distancia = min(abs(D - p) for p in pontos)
print(distancia)