
def main():
    N = int(input().strip())
    estoque = []
    for _ in range(N):
        estoque.append(int(input().strip()))
    P = int(input().strip())
    total_vendido = 0
    for _ in range(P):
        I = int(input().strip()) - 1
        if 0 <= I < N and estoque[I] > 0:
            estoque[I] -= 1
            total_vendido += 1
    print(total_vendido)

if __name__ == "__main__":
    main()
