import sys

def main():
    N = int(sys.stdin.read())
    if N == 0:
        print('*')
        print('*')
        return
    if N <= 5:
        left = 'I' * N
        right = '*'
    else:
        left = 'IIIII'
        right = 'I' * (N - 5)
    print(left)
    print(right)

if __name__ == '__main__':
    main()