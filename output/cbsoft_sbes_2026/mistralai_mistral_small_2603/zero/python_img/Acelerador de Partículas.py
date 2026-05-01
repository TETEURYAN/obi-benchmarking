
D = int(input().strip())
distancia_restante = D - 3
if distancia_restante < 0:
    print(1)
else:
    modulo = distancia_restante % 8
    if modulo == 0:
        print(1)
    elif modulo == 1 or modulo == 2:
        print(2)
    else:
        print(3)
