
import sys

input = sys.stdin.read
data = input().split()

C = int(data[0])
T = int(data[1])

index = 2
radii = []
for i in range(C):
    radii.append(int(data[index]))
    index += 1

shots = []
for i in range(T):
    x = int(data[index])
    y = int(data[index + 1])
    shots.append((x, y))
    index += 2

total = 0
for x, y in shots:
    dist_sq = x * x + y * y
    left = 0
    right = C - 1
    pos = -1
    while left <= right:
        mid = (left + right) // 2
        if radii[mid] * radii[mid] >= dist_sq:
            pos = mid
            right = mid - 1
        else:
            left = mid + 1
    if pos != -1:
        total += (C - pos)

print(total)
