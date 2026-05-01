
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    X = list(map(int, data[1:n+1]))
    Y = list(map(int, data[n+1:2*n+1]))

    points = list(zip(X, Y))
    points.sort()

    min_x = points[0][0]
    max_x = points[-1][0]
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    candidate1 = max_x - min_x
    candidate2 = max_y - min_y

    print(max(candidate1, candidate2))

if __name__ == "__main__":
    main()
