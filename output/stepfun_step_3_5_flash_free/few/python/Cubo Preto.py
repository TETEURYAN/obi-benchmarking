import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    k = N - 2
    zero = k ** 3
    um = 6 * k * k
    dois = 12 * k
    tres = 8
    print(zero)
    print(um)
    print(dois)
    print(tres)

if __name__ == "__main__":
    main()