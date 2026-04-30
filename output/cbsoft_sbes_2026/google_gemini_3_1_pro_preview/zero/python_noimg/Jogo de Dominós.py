import sys

def solve():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        print((n + 1) * (n + 2) // 2)

if __name__ == '__main__':
    solve()