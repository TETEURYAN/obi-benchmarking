import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    grid = []
    idx = 0
    for _ in range(15):
        row = []
        for _ in range(15):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for r in range(15):
        for c in range(15):
            color = grid[r][c]
            if color == 0:
                continue
            
            for dr, dc in directions:
                if 0 <= r + 4 * dr < 15 and 0 <= c + 4 * dc < 15:
                    win = True
                    for k in range(1, 5):
                        if grid[r + k * dr][c + k * dc] != color:
                            win = False
                            break
                    if win:
                        print(color)
                        return
    print(0)

if __name__ == '__main__':
    main()