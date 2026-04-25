
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    M_squared = M * M
    
    x = 0
    y = 0
    
    for _ in range(N):
        direction = data[idx]
        idx += 1
        distance = int(data[idx])
        idx += 1
        
        if direction == 'N':
            y += distance
        elif direction == 'S':
            y -= distance
        elif direction == 'L':
            x += distance
        elif direction == 'O':
            x -= distance
        
        if x * x + y * y > M_squared:
            print(1)
            return
    
    print(0)

solve()
