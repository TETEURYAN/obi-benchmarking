
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    compressed = []
    for x in a:
        if not compressed or compressed[-1] != x:
            compressed.append(x)
            
    ans = 0
    while len(compressed) > 1:
        min_val = min(compressed)
        idx = compressed.index(min_val)
        
        neighbors = []
        if idx > 0:
            neighbors.append(compressed[idx-1])
        if idx < len(compressed) - 1:
            neighbors.append(compressed[idx+1])
            
        min_neighbor = min(neighbors)
        
        ans += min_neighbor - min_val
        compressed[idx] = min_neighbor
        
        new_compressed = []
        for x in compressed:
            if not new_compressed or new_compressed[-1] != x:
                new_compressed.append(x)
        compressed = new_compressed

    print(ans)

if __name__ == '__main__':
    solve()
