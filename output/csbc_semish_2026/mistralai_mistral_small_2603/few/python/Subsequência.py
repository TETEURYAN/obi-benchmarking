
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    idx = 0
    A = int(data[idx])
    B = int(data[idx + 1])
    idx += 2

    SA = list(map(int, data[idx:idx + A]))
    idx += A

    SB = list(map(int, data[idx:idx + B]))

    i = j = 0
    while i < A and j < B:
        if SA[i] == SB[j]:
            j += 1
        i += 1

    print('S' if j == B else 'N')

if __name__ == "__main__":
    main()
