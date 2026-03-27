import sys

def main():
    C, N = map(int, sys.stdin.read().split())
    print(C % N)

if __name__ == "__main__":
    main()