
C = int(input())
A = int(input())

if A == 0:
    print(0)
else:
    viagens = (A + C - 1) // (C - 1)
    print(viagens)
