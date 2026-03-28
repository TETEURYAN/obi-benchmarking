import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    M = int(data[0])
    grid = []
    idx = 1
    for _ in range(M):
        grid.append(data[idx])
        idx += 1
    A = int(data[idx])
    B = int(data[idx + 1])
    
    visited = [[False] * M for _ in range(M)]
    i, j = A - 1, B - 1
    tempo = 0
    
    while True:
        if i < 0 or i >= M or j < 0 or j >= M:
            print(-1)
            return
        if grid[i][j] == 'X':
            print(tempo)
            return
        if visited[i][j]:
            print(0)
            return
        visited[i][j] = True
        d = grid[i][j]
        if d == 'N':
            i -= 1
        elif d == 'S':
            i += 1
        elif d == 'L':
            j += 1
        elif d == 'O':
            j -= 1
        tempo += 1

if __name__ == "__main__":
    main()