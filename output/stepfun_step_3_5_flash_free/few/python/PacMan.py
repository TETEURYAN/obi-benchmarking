import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    grid = data[1:1+n]
    current = 0
    max_food = 0
    for i in range(n):
        cols = range(n) if i % 2 == 0 else range(n-1, -1, -1)
        for j in cols:
            cell = grid[i][j]
            if cell == 'o':
                current += 1
            elif cell == 'A':
                current = 0
            if current > max_food:
                max_food = current
    print(max_food)

if __name__ == "__main__":
    main()