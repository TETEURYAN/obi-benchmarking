
def main():
    N = int(input())
    estoque = [0] * (N + 1)
    for i in range(1, N + 1):
        estoque[i] = int(input())
    P = int(input())
    total_vendido = 0
    for _ in range(P):
        I = int(input())
        if estoque[I] > 0:
            estoque[I] -= 1
            total_vendido += 1
    print(total_vendido)

if __name__ == '__main__':
    main()
