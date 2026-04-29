m, n = map(int, input().split())

a, b = min(m, n), max(m, n)

if a == 1:
    print(m * n)
elif a == 2:
    groups = b // 4
    rem = b % 4
    print(groups * 4 + min(2, rem) * 2)
else:
    print((m * n + 1) // 2)