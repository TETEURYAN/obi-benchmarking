import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    varetas = list(map(int, input_data))
    varetas.sort()

    if varetas[0] + varetas[1] > varetas[2] or varetas[1] + varetas[2] > varetas[3]:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    solve()