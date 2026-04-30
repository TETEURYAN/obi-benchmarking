import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    ans = 0
    for i in range(1, n + 1):
        ans += int(input_data[i]) - 1
    print(ans)

if __name__ == '__main__':
    solve()