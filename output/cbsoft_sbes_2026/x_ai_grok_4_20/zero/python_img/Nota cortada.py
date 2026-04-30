
B = int(input())
T = int(input())

area_total = 160 * 70
area_metade = area_total / 2

# Área do trapézio da esquerda (Felix)
area_felix = ((B + T) * 70) / 2

if area_felix > area_metade:
    print(1)
elif area_felix < area_metade:
    print(2)
else:
    print(0)
