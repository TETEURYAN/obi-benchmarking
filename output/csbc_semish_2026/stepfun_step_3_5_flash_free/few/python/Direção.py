import sys

data = sys.stdin.read().split()
A, B = data[0], data[1]
dirs = {'norte': 0, 'leste': 90, 'sul': 180, 'oeste': 270}
a = dirs[A]
b = dirs[B]
diff = abs(a - b)
print(min(diff, 360 - diff))