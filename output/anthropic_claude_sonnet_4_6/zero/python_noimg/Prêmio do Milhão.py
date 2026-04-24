
n = int(input())
total = 0
for i in range(1, n + 1):
    a = int(input())
    total += a
    if total >= 1000000:
        print(i)
        break
