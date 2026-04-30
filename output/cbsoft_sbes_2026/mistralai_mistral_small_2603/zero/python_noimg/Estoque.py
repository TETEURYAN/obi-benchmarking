
def main():
    import sys
    data = sys.stdin.read().split()
    ptr = 0
    M = int(data[ptr])
    ptr += 1
    N = int(data[ptr])
    ptr += 1

    estoque = []
    for _ in range(M):
        linha = list(map(int, data[ptr:ptr+N]))
        ptr += N
        estoque.append(linha)

    P = int(data[ptr])
    ptr += 1

    total_vendido = 0
    for _ in range(P):
        I = int(data[ptr]) - 1
        ptr += 1
        J = int(data[ptr]) - 1
        ptr += 1
        if estoque[I][J] > 0:
            estoque[I][J] -= 1
            total_vendido += 1

    print(total_vendido)

if __name__ == "__main__":
    main()
