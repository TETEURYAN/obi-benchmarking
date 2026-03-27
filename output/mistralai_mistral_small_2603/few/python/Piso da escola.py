
import sys

def main():
    data = sys.stdin.read().split()
    L = int(data[0])
    C = int(data[1])

    tipo1 = L * C + (L - 1) * (C - 1)
    tipo2 = 2 * (L - 1) + 2 * (C - 1)

    print(tipo1)
    print(tipo2)

if __name__ == "__main__":
    main()
