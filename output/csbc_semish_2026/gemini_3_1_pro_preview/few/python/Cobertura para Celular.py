import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    x = [0] * N
    y = [0] * N
    idx = 1
    for i in range(N):
        x[i] = int(input_data[idx])
        y[i] = int(input_data[idx+1])
        idx += 2
    
    A = int(input_data[idx])
    A2 = A * A
    
    cell_size = max(1, A)
    
    grid = {}
    for i in range(N):
        cell = (x[i] // cell_size, y[i] // cell_size)
        if cell not in grid:
            grid[cell] = set()
        grid[cell].add(i)
        
    queue = [0]
    start_cell = (x[0] // cell_size, y[0] // cell_size)
    grid[start_cell].remove(0)
    if not grid[start_cell]:
        del grid[start_cell]
        
    visited_count = 1
    if visited_count == N:
        print("S")
        return
        
    head = 0
    while head < len(queue):
        curr = queue[head]
        head += 1
        cx = x[curr]
        cy = y[curr]
        cx_cell = cx // cell_size
        cy_cell = cy // cell_size
        
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                cell = (cx_cell + dx, cy_cell + dy)
                if cell in grid:
                    cell_set = grid[cell]
                    to_remove = []
                    for nxt in cell_set:
                        if (x[nxt] - cx)**2 + (y[nxt] - cy)**2 <= A2:
                            queue.append(nxt)
                            to_remove.append(nxt)
                            visited_count += 1
                            if visited_count == N:
                                print("S")
                                return
                    if len(to_remove) == len(cell_set):
                        del grid[cell]
                    else:
                        for nxt in to_remove:
                            cell_set.remove(nxt)
                            
    print("N")

if __name__ == '__main__':
    solve()