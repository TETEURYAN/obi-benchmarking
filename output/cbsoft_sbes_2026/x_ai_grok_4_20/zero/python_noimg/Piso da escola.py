
L = int(input())
C = int(input())

if L == 1 and C == 1:
    print(1)
    print(0)
else:
    tipo1 = (L * C * 2) - (L + C - 2) * 2 + 1
    tipo2 = (L + C - 2) * 2
    print(tipo1)
    print(tipo2)
