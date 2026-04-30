
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
X = list(map(int, data[1:1+N]))
Y = list(map(int, data[1+N:1+2*N]))

points = [(X[i], Y[i]) for i in range(N)]

def can_distribute(D):
    for rot in range(2):
        if rot == 1:
            pts = [(-x + y, x + y) for x, y in points]
        else:
            pts = [(x + y, x - y) for x, y in points]
        
        xs = sorted(set(p[0] for p in pts))
        rank = {val: i for i, val in enumerate(xs)}
        max_rank = len(xs)
        
        events = []
        for px, py in pts:
            left = px - D
            right = px + D
            lo = 0
            hi = max_rank - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if xs[mid] >= left:
                    hi = mid
                else:
                    lo = mid + 1
            l_idx = lo
            
            lo = 0
            hi = max_rank - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if xs[mid] <= right:
                    lo = mid
                else:
                    hi = mid - 1
            r_idx = lo
            
            if l_idx > r_idx:
                continue
            events.append((l_idx, 1, py))
            events.append((r_idx + 1, -1, py))
        
        if not events:
            return True
        events.sort()
        
        active = []
        i = 0
        M = len(events)
        while i < M:
            curr_xrank = events[i][0]
            while i < M and events[i][0] == curr_xrank:
                delta, py_val = events[i][1], events[i][2]
                if delta == 1:
                    active.append(py_val)
                else:
                    active.remove(py_val)
                i += 1
            if not active:
                continue
            active.sort()
            for j in range(1, len(active)):
                if active[j] - active[j-1] <= D:
                    return True
    return False

low = 0
high = 2 * 10**9
while low < high:
    mid = (low + high) // 2
    if can_distribute(mid):
        high = mid
    else:
        low = mid + 1

print(low)
