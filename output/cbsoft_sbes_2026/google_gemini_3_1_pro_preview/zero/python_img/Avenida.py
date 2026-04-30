import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    d = int(input_data[0])
    rem = d % 400
    print(min(rem, 400 - rem))

if __name__ == '__main__':
    solve()