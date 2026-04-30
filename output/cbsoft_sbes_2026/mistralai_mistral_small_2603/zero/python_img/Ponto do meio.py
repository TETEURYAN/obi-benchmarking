t(input().strip())

if n == 0:
    print(4)
else:
    total = 4
    for i in range(1, n + 1):
        total += 5 * (2 * i - 1)
    print(total)
