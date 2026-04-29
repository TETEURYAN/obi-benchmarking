import sys

def main():
    n, t = map(int, sys.stdin.readline().split())

    if t == 0:
        print(n)
    elif t == 1:
        print(n * (n - 1))
    else:  # t == 2
        # Escolha 3 posições distintas; o rei deve ficar entre as duas torres.
        # Para cada trio de posições, há exatamente 1 arranjo válido: T K T.
        print(n * (n - 1) * (n - 2) // 6)

if __name__ == "__main__":
    main()
