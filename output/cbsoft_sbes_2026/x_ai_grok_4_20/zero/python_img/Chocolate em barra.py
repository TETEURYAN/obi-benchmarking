
N = int(input())
X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())

# Normalizar para 0-based
r1, c1 = X1 - 1, Y1 - 1
r2, c2 = X2 - 1, Y2 - 1

# Meio da barra
mid = N // 2

# Corte horizontal no meio: as figurinhas devem estar em lados diferentes das linhas
# Uma na parte de cima (linha < mid), outra na parte de baixo (linha >= mid)
horizontal_ok = (r1 < mid) != (r2 < mid)

# Corte vertical no meio: as figurinhas devem estar em lados diferentes das colunas
vertical_ok = (c1 < mid) != (c2 < mid)

if horizontal_ok or vertical_ok:
    print("S")
else:
    print("N")
