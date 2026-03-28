import sys

a = list(map(int, sys.stdin.read().split()))
total = sum(a)

if total % 2 != 0:
    print('N')
    sys.exit()

target = total // 2

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            if a[i] + a[j] + a[k] == target:
                print('S')
                sys.exit()

print('N')