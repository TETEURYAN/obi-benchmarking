import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    sequence = input_data[1:]
    
    count = 0
    for i in range(n - 2):
        if sequence[i] == '1' and sequence[i+1] == '0' and sequence[i+2] == '0':
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()