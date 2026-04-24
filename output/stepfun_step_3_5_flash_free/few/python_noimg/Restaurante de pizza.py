import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    A, B, R, G = map(int, data)
    if 2 * R <= min(A, B) and 360 % G == 0:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()