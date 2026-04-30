
F, C, E, B = map(int, input().split())

total_economica = (F - E + 1) * C
if B > total_economica:
    print("PROXIMO VOO")
else:
    fileira = E + (B - 1) // C
    posicao = chr(ord('A') + (B - 1) % C)
    print(f"{fileira} {posicao}")
