
import sys

N = int(sys.stdin.readline().strip())

if N == 0:
    print(4)
    sys.exit(0)

points = 4
midpoints = 4
centers = 1

for step in range(1, N + 1):
    new_midpoints = midpoints * 2 + centers * 4
    new_centers = midpoints + centers
    points += new_midpoints + new_centers
    midpoints = new_midpoints
    centers = new_centers

print(points)
