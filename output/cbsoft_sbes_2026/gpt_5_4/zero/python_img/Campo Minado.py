n = int(input())
v = [int(input()) for _ in range(n)]

for i in range(n):
    total = v[i]
    if i > 0:
        total += v[i - 1]
    if i + 1 < n:
        total += v[i + 1]
    print(total)