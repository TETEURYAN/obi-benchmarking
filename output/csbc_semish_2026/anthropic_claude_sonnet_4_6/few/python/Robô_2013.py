import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx]); idx+=1
    C = int(data[idx]); idx+=1
    A = int(data[idx])-1; idx+=1
    B = int(data[idx])-1; idx+=1
    
    grid = []
    for i in range(L):
        row = []
        for j in range(C):
            row.append(int(data[idx])); idx+=1
        grid.append(row)
    
    # Walk the path from (A,B), the start has exactly one black neighbor
    # We traverse until we reach a tile with only one black neighbor (the end)
    
    cur = (A, B)
    prev = None
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while True:
        r, c = cur
        neighbors = []
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 1:
                neighbors.append((nr, nc))
        
        # Find next: neighbor that is not prev
        nxt = None
        for nb in neighbors:
            if nb != prev:
                nxt = nb
                break
        
        if nxt is None:
            # dead end, this is the final position
            break
        
        prev = cur
        cur = nxt
    
    print(cur[0]+1, cur[1]+1)

main()