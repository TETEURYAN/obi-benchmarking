n = int(input())
a = list(map(int, input().split()))

count = 0
max_from_right = 0

for i in range(n - 1, -1, -1):
    if i == n - 1:
        max_from_right = a[i]
    else:
        if max_from_right >= a[i]:
            count += 1
        else:
            max_from_right = a[i]

print(count)