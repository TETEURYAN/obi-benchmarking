
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    x1, y1 = int(data[1]), int(data[2])
    x2, y2 = int(data[3]), int(data[4])

    # Verifica se é possível separar as figurinhas com um corte vertical
    if (x1 <= N // 2 and x2 > N // 2) or (x2 <= N // 2 and x1 > N // 2):
        print("S")
        return

    # Verifica se é possível separar as figurinhas com um corte horizontal
    if (y1 <= N // 2 and y2 > N // 2) or (y2 <= N // 2 and y1 > N // 2):
        print("S")
        return

    print("N")

if __name__ == "__main__":
    main()
