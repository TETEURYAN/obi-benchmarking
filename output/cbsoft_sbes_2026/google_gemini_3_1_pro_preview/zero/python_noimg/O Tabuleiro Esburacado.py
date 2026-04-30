import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    moves = [int(x) for x in input_data[1:n+1]]
    
    holes = {(1, 3), (2, 3), (2, 5), (5, 4)}
    
    move_map = {
        1: (1, 2),
        2: (2, 1),
        3: (2, -1),
        4: (1, -2),
        5: (-1, -2),
        6: (-2, -1),
        7: (-2, 1),
        8: (-1, 2)
    }
    
    x, y = 4, 3
    count = 0
    
    for m in moves:
        dx, dy = move_map[m]
        x += dx
        y += dy
        count += 1
        if (x, y) in holes:
            break
            
    print(count)

if __name__ == '__main__':
    main()