import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

idx = 0
n = int(data[idx])
idx += 1

fila = list(map(int, data[idx:idx + n]))
idx += n

m = int(data[idx])
idx += 1

sairam = set(map(int, data[idx:idx + m]))

resultado = [str(x) for x in fila if x not in sairam]
print(' '.join(resultado))