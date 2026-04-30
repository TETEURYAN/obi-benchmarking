
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
X = list(map(int, data[1:1+N]))
Y = list(map(int, data[1+N:1+2*N]))

points = [(X[i], Y[i]) for i in range(N)]

def can_assign(D):
    for rot in range(4):
        if rot == 1:
            pts = [(-y, x) for x, y in points]
        elif rot == 2:
            pts = [(-x, -y) for x, y in points]
        elif rot == 3:
            pts = [(y, -x) for x, y in points]
        else:
            pts = points[:]
        
        pts.sort()
        
        min_y = [float('inf')] * N
        max_y = [float('-inf')] * N
        min_y[N-1] = max_y[N-1] = pts[N-1][1]
        for i in range(N-2, -1, -1):
            min_y[i] = min(min_y[i+1], pts[i][1])
            max_y[i] = max(max_y[i+1], pts[i][1])
        
        j = 0
        for i in range(N):
            while j < N and pts[j][0] - pts[i][0] <= D:
                j += 1
            if j == N:
                break
            if max_y[j] - min_y[j] > D:
                continue
            if max(max_y[j] - pts[i][1], pts[i][1] - min_y[j]) <= D:
                return True
    return False

lo = 0
hi = 2 * 10**9
while lo < hi:
    mid = (lo + hi) // 2
    if can_assign(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)
