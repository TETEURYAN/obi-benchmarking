import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a + b < c:
    print(1)
elif a < b or b < c:
    print(2)
else:
    print(3)