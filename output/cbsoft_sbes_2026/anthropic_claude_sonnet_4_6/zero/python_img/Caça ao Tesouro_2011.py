import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    
    clues = []
    for _ in range(K):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        d = int(input_data[idx]); idx += 1
        clues.append((x, y, d))
    
    candidates = []
    for tx in range(N):
        for ty in range(N):
            valid = True
            for (cx, cy, d) in clues:
                dist = abs(tx - cx) + abs(ty - cy)
                if dist != d:
                    valid = False
                    break
            if valid:
                candidates.append((tx, ty))
    
    if len(candidates) == 1:
        print(candidates[0][0], candidates[0][1])
    else:
        print(-1, -1)

solve()