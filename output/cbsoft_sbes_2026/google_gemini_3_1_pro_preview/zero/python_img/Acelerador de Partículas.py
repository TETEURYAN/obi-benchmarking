import sys

def main():
    d = int(sys.stdin.read().strip())
    print((d - 3) % 8 - 2)

if __name__ == '__main__':
    main()