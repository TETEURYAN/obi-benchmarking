import sys

def main():
    L = int(sys.stdin.read())
    pieces = 1
    while L >= 2:
        pieces *= 4
        L = L // 2
    print(pieces)

if __name__ == '__main__':
    main()