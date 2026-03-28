import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    A = int(next(it)) - 1
    B = int(next(it)) - 1
    grid = []
    for _ in range(L):
        row = [int(next(it)) for _ in range(C)]
        grid.append(row)
    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    atual = (A, B)
    anterior = None
    
    while True:
        i, j = atual
        neighbors = []
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < L and 0 <= nj < C and grid[ni][nj] == 1:
                neighbors.append((ni, nj))
        count = len(neighbors)
        if anterior is None:
            if count != 1:
                break
            proximo = neighbors[0]
        else:
            if count == 1:
                if neighbors[0] == anterior:
                    break
                else:
                    break
            elif count == 2:
                if neighbors[0] == anterior:
                    proximo = neighbors[1]
                else:
                    proximo = neighbors[0]
            else:
                break
        anterior = atual
        atual = proximo
    
    print(atual[0] + 1, atual[1] + 1)

if __name__ == "__main__":
    main()