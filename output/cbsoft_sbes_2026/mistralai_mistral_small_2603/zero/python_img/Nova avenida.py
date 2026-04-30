
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        grid.append(row)
        index += m

    min_total = float('inf')
    for col in range(m):
        total = 0
        for row in range(n):
            total += grid[row][col]
        if total < min_total:
            min_total = total

    print(min_total)

if __name__ == "__main__":
    main()
