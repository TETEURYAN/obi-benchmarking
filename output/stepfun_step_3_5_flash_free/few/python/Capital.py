import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    a, b, c, d = map(int, data)
    if a * b == c * d or a * c == b * d or a * d == b * c:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()