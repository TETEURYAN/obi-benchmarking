import sys

data = sys.stdin.read().split()
N = int(data[0])

if N < 2:
    print(0)
    print(0)
    print(0)
    print(0)
else:
    zero = (N - 2) ** 3
    one = 6 * (N - 2) ** 2
    two = 12 * (N - 2)
    three = 8
    print(zero)
    print(one)
    print(two)
    print(three)