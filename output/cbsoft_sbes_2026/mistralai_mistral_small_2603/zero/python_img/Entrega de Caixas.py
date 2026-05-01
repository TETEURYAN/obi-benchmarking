a, b, c = int(input()), int(input()), int(input())
if a + b < c:
    print(1)
elif a == b == c:
    print(3)
elif a == b or b == c:
    print(2)
else:
    print(2)