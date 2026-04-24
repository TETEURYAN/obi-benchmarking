import sys
data = sys.stdin.read().split()
a, b, c = int(data[0]), int(data[1]), int(data[2])
if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)