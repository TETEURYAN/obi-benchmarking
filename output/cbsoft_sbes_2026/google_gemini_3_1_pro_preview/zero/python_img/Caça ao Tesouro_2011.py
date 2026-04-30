import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    x0 = int(input_data[2])
    y0 = int(input_data[3])
    d0 = int(input_data[4])
    
    clues = []
    idx = 5
    for _ in range(K - 1):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        d = int(input_data[idx+2])
        clues.append((x, y, d))
        idx += 3
        
    possible_locations = []
    
    for dx in range(-d0, d0 + 1):
        dy = d0 - abs(dx)
        
        px, py = x0 + dx, y0 + dy
        if 0 <= px < N and 0 <= py < N:
            valid = True
            for cx, cy, cd in clues:
                if abs(px - cx) + abs(py - cy) != cd:
                    valid = False
                    break
            if valid:
                possible_locations.append((px, py))
        
        if dy != 0:
            px, py = x0 + dx, y0 - dy
            if 0 <= px < N and 0 <= py < N:
                valid = True
                for cx, cy, cd in clues:
                    if abs(px - cx) + abs(py - cy) != cd:
                        valid = False
                        break
                if valid:
                    possible_locations.append((px, py))
                    
    if len(possible_locations) == 1:
        print(f"{possible_locations[0][0]} {possible_locations[0][1]}")
    else:
        print("-1 -1")

if __name__ == '__main__':
    solve()