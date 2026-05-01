import sys

data = sys.stdin.read().split()
if not data:
    exit()

d = int(data[0])

if d <= 800:
    print(1)
elif d <= 1400:
    print(2)
else:
    print(3)