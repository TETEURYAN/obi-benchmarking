B = int(input())
T = int(input())

# Área do pedaço da esquerda (trapézio) = (B + T) * 70 / 2
# Comparando com metade da nota: 160*70/2 = 5600
# Basta comparar B + T com 160
s = B + T

if s > 160:
    print(1)
elif s < 160:
    print(2)
else:
    print(0)