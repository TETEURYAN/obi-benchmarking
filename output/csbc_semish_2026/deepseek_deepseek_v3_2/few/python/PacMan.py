import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    grid = data[1:1 + n]
    
    total = 0
    best = 0
    
    for i in range(n):
        if i % 2 == 0:
            # left to right
            for j in range(n):
                cell = grid[i][j]
                if cell == 'o':
                    total += 1
                elif cell == 'A':
                    total = 0
                best = max(best, total)
        else:
            # right to left
            for j in range(n - 1, -1, -1):
                cell = grid[i][j]
                if cell == 'o':
                    total += 1
                elif cell == 'A':
                    total = 0
                best = max(best, total)
    
    print(best)

if __name__ == "__main__":
    main()