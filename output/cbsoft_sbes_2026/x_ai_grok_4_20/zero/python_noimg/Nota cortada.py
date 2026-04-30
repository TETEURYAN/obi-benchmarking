
B = int(input())
T = int(input())

area_total = 160 * 70
area_meia = area_total / 2

# Área à esquerda do corte: trapézio com bases B e T, altura 70
area_felix = (B + T) * 70 / 2

if area_felix > area_meia:
    print(1)
elif area_felix < area_meia:
    print(2)
else:
    print(0)
