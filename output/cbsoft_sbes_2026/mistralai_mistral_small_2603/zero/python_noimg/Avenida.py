
D = int(input().strip())

pontos_onibus = [0, 400, 800, 1200, 1600, 2000]

distancia_minima = float('inf')

for ponto in pontos_onibus:
    distancia = abs(D - ponto)
    if distancia < distancia_minima:
        distancia_minima = distancia

print(distancia_minima)
