import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    L = int(data[0])
    N = int(data[1])
    maior = L - N + 1
    resultado = maior * maior + (N - 1)
    print(resultado)

if __name__ == "__main__":
    main()