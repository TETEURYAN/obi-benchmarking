import sys

def main():
    N = int(sys.stdin.read())
    if N == 0:
        print(4)
        return
    print((2 * N + 1) ** 2)

if __name__ == "__main__":
    main()