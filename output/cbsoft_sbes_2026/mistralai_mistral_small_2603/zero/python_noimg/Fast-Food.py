
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    X = list(map(int, data[1:n+1]))
    Y = list(map(int, data[n+1:2*n+1]))

    points = list(zip(X, Y))
    points.sort()

    max_dist = 0
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            if dist > max_dist:
                max_dist = dist
                if max_dist >= (points[-1][0] - points[0][0] + points[-1][1] - points[0][1]):
                    break
        if max_dist >= (points[-1][0] - points[0][0] + points[-1][1] - points[0][1]):
            break

    print(max_dist)

if __name__ == "__main__":
    main()
