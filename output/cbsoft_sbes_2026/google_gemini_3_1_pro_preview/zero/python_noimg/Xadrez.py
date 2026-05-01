import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    L = int(input_data[0])
    C = int(input_data[1])
    
    if (L + C) % 2 == 0:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    solve()