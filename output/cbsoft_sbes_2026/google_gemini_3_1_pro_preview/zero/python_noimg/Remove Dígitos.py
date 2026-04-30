import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    steps = 0
    while n > 0:
        max_d = 0
        temp = n
        while temp > 0:
            d = temp % 10
            if d > max_d:
                max_d = d
            temp //= 10
        n -= max_d
        steps += 1
    print(steps)

if __name__ == '__main__':
    solve()