n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(n):
    total = a[i]
    if i > 0:
        total += a[i - 1]
    if i + 1 < n:
        total += a[i + 1]
    print(total)