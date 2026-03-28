import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

A = int(data[0])
B = int(data[1])

sa = data[2:2 + A]
sb = data[2 + A:2 + A + B]

j = 0
for x in sa:
    if x == sb[j]:
        j += 1
        if j == B:
            print('S')
            break
else:
    print('N')