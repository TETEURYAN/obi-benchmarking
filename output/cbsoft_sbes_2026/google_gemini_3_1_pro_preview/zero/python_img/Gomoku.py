import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    grid = [int(x) for x in input_data]
    
    def get(r, c):
        return grid[r * 15 + c]
        
    for r in range(15):
        for c in range(15):
            color = get(r, c)
            if color == 0:
                continue
                
            if c + 4 < 15:
                if all(get(r, c+i) == color for i in range(5)):
                    print(color)
                    return
            if r + 4 < 15:
                if all(get(r+i, c) == color for i in range(5)):
                    print(color)
                    return
            if r + 4 < 15 and c + 4 < 15:
                if all(get(r+i, c+i) == color for i in range(5)):
                    print(color)
                    return
            if r + 4 < 15 and c - 4 >= 0:
                if all(get(r+i, c-i) == color for i in range(5)):
                    print(color)
                    return
                    
    print(0)

if __name__ == '__main__':
    solve()