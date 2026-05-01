
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    N = int(data[0])
    A, B, C, D, E, F, G = map(int, data[1:8])

    total = A + B + C - D - E - F + G
    if total > N:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()
