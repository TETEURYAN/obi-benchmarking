import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    pos = input_data[1]
    
    for i in range(n):
        move = int(input_data[2 + i])
        if move == 1:
            if pos == 'A':
                pos = 'B'
            elif pos == 'B':
                pos = 'A'
        elif move == 2:
            if pos == 'B':
                pos = 'C'
            elif pos == 'C':
                pos = 'B'
        elif move == 3:
            if pos == 'A':
                pos = 'C'
            elif pos == 'C':
                pos = 'A'
                
    print(pos)

if __name__ == '__main__':
    solve()