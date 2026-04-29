d = int(input())

r = (d - 3) % 8

if r == 3:
    print(1)
elif r == 4:
    print(2)
else:
    print(3)