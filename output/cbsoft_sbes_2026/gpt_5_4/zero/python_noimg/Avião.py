F, C, E, B = map(int, input().split())

assentos_economica = (F - E + 1) * C

if B > assentos_economica:
    print("PROXIMO VOO")
else:
    indice = B - 1
    fileira = E + indice // C
    posicao = chr(ord('A') + indice % C)
    print(fileira, posicao)