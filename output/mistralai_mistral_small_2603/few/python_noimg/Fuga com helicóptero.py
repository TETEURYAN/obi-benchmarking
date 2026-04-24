import sys

def main():
    H, P, F, D = map(int, sys.stdin.read().split())
    if D == 1:
        if F < H:
            print('S')
        else:
            print('N')
    else:
        if F > H:
            print('S')
        else:
            print('N')

if __name__ == "__main__":
    main()