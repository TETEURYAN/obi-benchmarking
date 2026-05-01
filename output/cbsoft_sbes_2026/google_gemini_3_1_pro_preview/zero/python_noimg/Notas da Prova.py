import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    if n == 0:
        print("E")
    elif n <= 35:
        print("D")
    elif n <= 60:
        print("C")
    elif n <= 85:
        print("B")
    else:
        print("A")

if __name__ == '__main__':
    solve()