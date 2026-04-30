import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    x = [int(i) for i in input_data[1:n+1]]
    
    h = max(x)
    for i in range(h, 0, -1):
        row = []
        for val in x:
            if val >= i:
                row.append('1')
            else:
                row.append('0')
        print(' '.join(row))

if __name__ == '__main__':
    solve()