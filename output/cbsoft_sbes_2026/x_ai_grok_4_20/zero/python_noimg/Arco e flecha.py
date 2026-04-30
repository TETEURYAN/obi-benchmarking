
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
arrows = []
index = 1
for i in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    arrows.append((x, y))
    index += 2

penalties = [0] * N
prev_p = 0
points = []

for k in range(N):
    xr = arrows[k][0] + prev_p
    yr = arrows[k][1] + prev_p
    r2 = xr * xr + yr * yr
    points.append(r2)
    
    if k == 0:
        p = 0
    else:
        p = 0
        for i in range(k):
            if points[i] <= r2:
                p += 1
    penalties[k] = p
    prev_p = p

for p in penalties:
    print(p)
