d = int(input().strip())

r = d % 8
if r == 6:
    print(1)
elif r == 7:
    print(2)
else:
    print(3)