import sys

def main():
    p, r = map(int, sys.stdin.read().split())
    if p == 1:
        print('B')
    else:
        if r == 1:
            print('A')
        else:
            print('C')

if __name__ == '__main__':
    main()