
import sys
import math

def dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

def min_diameter(points):
    if not points:
        return 5
    n = len(points)
    if n == 1:
        return 5
    max_min_r = 0.0
    for i in range(n):
        min_r = 0.0
        for j in range(n):
            if i != j:
                d = dist(points[i][0], points[i][1], points[j][0], points[j][1])
                min_r = max(min_r, d)
        max_min_r = max(max_min_r, min_r)
    diameter = math.ceil(max_min_r * 2)
    return max(diameter, 5)

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    test_num = 1
    while True:
        N = int(data[index])
        index += 1
        if N == 0:
            break
        points = []
        for _ in range(N):
            X = int(data[index])
            Y = int(data[index + 1])
            index += 2
            points.append((X, Y))
        diam = min_diameter(points)
        print(f"Teste {test_num}")
        print(diam)
        print()
        test_num += 1

if __name__ == "__main__":
    main()
