import sys

def pode_formar_trilha(pecas):
    grau = [0] * 7
    adj = [[0] * 7 for _ in range(7)]
    usado = [False] * 7

    for x, y in pecas:
        if x == y:
            grau[x] += 2
            adj[x][x] += 1
        else:
            grau[x] += 1
            grau[y] += 1
            adj[x][y] += 1
            adj[y][x] += 1
        usado[x] = True
        usado[y] = True

    vertices = [i for i in range(7) if grau[i] > 0]
    if not vertices:
        return True

    visitado = [False] * 7
    pilha = [vertices[0]]
    visitado[vertices[0]] = True

    while pilha:
        v = pilha.pop()
        for u in range(7):
            if adj[v][u] > 0 and not visitado[u]:
                visitado[u] = True
                pilha.append(u)

    for v in vertices:
        if not visitado[v]:
            return False

    impares = sum(1 for g in grau if g % 2 == 1)
    return impares == 0 or impares == 2

def main():
    data = sys.stdin.read().strip().split()
    i = 0
    teste = 1
    out = []

    while i < len(data):
        n = int(data[i])
        i += 1
        if n == 0:
            break

        pecas = []
        for _ in range(n):
            x = int(data[i])
            y = int(data[i + 1])
            i += 2
            pecas.append((x, y))

        out.append(f"Teste {teste}")
        out.append("sim" if pode_formar_trilha(pecas) else "nao")
        out.append("")
        teste += 1

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
