import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    ans = sum(int(x) - 1 for x in input_data[1:n+1])
    print(ans)

if __name__ == '__main__':
    solve()