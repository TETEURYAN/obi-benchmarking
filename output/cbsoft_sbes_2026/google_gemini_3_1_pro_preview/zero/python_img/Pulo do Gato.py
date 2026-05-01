
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    C = int(input_data[0])
    tiles = [int(x) for x in input_data[1:C+1]]
    
    pos = 0
    jumps = 0
    
    while pos < C - 1:
        if pos + 2 < C and tiles[pos + 2] == 1:
            pos += 2
        elif pos + 1 < C and tiles[pos + 1] == 1:
            pos += 1
        else:
            print("-1")
            return
        jumps += 1
        
    print(jumps)

if __name__ == '__main__':
    solve()
