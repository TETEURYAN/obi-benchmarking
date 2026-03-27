import sys
import bisect

data = sys.stdin.read().split()
idx = 0
C = int(data[idx])
idx += 1
T = int(data[idx])
idx += 1
radii = []
for i in range(C):
    radii.append(int(data[idx]))
    idx += 1
sq_radii = [r * r for r in radii]
total = 0
for i in range(T):
    X = int(data[idx])
    idx += 1
    Y = int(data[idx])
    idx += 1
    dist_sq = X * X + Y * Y
    pos = bisect.bisect_left(sq_radii, dist_sq)
    pontos = C - pos
    total += pontos
print(total)