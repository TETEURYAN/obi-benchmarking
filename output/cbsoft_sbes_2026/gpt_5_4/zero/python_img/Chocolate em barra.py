import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    metade = n // 2

    horizontal = (x1 <= metade < x2) or (x2 <= metade < x1)
    vertical = (y1 <= metade < y2) or (y2 <= metade < y1)

    print("S" if horizontal or vertical else "N")

if __name__ == "__main__":
    main()
