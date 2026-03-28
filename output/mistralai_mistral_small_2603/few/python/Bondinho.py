import sys

def main():
    A = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    if A + M <= 50:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()