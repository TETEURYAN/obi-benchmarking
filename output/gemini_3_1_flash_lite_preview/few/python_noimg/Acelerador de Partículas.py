import sys

def solve():
    d = int(sys.stdin.read().strip())
    res = (d - 3) % 8
    if res == 3:
        print(1)
    elif res == 4:
        print(2)
    elif res == 5:
        print(3)

if __name__ == '__main__':
    solve()