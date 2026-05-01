
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    N = int(data[0])
    C = int(data[1])
    M = int(data[2])

    carimbadas = set(map(int, data[3:3+C]))
    compradas = list(map(int, data[3+C:3+C+M]))

    compradas_set = set(compradas)
    faltantes = carimbadas - compradas_set

    print(len(faltantes))

if __name__ == "__main__":
    main()
