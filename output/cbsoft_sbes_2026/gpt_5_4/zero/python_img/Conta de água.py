n = int(input().strip())

if n <= 10:
    print(7)
elif n <= 30:
    print(7 + (n - 10) * 1)
elif n <= 100:
    print(7 + 20 + (n - 30) * 2)
else:
    print(7 + 20 + 140 + (n - 100) * 5)