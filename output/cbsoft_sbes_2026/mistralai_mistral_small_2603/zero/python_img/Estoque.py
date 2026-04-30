
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    M = int(data[idx])
    idx += 1
    N = int(data[idx])
    idx += 1

    estoque = []
    for _ in range(M):
        linha = list(map(int, data[idx:idx+N]))
        idx += N
        estoque.append(linha)

    P = int(data[idx])
    idx += 1

    total_vendido = 0
    for _ in range(P):
        I = int(data[idx]) - 1
        idx += 1
        J = int(data[idx]) - 1
        idx += 1
        if estoque[I][J] > 0:
            estoque[I][J] -= 1
            total_vendido += 1

    print(total_vendido)

if __name__ == "__main__":
    main()
