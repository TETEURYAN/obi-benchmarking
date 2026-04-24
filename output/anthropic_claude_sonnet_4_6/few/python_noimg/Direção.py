import sys

data = sys.stdin.read().split()
A = data[0]
B = data[1]

angles = {'norte': 0, 'leste': 90, 'sul': 180, 'oeste': 270}

a = angles[A]
b = angles[B]

diff = abs(a - b)
result = min(diff, 360 - diff)
print(result)