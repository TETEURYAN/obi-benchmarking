
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    M = int(data[idx])
    N = int(data[idx + 1])
    idx += 2

    estoque = []
    for _ in range(M):
        linha = list(map(int, data[idx:idx + N]))
        estoque.append(linha)
        idx += N

    P = int(data[idx])
    idx += 1

    total_vendido = 0
    for _ in range(P):
        I = int(data[idx]) - 1
        J = int(data[idx + 1]) - 1
        idx += 2
        if estoque[I][J] > 0:
            estoque[I][J] -= 1
            total_vendido += 1

    print(total_vendido)

if __name__ == "__main__":
    main()
