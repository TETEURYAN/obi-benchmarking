import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    C, N = map(int, data)
    resultado = C % N
    print(resultado)

if __name__ == "__main__":
    main()