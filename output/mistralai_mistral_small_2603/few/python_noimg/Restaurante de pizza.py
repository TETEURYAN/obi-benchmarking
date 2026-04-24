
import sys

def main():
    data = sys.stdin.read().split()
    A = int(data[0])
    B = int(data[1])
    R = int(data[2])
    G = int(data[3])

    diameter = 2 * R
    fits_in_box = (A >= diameter) and (B >= diameter)

    if not fits_in_box:
        print('N')
        return

    if G == 360:
        print('S')
        return

    max_slices = 360 // G
    if max_slices >= 1:
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()
