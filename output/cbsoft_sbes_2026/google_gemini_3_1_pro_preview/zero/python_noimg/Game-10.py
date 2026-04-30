import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    N = int(lines[0])
    D = int(lines[1])
    A = int(lines[2])
    
    if D >= A:
        print(D - A)
    else:
        print(N - A + D)

if __name__ == '__main__':
    solve()