import sys

a = list(map(int, sys.stdin.read().split()))
s = sum(a)

if s % 3 != 0:
    print('N')
    sys.exit()

target = s // 3
n = 6

for i in range(n):
    if a[i] == target:
        rem1 = [a[j] for j in range(n) if j != i]
        m = len(rem1)
        for mask in range(1 << m):
            if mask.bit_count() == 2:
                sm = 0
                for k in range(m):
                    if mask >> k & 1:
                        sm += rem1[k]
                if sm == target:
                    print('S')
                    sys.exit()

print('N')