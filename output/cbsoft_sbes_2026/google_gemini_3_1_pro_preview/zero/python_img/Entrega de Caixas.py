import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    B = int(input_data[1])
    C = int(input_data[2])
    
    if (A < B and B < C) or (A + B < C):
        print(1)
    elif A < B or B < C:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    solve()