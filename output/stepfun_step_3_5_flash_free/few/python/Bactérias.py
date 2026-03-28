import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    P = int(data[1])
    d = 0
    atual = 1
    while atual * P <= N:
        atual *= P
        d += 1
    print(d)

if __name__ == "__main__":
    main()