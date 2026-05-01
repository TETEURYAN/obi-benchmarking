
import sys

def main():
    data = sys.stdin.read().split()
    A, B, C = map(int, data[:3])
    H, L = map(int, data[3:5])

    dimensions = [A, B, C]
    dimensions.sort()

    if (dimensions[0] <= H and dimensions[1] <= L) or (dimensions[0] <= L and dimensions[1] <= H):
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()
