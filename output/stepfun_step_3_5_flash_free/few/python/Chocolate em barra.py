import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    x1 = int(data[1])
    y1 = int(data[2])
    x2 = int(data[3])
    y2 = int(data[4])
    metade = n // 2
    horizontal = (x1 <= metade and x2 > metade) or (x1 > metade and x2 <= metade)
    vertical = (y1 <= metade and y2 > metade) or (y1 > metade and y2 <= metade)
    print('S' if horizontal or vertical else 'N')

if __name__ == "__main__":
    main()