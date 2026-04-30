
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    moves = [int(x) for x in input_data[1:N+1]]
    
    holes = {(1, 3), (2, 3), (2, 5), (5, 4)}
    
    moves_dict = {
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
    moves_made = 0
    
    for move in moves:
        dx, dy = moves_dict[move]
        x += dx
        y += dy
        moves_made += 1
        
        if (x, y) in holes:
            break
            
    print(moves_made)

if __name__ == '__main__':
    main()
