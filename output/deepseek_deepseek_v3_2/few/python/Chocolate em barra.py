import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    X1 = int(next(it))
    Y1 = int(next(it))
    X2 = int(next(it))
    Y2 = int(next(it))

    # Corte vertical: x = N/2
    if X1 <= N//2 and X2 > N//2 or X1 > N//2 and X2 <= N//2:
        print("S")
        return

    # Corte horizontal: y = N/2
    if Y1 <= N//2 and Y2 > N//2 or Y1 > N//2 and Y2 <= N//2:
        print("S")
        return

    print("N")

if __name__ == "__main__":
    main()