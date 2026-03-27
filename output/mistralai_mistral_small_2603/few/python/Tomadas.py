import sys

def main():
    T1, T2, T3, T4 = map(int, sys.stdin.read().split())
    total = T1 + T2 + T3 + T4 - 3
    print(total)

if __name__ == "__main__":
    main()