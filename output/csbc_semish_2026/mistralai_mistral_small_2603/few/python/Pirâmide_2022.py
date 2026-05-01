
import sys

def main():
    N = int(sys.stdin.readline())
    for i in range(1, N + 1):
        row = []
        for j in range(1, N + 1):
            val = min(i, j, N - i + 1, N - j + 1)
            row.append(str(val))
        print(' '.join(row))

if __name__ == "__main__":
    main()
