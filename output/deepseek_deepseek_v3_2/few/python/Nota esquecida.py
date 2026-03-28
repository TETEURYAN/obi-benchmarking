import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A = int(data[0])
    M = int(data[1])
    B = 2 * M - A
    print(B)

if __name__ == "__main__":
    main()