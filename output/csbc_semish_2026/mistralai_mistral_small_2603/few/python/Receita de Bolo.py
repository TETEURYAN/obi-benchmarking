import sys

def main():
    A, B, C = map(int, sys.stdin.read().split())
    max_bolos = min(A // 2, B // 3, C // 5)
    print(max_bolos)

if __name__ == "__main__":
    main()