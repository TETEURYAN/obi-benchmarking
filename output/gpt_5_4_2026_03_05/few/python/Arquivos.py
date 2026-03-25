import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
b = data[1]
a = data[2:2 + n]

a.sort()

i = 0
j = n - 1
folders = 0

while i <= j:
    if i == j:
        folders += 1
        break
    if a[i] + a[j] <= b:
        i += 1
        j -= 1
    else:
        j -= 1
    folders += 1

print(folders)