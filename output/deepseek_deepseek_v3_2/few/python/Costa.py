import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    M = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    grid = data[idx:idx+M]
    
    coast = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] != '#':
                continue
            # checa bordas do mapa
            if i == 0 or i == M-1 or j == 0 or j == N-1:
                coast += 1
                continue
            # checa vizinhos
            if (grid[i-1][j] == '.' or grid[i+1][j] == '.' or 
                grid[i][j-1] == '.' or grid[i][j+1] == '.'):
                coast += 1
    print(coast)

if __name__ == "__main__":
    main()