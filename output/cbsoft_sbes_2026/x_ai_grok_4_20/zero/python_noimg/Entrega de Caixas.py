
a = int(input())
b = int(input())
c = int(input())

if a + b < c:
    print(1)
elif a == b == c:
    print(3)
elif b == c:
    print(2)
elif a + b < c * 2:
    print(2)
else:
    print(3)
