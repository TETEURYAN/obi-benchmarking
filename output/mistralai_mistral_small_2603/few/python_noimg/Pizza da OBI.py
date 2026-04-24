
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    G = int(data[1])
    M = int(data[2])

    total_pedacos = G * 8 + M * 6
    distribuidos = min(N, total_pedacos)
    sobras = total_pedacos - distribuidos
    print(sobras)

if __name__ == "__main__":
    main()
