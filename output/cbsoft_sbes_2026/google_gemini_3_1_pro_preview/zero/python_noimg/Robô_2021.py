import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    C = int(input_data[1])
    S = int(input_data[2])
    
    commands = [int(x) for x in input_data[3:3+C]]
    
    curr = 1
    ans = 1 if curr == S else 0
    
    for cmd in commands:
        curr += cmd
        if curr > N:
            curr = 1
        elif curr < 1:
            curr = N
            
        if curr == S:
            ans += 1
            
    print(ans)

if __name__ == '__main__':
    solve()