
import sys
import math

def dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

test = 1
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    N = int(line)
    if N == 0:
        break
    points = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    
    if N == 1:
        diam = 5
    else:
        max_min_d = 0.0
        for i in range(N):
            min_d_to_other = float('inf')
            for j in range(N):
                if i != j:
                    d = dist(points[i][0], points[i][1], points[j][0], points[j][1])
                    if d < min_d_to_other:
                        min_d_to_other = d
            if min_d_to_other > max_min_d:
                max_min_d = min_d_to_other
        diam = math.ceil(max_min_d + 5.0)
    
    print(f"Teste {test}")
    print(diam)
    print()
    test += 1
