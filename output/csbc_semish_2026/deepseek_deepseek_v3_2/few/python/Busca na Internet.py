import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    # segundo = 2 * terceiro
    # primeiro = 2 * segundo
    # primeiro = 2 * (2 * t) = 4 * t
    primeiro = 4 * t
    print(primeiro)

if __name__ == "__main__":
    main()