
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == b + c + d and b + c == d and b == c:
    print('S')
else:
    print('N')
