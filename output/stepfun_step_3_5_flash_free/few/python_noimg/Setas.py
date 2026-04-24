import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    grid = data[1:1+n]
    status = [[0]*n for _ in range(n)]
    dirs = {'V': (1,0), '<': (0,-1), '>': (0,1), 'A': (-1,0)}
    
    def get_next(i, j):
        d = grid[i][j]
        di, dj = dirs[d]
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n:
            return (ni, nj)
        return None
    
    for i in range(n):
        for j in range(n):
            if status[i][j] == 0:
                stack = []
                pos_map = {}
                current = (i, j)
                while True:
                    ci, cj = current
                    if status[ci][cj] == 0:
                        status[ci][cj] = 1
                        pos_map[current] = len(stack)
                        stack.append(current)
                        nxt = get_next(ci, cj)
                        if nxt is None:
                            for cell in stack:
                                status[cell[0]][cell[1]] = 3
                            break
                        else:
                            current = nxt
                    elif status[ci][cj] == 1:
                        for cell in stack:
                            status[cell[0]][cell[1]] = 2
                        break
                    else:
                        cls = status[ci][cj]
                        for cell in stack:
                            status[cell[0]][cell[1]] = cls
                        break
    
    count = 0
    for i in range(n):
        for j in range(n):
            if status[i][j] == 2:
                count += 1
    print(count)

if __name__ == "__main__":
    main()