
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    points = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        points.append((x, y))

    penalties = []
    distances = []
    x_prev, y_prev = 0, 0

    for i in range(n):
        x, y = points[i]
        x_real = x + x_prev
        y_real = y + y_prev
        distance = x_real * x_real + y_real * y_real

        penalty = bisect.bisect_right(distances, distance)
        penalties.append(penalty)

        x_prev += penalty
        y_prev += penalty

        bisect.insort(distances, distance)

    for p in penalties:
        print(p)

if __name__ == "__main__":
    main()
