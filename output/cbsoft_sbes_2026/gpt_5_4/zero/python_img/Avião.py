F, C, E, B = map(int, input().split())

assentos_economica = (F - E + 1) * C

if B > assentos_economica:
    print("PROXIMO VOO")
else:
    fila = E + (B - 1) // C
    pos = chr(ord('A') + (B - 1) % C)
    print(fila, pos)