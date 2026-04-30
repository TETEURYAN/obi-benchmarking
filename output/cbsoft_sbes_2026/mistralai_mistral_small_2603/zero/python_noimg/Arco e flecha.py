
import sys
import bisect

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1

    distances = []
    penalties = []
    X_prev = 0
    Y_prev = 0

    for _ in range(N):
        X = int(input[ptr])
        Y = int(input[ptr + 1])
        ptr += 2

        XR = X + X_prev
        YR = Y + Y_prev

        distance = XR * XR + YR * YR
        penalty = bisect.bisect_right(distances, distance)
        penalties.append(penalty)

        bisect.insort(distances, distance)

        X_prev = penalty
        Y_prev = penalty

    print('\n'.join(map(str, penalties)))

if __name__ == "__main__":
    main()
