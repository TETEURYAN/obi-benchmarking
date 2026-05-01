import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    C = int(input_data[1])
    S = int(input_data[2])
    
    commands = [int(x) for x in input_data[3:3+C]]
    
    pos = 1
    count = 1 if pos == S else 0
    
    for cmd in commands:
        pos = (pos - 1 + cmd) % N + 1
        if pos == S:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()