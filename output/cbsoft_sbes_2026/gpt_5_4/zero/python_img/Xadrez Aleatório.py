n, t = map(int, input().split())

if t == 0:
    print(n)
elif t == 1:
    print(n * (n - 1))
else:
    print(n * (n - 1) * (n - 2) // 6)