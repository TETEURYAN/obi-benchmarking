
import sys

def main():
    N = int(sys.stdin.read())
    if N == 1:
        print('N')
        return
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print('S')
            return
    print('N')

if __name__ == '__main__':
    main()
