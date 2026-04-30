
L = int(input())
C = int(input())

if L == 1 and C == 1:
    print(1)
    print(0)
else:
    tipo1 = (L * C) + (L - 1) * (C - 1)
    tipo2 = 2 * (L - 1) * (C - 1)
    print(tipo1)
    print(tipo2)
