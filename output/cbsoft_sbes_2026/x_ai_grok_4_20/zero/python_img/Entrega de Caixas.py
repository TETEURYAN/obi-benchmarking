
a = int(input())
b = int(input())
c = int(input())

if a + b < c:
    print(1)
elif b == c and a + b < c:
    print(1)
elif a == b and b + a < c:
    print(1)
elif a + b < c or a + c < b or b + c < a:
    print(1)
elif a == b == c:
    print(3)
elif b == c:
    print(2)
elif a + b <= c:
    print(2)
else:
    print(2)
