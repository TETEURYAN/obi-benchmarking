import sys

def main():
    A = list(map(int, sys.stdin.read().split()))
    A1, A2, A3, A4 = A

    total = A1 + A2 + A3 + A4
    if total % 4 != 0:
        print('N')
        return

    target = total // 4
    areas = [A1, A2, A3, A4]

    for i in range(4):
        if areas[i] > target:
            print('N')
            return

    print('S')

if __name__ == '__main__':
    main()