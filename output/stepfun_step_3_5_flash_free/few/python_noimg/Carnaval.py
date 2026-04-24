import sys

data = sys.stdin.read().split()
if not data:
    exit()
notas = [float(x) for x in data[:5]]
notas_int = [int(round(n * 10)) for n in notas]
notas_int.sort()
soma = sum(notas_int[1:4])
print(f"{soma / 10.0:.1f}")