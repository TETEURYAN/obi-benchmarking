import sys

def main():
    data = sys.stdin.read().split()
    A = int(data[0])
    M = int(data[1])
    B = 2 * M - A
    print(B)

if __name__ == "__main__":
    main()