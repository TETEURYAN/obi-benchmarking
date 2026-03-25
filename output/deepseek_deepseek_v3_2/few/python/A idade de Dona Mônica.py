import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    M = int(data[0])
    A = int(data[1])
    B = int(data[2])
    C = M - A - B
    print(max(A, B, C))

if __name__ == "__main__":
    main()