import sys

def main():
    data = sys.stdin.read().strip().split()
    if len(data) != 4:
        return
    A = sorted(map(int, data))
    # Check if the four areas can be arranged as two pairs of equal rectangles
    # Conditions: possible arrangements: (A1*A4 == A2*A3) OR (A1*A3 == A2*A4) OR (A1*A2 == A3*A4)
    # Since sorted, we test combinations:
    if (A[0] * A[3] == A[1] * A[2]) or (A[0] * A[2] == A[1] * A[3]) or (A[0] * A[1] == A[2] * A[3]):
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()