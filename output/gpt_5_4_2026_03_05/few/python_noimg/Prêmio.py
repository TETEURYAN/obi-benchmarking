import sys

data = list(map(int, sys.stdin.read().split()))
p, d, b = data[0], data[1], data[2]

points = p + 2 * d + 3 * b

if points >= 150:
    print('B')
elif points >= 120:
    print('D')
elif points >= 100:
    print('P')
else:
    print('N')