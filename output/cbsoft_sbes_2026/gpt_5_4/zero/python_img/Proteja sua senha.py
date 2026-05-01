import sys

data = sys.stdin.read().split()
i = 0
teste = 1
out = []

while True:
    n = int(data[i])
    i += 1
    if n == 0:
        break

    possiveis = [set(range(10)) for _ in range(6)]

    for _ in range(n):
        pares = {
            'A': {int(data[i]), int(data[i + 1])},
            'B': {int(data[i + 2]), int(data[i + 3])},
            'C': {int(data[i + 4]), int(data[i + 5])},
            'D': {int(data[i + 6]), int(data[i + 7])},
            'E': {int(data[i + 8]), int(data[i + 9])},
        }
        i += 10

        senha_cod = data[i:i + 6]
        i += 6

        for pos in range(6):
            possiveis[pos] &= pares[senha_cod[pos]]

    senha = [str(next(iter(p))) for p in possiveis]

    out.append(f"Teste {teste}")
    out.append(" ".join(senha))
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))