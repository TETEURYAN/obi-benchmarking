
D = int(input().strip())
pontos = [0, 400, 800, 1200, 1600, 2000]
menor_distancia = float('inf')

for ponto in pontos:
    distancia = abs(D - ponto)
    if distancia < menor_distancia:
        menor_distancia = distancia

print(menor_distancia)
