
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    clues = []
    idx = 2
    for _ in range(K):
        clues.append((int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])))
        idx += 3
        
    possible = []
    for x in range(N):
        for y in range(N):
            valid = True
            for cx, cy, cd in clues:
                if abs(x - cx) + abs(y - cy) != cd:
                    valid = False
                    break
            if valid:
                possible.append((x, y))
                if len(possible) > 1:
                    print("-1 -1")
                    return
                    
    if len(possible) == 1:
        print(f"{possible[0][0]} {possible[0][1]}")
    else:
        print("-1 -1")

if __name__ == '__main__':
    solve()
