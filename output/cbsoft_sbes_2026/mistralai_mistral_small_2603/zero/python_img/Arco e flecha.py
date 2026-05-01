
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        points.append((x, y))

    penalties = []
    distances = []
    x_prev, y_prev = 0, 0

    for i in range(n):
        xk, yk = points[i]
        xr = xk + x_prev
        yr = yk + y_prev
        d = xr * xr + yr * yr

        if i == 0:
            penalty = 0
        else:
            pos = bisect.bisect_right(distances, d)
            penalty = len(distances) - pos

        penalties.append(penalty)
        bisect.insort(distances, d)
        x_prev, y_prev = penalty, penalty

    for p in penalties:
        print(p)

if __name__ == "__main__":
    main()
