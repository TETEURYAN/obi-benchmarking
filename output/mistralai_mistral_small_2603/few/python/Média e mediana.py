
import sys

def main():
    A, B = map(int, sys.stdin.read().split())
    if A > B:
        A, B = B, A
    C = 3 * B - 2 * A
    print(C)

if __name__ == "__main__":
    main()
