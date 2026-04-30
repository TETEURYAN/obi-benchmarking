import sys

def solve():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        ans = ((1 << n) + 1) ** 2
        print(ans)

if __name__ == '__main__':
    solve()