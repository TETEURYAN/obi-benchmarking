
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    x1 = int(data[1])
    y1 = int(data[2])
    x2 = int(data[3])
    y2 = int(data[4])

    if x1 == x2:
        if y1 <= n // 2 and y2 > n // 2:
            print('S')
        elif y2 <= n // 2 and y1 > n // 2:
            print('S')
        else:
            print('N')
    elif y1 == y2:
        if x1 <= n // 2 and x2 > n // 2:
            print('S')
        elif x2 <= n // 2 and x1 > n // 2:
            print('S')
        else:
            print('N')
    else:
        print('N')

if __name__ == "__main__":
    main()
