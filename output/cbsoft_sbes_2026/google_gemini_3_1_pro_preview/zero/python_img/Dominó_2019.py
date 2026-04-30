import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    ans = ((n + 1) * (n + 2)) // 2
    print(ans)

if __name__ == '__main__':
    solve()