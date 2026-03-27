
n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# As figurinhas devem estar em lados opostos em relação ao corte
# Corte horizontal: uma figurinha acima da linha média e a outra abaixo
# Corte vertical: uma figurinha à esquerda da coluna média e a outra à direita

# Para um corte horizontal, as figurinhas devem estar em linhas diferentes em relação à metade
# Para um corte vertical, as figurinhas devem estar em colunas diferentes em relação à metade

# Verifica se é possível com corte horizontal
# A linha média está entre n//2 e n//2 + 1
# Ou seja, figurinhas em linhas <= n//2 e > n//2
# Mas como o corte pode ser feito em qualquer lugar entre linhas, basta que as figurinhas não estejam no mesmo lado
# Ou seja, uma em linha <= n//2 e outra > n//2
# Mas como o corte pode ser feito entre linhas, basta que as figurinhas estejam em lados diferentes em relação à metade

# Para corte horizontal: uma figurina em linha <= n//2 e outra > n//2
# Para corte vertical: uma figurina em coluna <= n//2 e outra > n//2

# Mas note que o corte pode ser feito entre linhas, então basta que as figurinhas estejam em lados diferentes em relação à metade

# Verifica se é possível com corte horizontal
if (x1 <= n // 2 and x2 > n // 2) or (x1 > n // 2 and x2 <= n // 2):
    print('S')
elif (y1 <= n // 2 and y2 > n // 2) or (y1 > n // 2 and y2 <= n // 2):
    print('S')
else:
    print('N')
