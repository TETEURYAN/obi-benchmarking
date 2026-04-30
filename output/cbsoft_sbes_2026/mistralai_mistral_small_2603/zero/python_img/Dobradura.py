import sys

def main():
    teste = 1
    for line in sys.stdin:
        N = int(line.strip())
        if N == -1:
            break
        if N == 0:
            pecas = 1
        else:
            pecas = (2 ** N + 1) ** 2
        print(f"Teste {teste}")
        print(pecas)
        print()
        teste += 1

if __name__ == "__main__":
    main()