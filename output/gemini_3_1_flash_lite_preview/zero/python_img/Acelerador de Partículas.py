import sys

def solve():
    d = int(sys.stdin.readline())
    res = (d - 3) % 8
    if res == 3:
        print(1)
    elif res == 4:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    solve()