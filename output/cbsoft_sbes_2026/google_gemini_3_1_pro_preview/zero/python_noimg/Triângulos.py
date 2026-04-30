import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a, b, c = sorted([int(input_data[0]), int(input_data[1]), int(input_data[2])])
    
    if a + b <= c:
        print('n')
    elif a**2 + b**2 == c**2:
        print('r')
    elif a**2 + b**2 > c**2:
        print('a')
    else:
        print('o')

if __name__ == '__main__':
    solve()