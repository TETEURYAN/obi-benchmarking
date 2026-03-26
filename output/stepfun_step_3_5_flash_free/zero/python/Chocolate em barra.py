
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    x1 = int(data[1])
    y1 = int(data[2])
    x2 = int(data[3])
    y2 = int(data[4])
    metade = n // 2
    if (x1 <= metade) != (x2 <= metade) or (y1 <= metade) != (y2 <= metade):
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()
