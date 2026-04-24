import sys

def main():
    a, b, c, d = map(int, sys.stdin.read().split())
    if (a == c and b == d) or (a == b and c == d):
        print('V')
    else:
        print('F')

if __name__ == '__main__':
    main()